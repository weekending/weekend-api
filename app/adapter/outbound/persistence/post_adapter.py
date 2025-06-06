from sqlalchemy import select

from app.adapter.outbound.persistence.entity import PostEntity
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
        result = await self._session.execute(
            select(PostEntity)
            .where(PostEntity.is_active, PostEntity.category_id == category_id)
            .order_by(PostEntity.created_dtm.desc())
            .limit(limit)
            .offset(offset)
        )
        return [song.to_domain() for song in result.scalars()]
