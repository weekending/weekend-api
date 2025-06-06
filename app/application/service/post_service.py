from fastapi import Depends

from app.adapter.outbound.persistence import PostPersistenceAdapter
from app.common.exception import APIException
from app.common.http import Http4XX
from app.domain import Post
from ..port.input import PostUseCase
from ..port.output import PostRepositoryPort


class PostService(PostUseCase):
    def __init__(
        self,
        post_repo: PostRepositoryPort = Depends(PostPersistenceAdapter),
    ):
        self._post_repo = post_repo

    async def get_post_list(
        self, size: int, page: int, category_id: int
    ) -> list[Post]:
        return await self._post_repo.find_by_category(
            limit=size, offset=size * (page - 1), category_id=category_id
        )

    async def create_post(
        self,
        title: str,
        content: str,
        user_id: int,
        category_id: int,
    ) -> Post:
        return await self._post_repo.save(
            Post(
                category_id=category_id,
                user_id=user_id if user_id > 0 else None,
                title=title,
                content=content,
                is_active=True,
            )
        )

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
        post.title = title
        post.content = content
        return await self._post_repo.save(post)
