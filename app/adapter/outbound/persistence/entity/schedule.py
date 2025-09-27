from datetime import datetime

from sqlalchemy import (
    Boolean,
    Column,
    Date,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Table,
    Text,
    Time,
    UniqueConstraint,
    inspect,
)
from sqlalchemy.orm import Mapped, relationship

from app.domain import Schedule
from .base import Base
from .song import SongEntity
from .user import UserEntity


schedule_song_entity = Table(
    "t_schedule_song",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column(
        "schedule_id",
        Integer,
        ForeignKey("t_schedule.id", ondelete="CASCADE"),
        nullable=False,
    ),
    Column(
        "song_id",
        Integer,
        ForeignKey("t_song.id", ondelete="CASCADE"),
        nullable=False,
    ),
    Column(
        "created_dtm",
        DateTime,
        nullable=False,
        default=datetime.now,
        comment="생성 일시",
    ),
    UniqueConstraint("schedule_id", "song_id"),
)


schedule_user_entity = Table(
    "t_schedule_user",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column(
        "schedule_id",
        Integer,
        ForeignKey("t_schedule.id", ondelete="CASCADE"),
        nullable=False,
    ),
    Column(
        "user_id",
        Integer,
        ForeignKey("t_user.id", ondelete="CASCADE"),
        nullable=False,
    ),
    Column(
        "created_dtm",
        DateTime,
        nullable=False,
        default=datetime.now,
        comment="생성 일시",
    ),
    UniqueConstraint("schedule_id", "user_id"),
)


class ScheduleEntity(Base):
    __tablename__ = "t_schedule"
    __domain__ = Schedule

    id = Column(Integer, primary_key=True)
    band_id = Column(
        Integer, ForeignKey("t_band.id", ondelete="CASCADE"), nullable=False
    )
    title = Column(String(20), comment="제목", nullable=False)
    day = Column(Date, nullable=False, comment="일시")
    start_time = Column(Time, comment="시작 시간")
    end_time = Column(Time, comment="종료 시간")
    location = Column(String(30), comment="장소")
    memo = Column(Text, comment="메모")
    is_active = Column(Boolean, default=True, nullable=False, comment="활성화 여부")
    songs: Mapped[list[SongEntity]] = relationship(
        secondary=schedule_song_entity, order_by=schedule_song_entity.c.id.asc()
    )
    users: Mapped[list[UserEntity]] = relationship(secondary=schedule_user_entity)

    def to_domain(self) -> Schedule:
        insp = inspect(self)
        return Schedule(
            id=self.id,
            band_id=self.band_id,
            day=self.day,
            start_time=self.start_time,
            end_time=self.end_time,
            title=self.title,
            location=self.location,
            memo=self.memo,
            is_active=self.is_active,
            songs=(
                [s.to_domain() for s in self.songs]
                if "songs" not in insp.unloaded
                else []
            ),
            users=(
                [u.to_domain() for u in self.users]
                if "users" not in insp.unloaded
                else []
            ),
        )
