from datetime import datetime

from pydantic import BaseModel

from app.domain import PostComment
from .user import UserInfoResponse


class CommentResponse(BaseModel):
    id: int
    level: int
    content: str
    is_active: bool
    user: UserInfoResponse | None
    created_dtm: datetime

    @classmethod
    def from_domain(cls, comment: PostComment) -> "CategoryResponse":
        return cls(
            id=comment.id,
            level=comment.level,
            content=comment.content,
            is_active=comment.is_active,
            user=(
                UserInfoResponse.from_domain(comment.user)
                if comment.user
                else None
            ),
            created_dtm=comment.created_dtm,
        )
