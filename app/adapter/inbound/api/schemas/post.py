from datetime import datetime

from pydantic import BaseModel
from zoneinfo import ZoneInfo

from app.core.settings import get_settings
from app.domain import Post, PostCategory
from .user import UserInfoResponse


settings = get_settings()
kst = ZoneInfo(settings.TIMEZONE)


class PostCreateInfo(BaseModel):
    title: str
    content: str
    category_id: int


class PostUpdateInfo(BaseModel):
    title: str
    content: str


class PostCategoryResponse(BaseModel):
    id: int
    name: str
    allow_anonymous: bool

    @classmethod
    def from_domain(cls, category: PostCategory) -> "PostCategoryResponse":
        return PostCategoryResponse(
            id=category.id,
            name=category.name,
            allow_anonymous=category.allow_anonymous,
        )


class PostListResponse(BaseModel):
    id: int
    title: str
    comment_count: int
    is_new: bool
    category: PostCategoryResponse
    user: UserInfoResponse | None
    updated_dtm: datetime | None = None
    created_dtm: datetime

    @classmethod
    def from_domain(cls, post: Post) -> "PostListResponse":
        return cls(
            id=post.id,
            title=post.title,
            comment_count=post.comment_count,
            is_new=(datetime.now(kst) - post.created_dtm).days < 1,
            category=PostCategoryResponse.from_domain(post.category),
            user=UserInfoResponse.from_domain(post.user) if post.user else None,
            updated_dtm=post.updated_dtm,
            created_dtm=post.created_dtm,
        )


class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    is_active: bool
    category: PostCategoryResponse
    user: UserInfoResponse | None
    updated_dtm: datetime | None = None
    created_dtm: datetime

    @classmethod
    def from_domain(cls, post: Post) -> "PostResponse":
        return cls(
            id=post.id,
            title=post.title,
            content=post.content,
            is_active=post.is_active,
            category=PostCategoryResponse.from_domain(post.category),
            user=UserInfoResponse.from_domain(post.user) if post.user else None,
            updated_dtm=post.updated_dtm,
            created_dtm=post.created_dtm,
        )
