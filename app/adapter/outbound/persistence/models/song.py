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
from .base import BaseModel
from .user import UserModel


class SongModel(BaseModel):
    __tablename__ = "t_song"

    id = Column(Integer, primary_key=True)
    band_id = Column(
        Integer, ForeignKey("t_band.id", ondelete="CASCADE"), nullable=False
    )
    user_id = Column(Integer, ForeignKey("t_user.id", ondelete="CASCADE"))
    user = relationship(UserModel, lazy="joined")
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

    @staticmethod
    def from_domain(song: Song) -> "SongModel":
        return SongModel(
            id=song.id,
            band_id=song.band_id,
            user_id=song.user_id,
            status=song.status,
            title=song.title,
            singer=song.singer,
            thumbnail=song.thumbnail,
            is_active=song.is_active,
            created_dtm=song.created_dtm,
            in_progress_dtm=song.in_progress_dtm,
            closed_dtm=song.closed_dtm,
        )

    def to_domain(self) -> Song:
        return Song(
            id=self.id,
            band_id=self.band_id,
            user_id=self.user_id,
            status=self.status,
            title=self.title,
            singer=self.singer,
            thumbnail=self.thumbnail,
            is_active=self.is_active,
            created_dtm=self.created_dtm,
            in_progress_dtm=self.in_progress_dtm,
            closed_dtm=self.closed_dtm,
        )
