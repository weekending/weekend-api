from abc import ABC, abstractmethod

from app.domain import Notice


class NoticeUseCase(ABC):
    @abstractmethod
    async def get_notice_list(self, size: int, page: int) -> list[Notice]:
        raise NotImplementedError

    @abstractmethod
    async def get_notice_info(self, notice_id: int) -> Notice:
        raise NotImplementedError
