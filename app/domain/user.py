from pydantic import BaseModel


class User(BaseModel):
    id: int = None
    name: str
    email: str
    password: str
    is_active: bool
    is_admin: bool
