from pydantic import BaseModel, Field

from app.domain import PostCategory


class CategoryResponse(BaseModel):
    id: int = Field(title="일정 PK")
    name: str
    code: str
    allow_anonymous: bool
    is_active: bool

    @staticmethod
    def from_domain(category: PostCategory) -> "CategoryResponse":
        return CategoryResponse(
            id=category.id,
            name=category.name,
            code=category.code,
            allow_anonymous=category.allow_anonymous,
            is_active=category.is_active,
        )
