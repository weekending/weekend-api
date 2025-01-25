from pydantic import BaseModel

from app.models import PermissionType


class JWTAuthorizationCredentials(BaseModel):
    user_id: int
    username: str
    permission: PermissionType
    exp: float
    iat: float
