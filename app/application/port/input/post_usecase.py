from abc import ABC, abstractmethod

from app.domain import Post


class PostUseCase(ABC):
    @abstractmethod
    async def get_post_list(
        self, size: int, page: int, category_id: int
    ) -> list[Post]:
        raise NotImplementedError

    @abstractmethod
    async def create_post(
        self,
        title: str,
        content: str,
        user_id: int,
        category_id: int,
    ) -> Post:
        raise NotImplementedError

    @abstractmethod
    async def get_post_info(self, post_id: int) -> Post:
        raise NotImplementedError

    @abstractmethod
    async def update_post(
        self,
        post_id: int,
        user_id: int,
        title: str,
        content: str,
    ) -> Post:
        raise NotImplementedError
