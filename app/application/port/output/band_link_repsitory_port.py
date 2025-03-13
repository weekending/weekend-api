from abc import ABC, abstractmethod

from app.domain import BandLink


class BandLinkRepositoryPort(ABC):
    @abstractmethod
    async def save(self, band_link: BandLink) -> BandLink:
        raise NotImplementedError
