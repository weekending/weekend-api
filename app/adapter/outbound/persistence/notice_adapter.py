from sqlalchemy import select

from app.adapter.outbound.persistence.entity import NoticeEntity
from app.adapter.outbound.persistence.reporitory.base import BaseRepository
from app.application.port.output import NoticeRepositoryPort
from app.domain import Notice


class NoticePersistenceAdapter(BaseRepository, NoticeRepositoryPort):
    async def find_by_id_or_none(self, id_: int) -> Notice | None:
        if not (model := await self._find_by_id_or_none(id_, NoticeEntity)):
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
        return [notice.to_domain() for notice in result.scalars()]
