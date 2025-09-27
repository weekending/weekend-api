from datetime import date
from typing import Iterable

from sqlalchemy import Sequence, select, insert
from sqlalchemy.orm import selectinload, with_loader_criteria

from app.adapter.outbound.persistence.entity import (
    ScheduleEntity,
    SongEntity,
    schedule_user_entity,
)
from app.adapter.outbound.persistence.reporitory.base import BaseRepository
from app.application.port.output import ScheduleRepositoryPort
from app.domain import Schedule


class SchedulePersistenceAdapter(BaseRepository, ScheduleRepositoryPort):
    async def save(self, schedule: Schedule) -> Schedule:
        model = await self._save(schedule, ScheduleEntity)
        return model.to_domain()

    async def find_by_id_with_song_and_user(self, id_: int) -> Schedule | None:
        result = await self._session.execute(
            select(ScheduleEntity)
            .options(
                selectinload(ScheduleEntity.songs),
                with_loader_criteria(SongEntity, SongEntity.is_active == True)
            )
            .options(selectinload(ScheduleEntity.users))
            .where(ScheduleEntity.id == id_)
        )
        if not (schedule := result.scalar_one_or_none()):
            return None
        return schedule.to_domain()

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
        return map(lambda schedule: schedule.to_domain(), result.scalars())

    async def find_schedule_user_exists(
        self, schedule_id: int, user_id: int
    ) -> Sequence:
        result = await self._session.execute(
            select(schedule_user_entity).where(
                schedule_user_entity.c.schedule_id == schedule_id,
                schedule_user_entity.c.user_id == user_id,
            )
        )
        return result.scalars().all()

    async def insert_schedule_user(self, schedule_id: int, user_id: int):
        await self._session.execute(
            insert(schedule_user_entity).values(
                schedule_id=schedule_id, user_id=user_id
            )
        )
        await self._session.commit()
