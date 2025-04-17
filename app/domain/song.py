from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class SongStatus(Enum):
    PENDING = "PENDING"  # 대기
    INPROGRESS = "INPROGRESS"  # 진행중
    CLOSED = "CLOSED"  # 종료

    def __str__(self):
        return self.value


class Song(BaseModel):
    id: int = None
    band_id: int
    user_id: int | None
    title: str
    singer: str
    thumbnail: str | None
    status: SongStatus
    is_active: bool
    created_dtm: datetime
    in_progress_dtm: datetime | None
    closed_dtm: datetime | None
