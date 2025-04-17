from app.adapter.outbound.persistence.entity import BandEntity, BandLinkEntity
from app.adapter.outbound.persistence.reporitory.base import BaseRepository
from app.application.port.output import BandRepositoryPort
from app.domain import Band, BandLink


class BandPersistenceAdapter(BaseRepository, BandRepositoryPort):
    async def save(self, band: Band) -> Band:
        model = await self._save(band, BandEntity)
        return model.to_domain()

    async def find_by_id_or_none(self, id_: int) -> Band | None:
        if model := await self._find_by_id_or_none(id_, BandEntity):
            return model.to_domain()

    async def create_link(self, band_link: BandLink) -> BandLink:
        model = await self._save(band_link, BandLinkEntity)
        return model.to_domain()
