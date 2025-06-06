from pydantic import BaseModel, Field

from app.domain import Post


class PostCreateInfo(BaseModel):
    title: str
    content: str
    category_id: int


class PostUpdateInfo(BaseModel):
    title: str
    content: str


class PostResponse(BaseModel):
    id: int = Field(title="일정 PK")
    title: str
    content: str
    user_id: int | None
    category_id: int
    is_active: bool

    @staticmethod
    def from_domain(post: Post) -> "PostResponse":
        return PostResponse(
            id=post.id,
            title=post.title,
            content=post.content,
            user_id=post.user_id,
            category_id=post.category_id,
            is_active=post.is_active,
        )
