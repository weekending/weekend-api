from abc import ABC, abstractmethod

from app.domain import Band, BandLink


class BandRepositoryPort(ABC):
    @abstractmethod
    async def save(self, band: Band) -> Band:
        raise NotImplementedError

    @abstractmethod
    async def find_by_id_or_none(self, id_: int) -> Band | None:
        raise NotImplementedError

    @abstractmethod
    async def create_link(self, band_link: BandLink) -> BandLink:
        raise NotImplementedError
