from abc import ABC, abstractmethod

from app.domain import PostCategory


class PostCategoryRepositoryPort(ABC):
    @abstractmethod
    async def find_by_id_or_none(self, id_: int) -> PostCategory | None:
        raise NotImplementedError

    @abstractmethod
    async def find_active_list(self) -> list[PostCategory]:
        raise NotImplementedError

