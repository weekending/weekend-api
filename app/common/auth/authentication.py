from http.cookies import SimpleCookie

from fastapi import Depends
from fastapi.security.utils import get_authorization_scheme_param
from jwt.exceptions import InvalidTokenError
from pydantic import ValidationError
from starlette.exceptions import HTTPException
from starlette.requests import Request

from app.common.exception import APIException
from app.common.http import Http4XX
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
            self.handle_exception(request)

    def get_authorization(self, request: Request) -> str:
        raise NotImplementedError("`get_authorization` must be overridden.")

    def handle_exception(self, request: Request):
        raise APIException(Http4XX.UNAUTHENTICATED)


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
            raise APIException(Http4XX.UNAUTHENTICATED)
        return token


class CookieAuthentication(BaseAuthentication):
    def get_authorization(self, request: Request) -> str:
        cookie = SimpleCookie()
        cookie.load(request.headers.get("Cookie", ""))
        token = cookie.get("token")
        return token.value if token else ""

    def handle_exception(self, request: Request):
        location = f"/login?redirect={request.url.path}"
        raise HTTPException(status_code=302, headers={"Location": location})


class CookieForRedocAuthentication(CookieAuthentication):
    def handle_exception(self, request: Request):
        raise HTTPException(status_code=302, headers={"Location": "/docs/login"})
