from datetime import datetime
from typing import Iterable

from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.adapter.outbound.persistence.models import ScheduleModel
from app.adapter.outbound.persistence.reporitory.base import BaseRepository
from app.application.port.output import ScheduleRepositoryPort
from app.domain import Schedule


class SchedulePersistenceAdapter(BaseRepository, ScheduleRepositoryPort):
    async def save(self, schedule: Schedule) -> Schedule:
        model = await self._save(schedule, ScheduleModel)
        return model.to_domain()

    async def find_by_id_with_user(self, id_: int) -> Schedule | None:
        result = await self._session.execute(
            select(ScheduleModel)
            .options(selectinload(ScheduleModel.users))
            .where(ScheduleModel.id == id_)
            .order_by(ScheduleModel.day, ScheduleModel.start_time)
        )
        if schedule := result.scalar_one_or_none():
            return schedule.to_domain(user=True)

    async def find_active_schedules_with_user(
        self, band_id: int
    ) -> Iterable[Schedule]:
        result = await self._session.execute(
            select(ScheduleModel)
            .options(selectinload(ScheduleModel.users))
            .where(
                ScheduleModel.is_active.is_(True),
                ScheduleModel.band_id == band_id,
                ScheduleModel.day >= datetime.now().date(),
            )
            .order_by(ScheduleModel.day, ScheduleModel.start_time)
        )
        return map(lambda schedule: schedule.to_domain(user=True), result.scalars())
