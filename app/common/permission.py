from fastapi import Depends
from starlette.exceptions import HTTPException
from starlette.requests import Request

from app.common.auth import cookie, jwt_auth
from app.common.auth.authentication import JWTAuthorizationCredentials
from app.common.exception import APIException
from app.common.http import Http4XX


def allow_any(
    credentials: JWTAuthorizationCredentials = Depends(jwt_auth)
) -> JWTAuthorizationCredentials:
    return credentials


def is_authenticated(
    credentials: JWTAuthorizationCredentials = Depends(jwt_auth)
) -> JWTAuthorizationCredentials:
    if not credentials.is_authenticated:
        raise APIException(Http4XX.PERMISSION_DENIED)
    return credentials


def leader_only(
    credentials: JWTAuthorizationCredentials = Depends(jwt_auth)
) -> JWTAuthorizationCredentials:
    if credentials.permission.is_leader() or credentials.permission.is_admin():
        return credentials
    raise APIException(Http4XX.PERMISSION_DENIED)


def cookie_allow_any(
    credentials: JWTAuthorizationCredentials = Depends(cookie)
) -> JWTAuthorizationCredentials:
    return credentials


def cookie_authenticated(
    request: Request,
    credentials: JWTAuthorizationCredentials = Depends(cookie),
) -> JWTAuthorizationCredentials:
    if not credentials.is_authenticated:
        raise HTTPException(
            status_code=302,
            headers={"Location": f"/login?redirect={request.url.path}"},
        )
    return credentials
