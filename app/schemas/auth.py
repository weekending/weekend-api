from pydantic import BaseModel


class SignupInfo(BaseModel):
    name: str
    username: str
    password: str
    password_check: str
    band_id: int | None = None


class LoginInfo(BaseModel):
    username: str
    password: str
