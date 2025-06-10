from sqlalchemy import select

from app.adapter.outbound.persistence.entity import PostCategoryEntity
from app.adapter.outbound.persistence.reporitory.base import BaseRepository
from app.application.port.output import PostCategoryRepositoryPort
from app.domain import PostCategory


class PostCategoryPersistenceAdapter(BaseRepository, PostCategoryRepositoryPort):
    async def find_by_id_or_none(self, id_: int) -> PostCategory | None:
        if entity := await self._find_by_id_or_none(id_, PostCategoryEntity):
            return entity.to_domain()
        return None

    async def find_active_list(self) -> list[PostCategory]:
        result = await self._session.execute(
            select(PostCategoryEntity).where(
                PostCategoryEntity.is_active
            ).order_by(PostCategoryEntity.sequence)
        )
        return [category.to_domain() for category in result.scalars()]
