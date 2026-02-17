from abc import ABC, abstractmethod

from app.domain.playlist import Playlist


class PlaylistUseCase(ABC):
    @abstractmethod
    async def get_playlist_list(
        self, band_id: int, page: int, size: int
    ) -> list[Playlist]:
        raise NotImplementedError

    @abstractmethod
    async def create_playlist(
        self, user_id: int, band_id: int, title: str, description: str | None
    ) -> Playlist:
        raise NotImplementedError

    @abstractmethod
    async def get_playlist_info(self, playlist_id: int) -> Playlist:
        raise NotImplementedError
