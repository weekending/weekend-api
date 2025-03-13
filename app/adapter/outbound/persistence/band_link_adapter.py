from app.adapter.outbound.persistence.models import BandLinkModel
from app.adapter.outbound.persistence.reporitory.base import BaseRepository
from app.application.port.output import BandLinkRepositoryPort
from app.domain import BandLink


class BandLinkPersistenceAdapter(BaseRepository, BandLinkRepositoryPort):
    async def save(self, band_link: BandLink) -> BandLink:
        model = await self._save(band_link, BandLinkModel)
        return model.to_domain()
