from fastapi import Depends
from starlette.exceptions import HTTPException

from app.common.auth import jwt_auth
from app.common.auth.authentication import JWTAuthorizationCredentials


def is_authenticated(
    credentials: JWTAuthorizationCredentials = Depends(jwt_auth)
) -> JWTAuthorizationCredentials:
    return credentials


def leader_only(
    credentials: JWTAuthorizationCredentials = Depends(jwt_auth)
) -> JWTAuthorizationCredentials:
    if credentials.permission.is_leader() or credentials.permission.is_admin():
        return credentials
    raise HTTPException(status_code=403, detail="권한이 없습니다.")
