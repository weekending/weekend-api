from abc import ABC, abstractmethod
from datetime import date

from app.domain import Schedule


class ScheduleUseCase(ABC):
    @abstractmethod
    async def create_schedule(
        self, user_id: int, band_id: int, day: date, **kwargs
    ) -> Schedule:
        raise NotImplementedError

    @abstractmethod
    async def get_schedule_info(self, schedule_id: int) -> Schedule:
        raise NotImplementedError

    @abstractmethod
    async def get_band_schedules(self, user_id: int, band_id: int) -> list[Schedule]:
        raise NotImplementedError
