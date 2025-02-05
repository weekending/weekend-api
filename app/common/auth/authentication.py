from http.cookies import SimpleCookie

from fastapi import Depends
from fastapi.security.utils import get_authorization_scheme_param
from jwt.exceptions import InvalidTokenError
from pydantic import ValidationError
from starlette.exceptions import HTTPException
from starlette.requests import Request

from .jwt_provider import JWTProvider
from .schemas import JWTAuthorizationCredentials


class BaseAuthentication:
    async def __call__(
        self,
        request: Request,
        jwt: JWTProvider = Depends(JWTProvider),
    ) -> JWTAuthorizationCredentials:
        token = self.get_authorization(request)
        try:
            return JWTAuthorizationCredentials(**jwt.decode_token(token))
        except (ValidationError, InvalidTokenError):
            self.handle_exception()

    def get_authorization(self, request: Request) -> str:
        raise NotImplementedError("`get_authorization` must be overridden.")

    def handle_exception(self):
        raise HTTPException(status_code=401, detail="잘못된 인증")


class Authentication(BaseAuthentication):
    """헤더에 있는 인증 정보를 가져와 유효성을 평가합니다.

    요청시 헤더에 인증 토큰을 추가하여 인증할 수 있습니다.
        "Authorization": "Bearer {token}"
    """

    scheme = "BEARER"

    def get_authorization(self, request: Request) -> str:
        authorization = request.headers.get("Authorization")
        scheme, token = get_authorization_scheme_param(authorization)
        if not authorization or scheme.upper() != self.scheme:
            raise HTTPException(status_code=401, detail="잘못된 인증")
        return token


class CookieAuthentication(BaseAuthentication):
    def get_authorization(self, request: Request) -> str:
        cookie = SimpleCookie()
        cookie.load(request.headers.get("Cookie", ""))
        token = cookie.get("token")
        return token.value if token else ""

    def handle_exception(self):
        raise HTTPException(status_code=302, headers={"Location": "/docs/login"})
