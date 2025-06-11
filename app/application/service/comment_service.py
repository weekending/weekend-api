from collections import defaultdict

from fastapi import Depends

from app.adapter.inbound.api.schemas.comment import CommentResponse
from app.adapter.outbound.persistence import PostCommentPersistenceAdapter
from app.domain import PostComment
from ..port.input import PostCommentUseCase
from ..port.output import PostCommentRepositoryPort


class PostCommentService(PostCommentUseCase):
    def __init__(
        self,
        comment_repo: PostCommentRepositoryPort = Depends(
            PostCommentPersistenceAdapter,
        ),
    ):
        self._comment_repo = comment_repo

    async def get_post_comments(self, post_id: int) -> list[PostComment]:
        return await self._comment_repo.find_by_post(post_id)
