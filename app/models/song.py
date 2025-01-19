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
    group_id = Column(
        Integer, ForeignKey("t_group.id", ondelete="CASCADE"), nullable=False
    )
    user_id = Column(Integer, ForeignKey("t_user.id", ondelete="CASCADE"))
    user = relationship(User, lazy="joined")
    status = Column(
        Enum(SongStatus, native_enum=False),
        comment="사용자 권한",
        nullable=False,
        default=SongStatus.PENDING,
    )
    title = Column(String(100), comment="타이틀", nullable=False)
    singer = Column(String(50), comment="가수", nullable=False)
    thumbnail = Column(Text, comment="썸네일 이미지")
    is_active = Column(Boolean, comment="활성화 여부", nullable=False, default=True)
    in_progress_dtm = Column(DateTime, comment="진행 시작 일시")
    closed_dtm = Column(DateTime, comment="종료 일시")

    def to_dict(self) -> dict:
        now = datetime.now()
        return {
            "title": self.title,
            "singer": self.singer,
            "status": self.status.value,
            "created_dtm": self.created_dtm.strftime('%Y.%m.%d'),
            "in_progress_dtm": (
                self.in_progress_dtm.strftime('%Y.%m.%d')
                if self.in_progress_dtm else None
            ),
            "closed_dtm": (
                self.closed_dtm.strftime('%Y.%m.%d')
                if self.closed_dtm else None
            ),
            "from_in_progress":  (
                (now - self.in_progress_dtm).days
                if self.in_progress_dtm else None
            ),
            "from_created":  (now - self.created_dtm).days
        }
