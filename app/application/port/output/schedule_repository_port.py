from abc import ABC, abstractmethod
from datetime import date

from app.domain import Schedule


class ScheduleRepositoryPort(ABC):
    @abstractmethod
    async def save(self, schedule: Schedule) -> Schedule:
        raise NotImplementedError

    @abstractmethod
    async def find_by_id_with_user(self, id_: int) -> Schedule | None:
        raise NotImplementedError

    @abstractmethod
    async def find_active_schedules_with_user(
        self, band_id: int, from_: date, to: date
    ) -> list[Schedule]:
        raise NotImplementedError
