from abc import ABC, abstractmethod
from datetime import date

from app.domain import Schedule


class ScheduleUseCase(ABC):
    @abstractmethod
    async def create_schedule(
        self, user_id: int, band_id: int, title: str, day: date, **kwargs
    ) -> Schedule:
        raise NotImplementedError

    @abstractmethod
    async def get_schedule_info(self, schedule_id: int) -> Schedule:
        raise NotImplementedError

    @abstractmethod
    async def get_band_schedules(
        self,
        user_id: int,
        band_id: int,
        from_: date,
        to: date,
    ) -> list[Schedule]:
        raise NotImplementedError

    @abstractmethod
    async def update_schedule_info(
        self, schedule_id: int, user_id: int, **kwargs
    ) -> Schedule:
        raise NotImplementedError

    @abstractmethod
    async def attend_schedule(self, schedule_id: int, user_id: int) -> bool:
        raise NotImplementedError
