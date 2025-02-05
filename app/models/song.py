from datetime import datetime
import enum

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import relationship

from .base import BaseModel
from .user import User


class SongStatus(enum.Enum):
    PENDING = "PENDING"  # 대기
    INPROGRESS = "INPROGRESS"  # 진행중
    CLOSED = "CLOSED"  # 종료


class Song(BaseModel):
    __tablename__ = "t_song"

    id = Column(Integer, primary_key=True)
    band_id = Column(
        Integer, ForeignKey("t_band.id", ondelete="CASCADE"), nullable=False
    )
    user_id = Column(Integer, ForeignKey("t_user.id", ondelete="CASCADE"))
    user = relationship(User, lazy="joined")
    status = Column(
        Enum(SongStatus, native_enum=False),
        default=SongStatus.PENDING,
        nullable=False,
        comment="사용자 권한",
    )
    title = Column(String(100), nullable=False, comment="타이틀")
    singer = Column(String(50), nullable=False, comment="가수")
    thumbnail = Column(Text, comment="썸네일 이미지")
    is_active = Column(Boolean, default=True, nullable=False, comment="활성화 여부")
    in_progress_dtm = Column(DateTime, comment="진행 시작 일시")
    closed_dtm = Column(DateTime, comment="종료 일시")

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "singer": self.singer,
            "status": self.status.value,
            "created_dtm": self.created_dtm.strftime("%Y.%m.%d"),
            "in_progress_dtm": (
                self.in_progress_dtm.strftime("%Y.%m.%d")
                if self.in_progress_dtm else None
            ),
            "closed_dtm": (
                self.closed_dtm.strftime("%Y.%m.%d")
                if self.closed_dtm else None
            ),
        }
