from sqlalchemy import select

from app.adapter.outbound.persistence.models.band import BandModel
from app.adapter.outbound.persistence.reporitory.base import BaseRepository
from app.application.port.output import BandRepositoryPort
from app.domain import Band


class BandPersistenceAdapter(BaseRepository, BandRepositoryPort):
    async def save(self, band: Band) -> Band:
        model = BandModel.from_domain(band)
        self._session.add(model)
        await self._session.commit()
        return model.to_domain()

    async def find_by_id_or_none(self, id_: int) -> Band | None:
        result = await self._session.execute(
            select(BandModel).where(BandModel.id == id_)
        )
        if band := result.scalar_one_or_none():
            return band.to_domain()
