from sqlalchemy import func, select

from app.adapter.outbound.persistence.entity import PostEntity, PostCommentEntity
from app.adapter.outbound.persistence.reporitory.base import BaseRepository
from app.application.port.output import PostRepositoryPort
from app.domain import Post


class PostPersistenceAdapter(BaseRepository, PostRepositoryPort):
    async def save(self, post: Post) -> Post:
        model = await self._save(post, PostEntity)
        return model.to_domain()

    async def find_by_id_or_none(self, id_: int) -> Post | None:
        if not (model := await self._find_by_id_or_none(id_, PostEntity)):
            return None
        return model.to_domain()

    async def find_by_category(
        self, limit: int, offset: int, category_id: int
    ) -> list[Post]:
        query = (
            select(
                PostEntity,
                (
                    select(func.count(PostCommentEntity.id))
                    .where(PostCommentEntity.post_id == PostEntity.id)
                    .scalar_subquery()
                    .label("comment_count")
                )
            )
            .where(PostEntity.is_active)
            .order_by(PostEntity.created_dtm.desc())
            .limit(limit)
            .offset(offset)
        )
        if category_id:
            query = query.where(PostEntity.category_id == category_id)
        result = await self._session.execute(query)
        return [
            row.PostEntity.to_domain(comment_count=row.comment_count)
            for row in result.fetchall()
        ]

    async def count_by_category(self, category_id: int) -> int:
        query = select(func.count(PostEntity.id)).where(PostEntity.is_active)
        if category_id:
            query = query.where(PostEntity.category_id == category_id)
        result = await self._session.execute(query)
        return result.scalar_one()
