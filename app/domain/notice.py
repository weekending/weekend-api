from datetime import datetime
import enum

from pydantic import BaseModel


class NoticeImageType(enum.Enum):
    IMAGE = "image"
    BUTTON = "button"


class NoticeImage(BaseModel):
    id: int | None = None
    notice_id: int | None = None
    type: NoticeImageType
    image_url: str
    link: str | None = None
    sequence: int = 0
    is_active: bool = True
    updated_dtm: datetime | None = None
    created_dtm: datetime | None = None


class Notice(BaseModel):
    id: int | None = None
    title: str
    content: str
    is_active: bool
    images: list[NoticeImage] = []
    updated_dtm: datetime | None = None
    created_dtm: datetime | None = None
  