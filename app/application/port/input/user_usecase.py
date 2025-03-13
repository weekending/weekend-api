from abc import ABC, abstractmethod
from typing import Iterable

from app.domain import Band, User


class UserUseCase(ABC):
    @abstractmethod
    async def get_user_info(self, user_id: int) -> User:
        raise NotImplementedError

    @abstractmethod
    async def get_user_bands(self, user_id: int) -> Iterable[Band]:
        raise NotImplementedError
