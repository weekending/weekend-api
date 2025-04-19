from datetime import date, datetime
from typing import Iterable

from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.adapter.outbound.persistence.entity import ScheduleEntity
from app.adapter.outbound.persistence.reporitory.base import BaseRepository
from app.application.port.output import ScheduleRepositoryPort
from app.domain import Schedule


class SchedulePersistenceAdapter(BaseRepository, ScheduleRepositoryPort):
    async def save(self, schedule: Schedule) -> Schedule:
        model = await self._save(schedule, ScheduleEntity)
        return model.to_domain()

    async def find_by_id_with_user(self, id_: int) -> Schedule | None:
        result = await self._session.execute(
            select(ScheduleEntity)
            .options(selectinload(ScheduleEntity.users))
            .where(ScheduleEntity.id == id_)
            .order_by(ScheduleEntity.day, ScheduleEntity.start_time)
        )
        if schedule := result.scalar_one_or_none():
            return schedule.to_domain(user=True)

    async def find_active_schedules_with_user(
        self, band_id: int, from_: date, to: date
    ) -> Iterable[Schedule]:
        query = (
            select(ScheduleEntity)
            .options(selectinload(ScheduleEntity.users))
            .where(
                ScheduleEntity.is_active.is_(True),
                ScheduleEntity.band_id == band_id,
            )
        )
        if from_:
            query = query.where(ScheduleEntity.day >= from_)
        if to:
            query = query.where(ScheduleEntity.day <= to)
        result = await self._session.execute(
            query.order_by(ScheduleEntity.day, ScheduleEntity.start_time)
        )
        return map(lambda schedule: schedule.to_domain(user=True), result.scalars())
