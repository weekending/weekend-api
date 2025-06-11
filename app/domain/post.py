from datetime import datetime

from pydantic import BaseModel

from .user import User


class PostCategory(BaseModel):
    id: int
    name: str
    code: str
    allow_anonymous: bool
    is_active: bool
    sequence: int


class Post(BaseModel):
    id: int = None
    category_id: int
    user_id: int | None = None
    title: str
    content: str
    is_active: bool
    comment_count: int = 0
    updated_dtm: datetime | None = None
    created_dtm: datetime
    category: PostCategory | None = None
    user: User | None = None


class PostComment(BaseModel):
    id: int = None
    user_id: int | None = None
    post_id: int
    parent_id: int | None = None
    level: int
    content: str
    is_active: bool
    updated_dtm: datetime | None = None
    created_dtm: datetime
    user: User | None = None
