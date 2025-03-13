from datetime import datetime
from fastapi import Depends

from app.adapter.outbound.persistence import SongPersistenceAdapter
from app.common.exception import APIException
from app.common.http import Http4XX
from app.domain import Song, SongStatus
from ..port.input import SongUseCase
from ..port.output import SongRepositoryPort


class SongService(SongUseCase):
    def __init__(
        self,
        song_repo: SongRepositoryPort = Depends(SongPersistenceAdapter),
    ):
        self._song_repo = song_repo

    async def create_song(
        self, user_id: int, band_id: int, title: str, singer: str
    ) -> Song:
        return await self._song_repo.save(
            Song(
                band_id=band_id,
                user_id=user_id,
                status=SongStatus.PENDING,
                title=title,
                singer=singer,
                thumbnail=None,
                is_active=True,
                created_dtm=datetime.now(),
                in_progress_dtm=None,
                closed_dtm=None,
            )
        )

    async def get_song_info(self, song_id: int) -> Song:
        if not (song := await self._song_repo.find_by_id_or_none(song_id)):
            raise APIException(Http4XX.SONG_NOT_FOUND)
        return song

    async def remove_song(self, song_id: int):
        if not (song := await self._song_repo.find_by_id_or_none(song_id)):
            raise APIException(Http4XX.SONG_NOT_FOUND)
        await self._song_repo.remove(song)

    async def update_status(self, song_id: int, status: SongStatus) -> Song:
        if not (song := await self._song_repo.find_by_id_or_none(song_id)):
            raise APIException(Http4XX.SONG_NOT_FOUND)
        song.status = status
        return await self._song_repo.save(song)
