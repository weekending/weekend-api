from abc import ABC, abstractmethod

from app.domain import PostComment


class PostCommentRepositoryPort(ABC):
    @abstractmethod
    async def find_by_post(self, post_id: int) -> list[PostComment]:
        raise NotImplementedError
