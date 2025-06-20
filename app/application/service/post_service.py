from datetime import datetime

from fastapi import Depends
from zoneinfo import ZoneInfo

from app.adapter.outbound.persistence import (
    PostPersistenceAdapter,
    PostCategoryPersistenceAdapter,
)
from app.common.exception import APIException
from app.common.http import Http4XX
from app.core.settings import Settings, get_settings
from app.domain import Post, PostCategory
from ..port.input import PostUseCase
from ..port.output import PostCategoryRepositoryPort, PostRepositoryPort


class PostService(PostUseCase):
    def __init__(
        self,
        category_repo: PostCategoryRepositoryPort = Depends(
            PostCategoryPersistenceAdapter
        ),
        post_repo: PostRepositoryPort = Depends(PostPersistenceAdapter),
        settings: Settings = Depends(get_settings),
    ):
        self._category_repo = category_repo
        self._post_repo = post_repo
        self._tz = ZoneInfo(settings.TIMEZONE)

    async def get_post_list(
        self, size: int, page: int, category_id: int
    ) -> list[Post]:
        return await self._post_repo.find_by_category(
            limit=size, offset=size * (page - 1), category_id=category_id
        )

    async def _get_category(self, category_id: int) -> PostCategory:
        category = await self._category_repo.find_by_id_or_none(category_id)
        if not category:
            raise APIException(Http4XX.CATEGORY_NOT_FOUND)
        return category

    async def create_post(
        self,
        category_id: int,
        user_id: int,
        title: str,
        content: str,
    ) -> Post:
        category = await self._get_category(category_id)
        if not category.allow_anonymous and user_id <= 0:
            raise APIException(Http4XX.PERMISSION_DENIED)
        post = await self._post_repo.save(
            Post(
                category_id=category.id,
                user_id=user_id if user_id > 0 else None,
                title=title,
                content=content,
                is_active=True,
                created_dtm=datetime.now(),
            )
        )
        post.category = category
        return post

    async def get_post_info(self, post_id: int) -> Post:
        if not (post := await self._post_repo.find_by_id_or_none(post_id)):
            raise APIException(Http4XX.POST_NOT_FOUND)
        elif not post.is_active:
            raise APIException(Http4XX.INACTIVE_POST)
        return post

    async def update_post(
        self,
        post_id: int,
        user_id: int,
        title: str,
        content: str,
    ) -> Post:
        if not (post := await self._post_repo.find_by_id_or_none(post_id)):
            raise APIException(Http4XX.POST_NOT_FOUND)
        elif post.user_id is None:
            raise APIException(Http4XX.PERMISSION_DENIED)
        elif post.user_id != user_id:
            raise APIException(Http4XX.PERMISSION_DENIED)
        post.title = title
        post.content = content
        post.updated_dtm = datetime.now(tz=self._tz)
        return await self._post_repo.save(post)

    async def get_post_count(self, category_id: int) -> int:
        return await self._post_repo.count_by_category(category_id)

