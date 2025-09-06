from abc import ABC, abstractmethod

from app.domain import Notice


class NoticeRepositoryPort(ABC):
    @abstractmethod
    async def find_by_id_or_none(self, id_: int) -> Notice | None:
        raise NotImplementedError

    @abstractmethod
    async def find_all(self, limit: int, offset: int) -> list[Notice]:
        raise NotImplementedError
