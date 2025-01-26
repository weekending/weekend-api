from datetime import datetime
from typing import Sequence

from sqlalchemy import (
    Boolean,
    Column,
    Date,
    ForeignKey,
    Integer,
    String,
    Table,
    Text,
    Time,
    select,
)
from sqlalchemy.orm import Mapped, relationship, selectinload

from app.core.database import execute_query
from .base import BaseModel
from .user import User


schedule_user = Table(
    "t_schedule_user",
    BaseModel.metadata,
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
)


class Schedule(BaseModel):
    __tablename__ = "t_schedule"

    id = Column(Integer, primary_key=True)
    band_id = Column(
        Integer, ForeignKey("t_band.id", ondelete="CASCADE"), nullable=False
    )
    date = Column(Date, nullable=False, comment="일시")
    start_time = Column(Time, comment="시작 시간")
    end_time = Column(Time, comment="종료 시간")
    title = Column(String(20), comment="제목")
    location = Column(String(30), comment="장소")
    memo = Column(Text, comment="메모")
    is_active = Column(Boolean, default=True, nullable=False, comment="활성화 여부")
    users: Mapped[list[User]] = relationship(secondary=schedule_user)

    @classmethod
    async def find_active_schedules(cls, band_id: int) -> Sequence["Schedule"]:
        result = await execute_query(
            select(cls)
            .options(selectinload(cls.users))
            .where(
                cls.is_active.is_(True),
                cls.band_id == band_id,
                cls.date >= datetime.now().date(),
            )
            .order_by(cls.date, cls.start_time)
        )
        return result.scalars().all()
