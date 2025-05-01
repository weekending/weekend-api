from datetime import date

from fastapi import Depends

from app.adapter.outbound.persistence import (
    SchedulePersistenceAdapter,
    UserBandPersistenceAdapter,
)
from app.common.exception import APIException
from app.common.http import Http4XX
from app.common.utils import check_user_leader_permission
from app.domain import Schedule
from ..port.input import ScheduleUseCase
from ..port.output import ScheduleRepositoryPort, UserBandRepositoryPort


class ScheduleService(ScheduleUseCase):
    def __init__(
        self,
        schedule_repo: ScheduleRepositoryPort = Depends(SchedulePersistenceAdapter),
        user_band_repo: UserBandRepositoryPort = Depends(UserBandPersistenceAdapter),
    ):
        self._schedule_repo = schedule_repo
        self._user_band_repo = user_band_repo

    async def create_schedule(
        self, user_id: int, band_id: int, title: str, day: date, **kwargs
    ) -> Schedule:
        check_user_leader_permission(
            user_band=await self._user_band_repo.find_by_user_and_band(
                user_id, band_id
            )
        )
        return await self._schedule_repo.save(
            Schedule(
                band_id=band_id,
                title=title,
                day=day,
                is_active=True,
                users=[],
                **kwargs,
            )
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

    async def update_schedule_info(
        self, schedule_id: int, user_id: int, **kwargs
    ) -> Schedule:
        if not (schedule := await self._schedule_repo.find_by_id_with_user(schedule_id)):
            raise APIException(Http4XX.SCHEDULE_NOT_FOUND)

        check_user_leader_permission(
            user_band=await self._user_band_repo.find_by_user_and_band(
                user_id, schedule.band_id
            )
        )
        for field, value in kwargs.items():
            if value is not None:
                setattr(schedule, field, value)
        return await self._schedule_repo.save(schedule)
