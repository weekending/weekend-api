from fastapi import Depends

from app.common.auth import jwt_auth
from app.common.auth.authentication import JWTAuthorizationCredentials
from app.common.exception import APIException
from app.common.http import Http4XX


# def is_authenticated(
#     credentials: JWTAuthorizationCredentials = Depends(jwt_auth)
# ) -> JWTAuthorizationCredentials:
#     return credentials

def is_authenticated() -> JWTAuthorizationCredentials:
    return JWTAuthorizationCredentials(
        user_id=1, email="test@test.com", exp=-1, iat=-1
    )


def leader_only(
    credentials: JWTAuthorizationCredentials = Depends(jwt_auth)
) -> JWTAuthorizationCredentials:
    if credentials.permission.is_leader() or credentials.permission.is_admin():
        return credentials
    raise APIException(Http4XX.PERMISSION_DENIED)
