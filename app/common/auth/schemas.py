from pydantic import BaseModel


class JWTAuthorizationCredentials(BaseModel):
    user_id: int
    email: str
    exp: float
    iat: float
