from datetime import datetime

from pydantic import BaseModel

from app.domain import Notice


class NoticeResponse(BaseModel):
    id: int
    title: str
    content: str
    is_active: bool
    updated_dtm: datetime | None = None
    created_dtm: datetime

    @classmethod
    def from_domain(cls, notice: Notice) -> "NoticeResponse":
        return cls(
            id=notice.id,
            title=notice.title,
            content=notice.content,
            is_active=notice.is_active,
            updated_dtm=notice.updated_dtm,
            created_dtm=notice.created_dtm,
        )
