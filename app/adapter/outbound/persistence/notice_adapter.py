from sqlalchemy import select
from sqlalchemy.orm import joinedload

from app.adapter.outbound.persistence.entity import NoticeEntity, NoticeImageEntity
from app.adapter.outbound.persistence.reporitory.base import BaseRepository
from app.application.port.output import NoticeRepositoryPort
from app.domain import Notice


class NoticePersistenceAdapter(BaseRepository, NoticeRepositoryPort):
    async def find_by_id_or_none(self, id_: int) -> Notice | None:
        result = await self._session.execute(
            select(NoticeEntity)
            .where(NoticeEntity.id == id_)
            .options(
                joinedload(NoticeEntity.images.and_(NoticeImageEntity.is_active))
            )
        )
        if not (model := result.unique().scalar_one_or_none()):
            return None
        return model.to_domain()

    async def find_all(self, limit: int, offset: int) -> list[Notice]:
        result = await self._session.execute(
            select(NoticeEntity)
            .where(NoticeEntity.is_active)
            .order_by(NoticeEntity.created_dtm.desc())
            .limit(limit)
            .offset(offset)
        )
        return [notice.to_domain() for notice in result.unique().scalars()]
