from fastapi import Depends

from app.adapter.outbound.persistence import PostCategoryPersistenceAdapter
from app.domain import PostCategory
from ..port.input import PostCategoryUseCase
from ..port.output import PostCategoryRepositoryPort


class PostCategoryService(PostCategoryUseCase):
    def __init__(
        self,
        category_repo: PostCategoryRepositoryPort = Depends(
            PostCategoryPersistenceAdapter
        ),
    ):
        self._category_repo = category_repo

    async def get_active_categories(self) -> list[PostCategory]:
        return await self._category_repo.find_active_list()
