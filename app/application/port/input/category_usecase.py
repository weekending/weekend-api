from abc import ABC, abstractmethod

from app.domain import PostCategory


class PostCategoryUseCase(ABC):
    @abstractmethod
    async def get_categories(self) -> list[PostCategory]:
        raise NotImplementedError
