from abc import ABC, abstractmethod

from app.domain import Post


class PostRepositoryPort(ABC):
    @abstractmethod
    async def save(self, post: Post) -> Post:
        raise NotImplementedError

    @abstractmethod
    async def find_by_id_or_none(self, id_: int) -> Post | None:
        raise NotImplementedError

    @abstractmethod
    async def find_by_category(
        self, limit: int, offset: int, category_id: int
    ) -> list[Post]:
        raise NotImplementedError

