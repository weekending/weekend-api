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

from app.domain import Song, SongStatus
from .base import Base
from .user import UserEntity


class SongEntity(Base):
    __tablename__ = "t_song"
    __domain__ = Song

    id = Column(Integer, primary_key=True)
    band_id = Column(
        Integer, ForeignKey("t_band.id", ondelete="CASCADE"), nullable=False
    )
    user_id = Column(Integer, ForeignKey("t_user.id", ondelete="CASCADE"))
    user = relationship(UserEntity, lazy="joined")
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
