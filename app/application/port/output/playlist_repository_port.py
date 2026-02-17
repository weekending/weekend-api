from abc import ABC, abstractmethod

from app.domain.playlist import Playlist


class PlaylistRepositoryPort(ABC):
    @abstractmethod
    async def save(self, playlist: Playlist) -> Playlist:
        raise NotImplementedError

    @abstractmethod
    async def find_by_id_with_songs(self, id_: int) -> Playlist | None:
        raise NotImplementedError

    @abstractmethod
    async def find_by_band(
        self, band_id: int, limit: int, offset: int
    ) -> list[Playlist]:
        raise NotImplementedError
