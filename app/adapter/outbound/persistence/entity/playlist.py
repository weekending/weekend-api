from datetime import datetime

from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
    Table,
    Text,
    DateTime,
    UniqueConstraint,
    inspect,
)
from sqlalchemy.orm import Mapped, relationship

from app.domain.playlist import Playlist
from .base import Base
from .song import SongEntity


playlist_song_entity = Table(
    "t_playlist_song",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column(
        "playlist_id",
        Integer,
        ForeignKey("t_playlist.id", ondelete="CASCADE"),
        nullable=False,
    ),
    Column(
        "song_id",
        Integer,
        ForeignKey("t_song.id", ondelete="CASCADE"),
        nullable=False,
    ),
    Column("sequence", Integer, nullable=False, default=0, comment="정렬 순서"),
    Column(
        "created_dtm",
        DateTime,
        nullable=False,
        default=datetime.now,
        comment="생성 일시",
    ),
    UniqueConstraint("playlist_id", "song_id"),
)


class PlaylistEntity(Base):
    __tablename__ = "t_playlist"
    __domain__ = Playlist

    id = Column(Integer, primary_key=True)
    band_id = Column(
        Integer, ForeignKey("t_band.id", ondelete="CASCADE"), nullable=False
    )
    title = Column(String(100), nullable=False, comment="제목")
    description = Column(Text, comment="설명")
    thumbnail = Column(Text, comment="썸네일 이미지")
    is_active = Column(Boolean, default=True, nullable=False, comment="활성화 여부")
    songs: Mapped[list[SongEntity]] = relationship(
        secondary=playlist_song_entity,
        order_by=playlist_song_entity.c.sequence.asc(),
    )

    def to_domain(self) -> Playlist:
        insp = inspect(self)
        return Playlist(
            id=self.id,
            band_id=self.band_id,
            title=self.title,
            description=self.description,
            thumbnail=self.thumbnail,
            is_active=self.is_active,
            songs=(
                [s.to_domain() for s in self.songs]
                if "songs" not in insp.unloaded
                else []
            ),
            created_dtm=self.created_dtm,
            updated_dtm=self.updated_dtm,
        )
