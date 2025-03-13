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
)
from sqlalchemy.orm import Mapped, relationship

from app.domain import Schedule
from .base import Model
from .user import UserModel


schedule_user_model = Table(
    "t_schedule_user",
    Model.metadata,
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


class ScheduleModel(Model):
    __tablename__ = "t_schedule"

    id = Column(Integer, primary_key=True)
    band_id = Column(
        Integer, ForeignKey("t_band.id", ondelete="CASCADE"), nullable=False
    )
    day = Column(Date, nullable=False, comment="일시")
    start_time = Column(Time, comment="시작 시간")
    end_time = Column(Time, comment="종료 시간")
    title = Column(String(20), comment="제목")
    location = Column(String(30), comment="장소")
    memo = Column(Text, comment="메모")
    is_active = Column(Boolean, default=True, nullable=False, comment="활성화 여부")
    users: Mapped[list[UserModel]] = relationship(secondary=schedule_user_model)

    @staticmethod
    def from_domain(schedule: Schedule) -> "ScheduleModel":
        return ScheduleModel(
            id=schedule.id,
            band_id=schedule.band_id,
            day=schedule.day,
            start_time=schedule.start_time,
            end_time=schedule.end_time,
            title=schedule.title,
            location=schedule.location,
            memo=schedule.memo,
            is_active=schedule.is_active,
        )

    def to_domain(self, user: bool = False) -> Schedule:
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
            users=[u.to_domain() for u in self.users] if user else [],
        )
