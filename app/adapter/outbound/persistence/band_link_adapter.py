from app.adapter.outbound.persistence.models.band import BandLinkModel
from app.adapter.outbound.persistence.reporitory.base import BaseRepository
from app.application.port.output import BandLinkRepositoryPort
from app.domain import BandLink


class BandLinkPersistenceAdapter(BaseRepository, BandLinkRepositoryPort):
    async def save(self, band_link: BandLink) -> BandLink:
        model = BandLinkModel.from_domain(band_link)
        self._session.add(model)
        await self._session.commit()
        return model.to_domain()
