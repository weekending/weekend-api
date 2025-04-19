from datetime import date

from fastapi import Depends

from app.adapter.outbound.persistence import SchedulePersistenceAdapter
from app.common.exception import APIException
from app.common.http import Http4XX
from app.domain import Schedule
from ..port.input import ScheduleUseCase
from ..port.output import ScheduleRepositoryPort


class ScheduleService(ScheduleUseCase):
    def __init__(
        self,
        schedule_repo: ScheduleRepositoryPort = Depends(SchedulePersistenceAdapter),
    ):
        self._schedule_repo = schedule_repo

    async def create_schedule(
        self, user_id: int, band_id: int, day: date, **kwargs
    ) -> Schedule:
        return await self._schedule_repo.save(
            Schedule(band_id=band_id, day=day, is_active=True, users=[], **kwargs)
        )

    async def get_schedule_info(self, schedule_id: int) -> Schedule:
        if not (schedule := await self._schedule_repo.find_by_id_with_user(schedule_id)):
            raise APIException(Http4XX.SCHEDULE_NOT_FOUND)
        return schedule

    async def get_band_schedules(
        self,
        user_id: int,
        band_id: int,
        from_: date,
        to: date,
    ) -> list[Schedule]:
        return await self._schedule_repo.find_active_schedules_with_user(
            band_id, from_, to
        )
