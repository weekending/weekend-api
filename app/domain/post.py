from pydantic import BaseModel


class PostCategory(BaseModel):
    id: int
    name: str
    code: str
    allow_anonymous: bool
    is_active: bool


class Post(BaseModel):
    id: int = None
    category_id: int
    user_id: int | None = None
    title: str
    content: str
    is_active: bool
