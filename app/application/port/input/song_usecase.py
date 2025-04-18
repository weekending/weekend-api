from abc import ABC, abstractmethod

from app.domain import Song, SongStatus


class SongUseCase(ABC):
    @abstractmethod
    async def get_song_list(
        self, user_id: int, band_id: int, status: SongStatus
    ) -> list[Song]:
        raise NotImplementedError

    @abstractmethod
    async def create_song(
        self, user_id: int, band_id: int, title: str, singer: str
    ) -> Song:
        raise NotImplementedError

    @abstractmethod
    async def get_song_info(self, song_id: int) -> Song:
        raise NotImplementedError

    @abstractmethod
    async def remove_song(self, song_id: int):
        raise NotImplementedError

    @abstractmethod
    async def update_status(self, song_id: int, status: SongStatus) -> Song:
        raise NotImplementedError
