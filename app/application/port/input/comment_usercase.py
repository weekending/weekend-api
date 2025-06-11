from abc import ABC, abstractmethod

from app.domain import PostComment


class PostCommentUseCase(ABC):
    @abstractmethod
    async def get_post_comments(self, post_id: int) -> list[PostComment]:
        raise NotImplementedError
