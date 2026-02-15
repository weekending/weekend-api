from datetime import datetime, timedelta, timezone

from pydantic import BaseModel

from app.domain import Notice, NoticeImage


class NoticeImageResponse(BaseModel):
    id: int
    type: str
    image_url: str
    link: str | None = None
    sequence: int

    @classmethod
    def from_domain(cls, image: NoticeImage) -> "NoticeImageResponse":
        return cls.model_construct(
            id=image.id,
            type=image.type,
            image_url=image.image_url,
            link=image.link,
            sequence=image.sequence,
        )


class NoticeResponse(BaseModel):
    id: int
    title: str
    content: str
    is_active: bool
    is_new: bool = False
    images: list[NoticeImageResponse] = []
    updated_dtm: datetime | None = None
    created_dtm: datetime

    @classmethod
    def from_domain(cls, notice: Notice) -> "NoticeResponse":
        is_new = (datetime.now(timezone.utc) - notice.created_dtm.replace(tzinfo=timezone.utc)) <= timedelta(days=30)
        return cls(
            id=notice.id,
            title=notice.title,
            content=notice.content,
            is_active=notice.is_active,
            is_new=is_new,
            images=[NoticeImageResponse.from_domain(img) for img in notice.images],
            updated_dtm=notice.updated_dtm,
            created_dtm=notice.created_dtm,
        )
