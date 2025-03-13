from sqlalchemy import select

from app.adapter.outbound.persistence.models import BandModel
from app.adapter.outbound.persistence.reporitory.base import BaseRepository
from app.application.port.output import BandRepositoryPort
from app.domain import Band


class BandPersistenceAdapter(BaseRepository, BandRepositoryPort):
    async def save(self, band: Band) -> Band:
        model = await self._save(band, BandModel)
        return model.to_domain()

    async def find_by_id_or_none(self, id_: int) -> Band | None:
        if model := await self._find_by_id_or_none(id_, BandModel):
            return model.to_domain()
