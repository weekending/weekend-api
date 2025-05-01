from abc import ABC, abstractmethod
from typing import Iterable

from app.domain import Band, UserBand


class UserBandRepositoryPort(ABC):
    @abstractmethod
    async def save(self, user: UserBand):
        raise NotImplementedError

    @abstractmethod
    async def find_by_user_and_band(self, user_id: int, band_id: int) -> UserBand | None:
        raise NotImplementedError

    @abstractmethod
    async def find_user_bands(self, user_id: int) -> Iterable[Band]:
        raise NotImplementedError

    @abstractmethod
    async def find_band_users(self, band_id: int) -> list[UserBand]:
        raise NotImplementedError
