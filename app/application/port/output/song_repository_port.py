from abc import ABC, abstractmethod

from app.domain import Song, SongStatus


class SongRepositoryPort(ABC):
    @abstractmethod
    async def save(self, song: Song) -> Song:
        raise NotImplementedError

    @abstractmethod
    async def remove(self, song: Song):
        raise NotImplementedError

    @abstractmethod
    async def find_by_id_or_none(self, id_: int) -> Song | None:
        raise NotImplementedError

    @abstractmethod
    async def find_by_band(self, band_id: int, status: SongStatus) -> list[Song]:
        raise NotImplementedError

