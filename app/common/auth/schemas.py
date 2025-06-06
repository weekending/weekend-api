from pydantic import BaseModel


class JWTAuthorizationCredentials(BaseModel):
    is_authenticated: bool
    user_id: int | None
    email: str | None
    exp: float
    iat: float
