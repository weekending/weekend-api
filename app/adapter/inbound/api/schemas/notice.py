from datetime import datetime

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
    images: list[NoticeImageResponse] = []
    updated_dtm: datetime | None = None
    created_dtm: datetime

    @classmethod
    def from_domain(cls, notice: Notice) -> "NoticeResponse":
        return cls(
            id=notice.id,
            title=notice.title,
            content=notice.content,
            is_active=notice.is_active,
            images=[NoticeImageResponse.from_domain(img) for img in notice.images],
            updated_dtm=notice.updated_dtm,
            created_dtm=notice.created_dtm,
        )
