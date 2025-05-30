from datetime import datetime
from fastapi import Depends

from app.adapter.outbound.persistence import (
    SongPersistenceAdapter,
    UserBandPersistenceAdapter,
)
from app.common.exception import APIException
from app.common.http import Http4XX
from app.common.utils import check_user_leader_permission
from app.domain import Song, SongStatus
from ..port.input import SongUseCase
from ..port.output import SongRepositoryPort, UserBandRepositoryPort


class SongService(SongUseCase):
    def __init__(
        self,
        song_repo: SongRepositoryPort = Depends(SongPersistenceAdapter),
        user_band_repo: UserBandRepositoryPort = Depends(UserBandPersistenceAdapter),
    ):
        self._song_repo = song_repo
        self._user_band_repo = user_band_repo

    async def get_song_list(
        self, user_id: int, band_id: int, status: SongStatus
    ) -> list[Song]:
        return await self._song_repo.find_by_band(band_id, status)

    async def create_song(
        self, user_id: int, band_id: int, title: str, singer: str
    ) -> Song:
        check_user_leader_permission(
            user_band=await self._user_band_repo.find_by_user_and_band(
                user_id, band_id
            )
        )
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

    async def remove_song(self, song_id: int, user_id: int):
        if not (song := await self._song_repo.find_by_id_or_none(song_id)):
            raise APIException(Http4XX.SONG_NOT_FOUND)

        check_user_leader_permission(
            user_band=await self._user_band_repo.find_by_user_and_band(
                user_id, song.band_id
            )
        )
        await self._song_repo.remove(song)

    def _update_status(self, song: Song, status: SongStatus):
        match status:
            case SongStatus.PENDING:
                song.in_progress_dtm = None
                song.closed_dtm = None
            case SongStatus.INPROGRESS:
                song.in_progress_dtm = datetime.now()
            case SongStatus.CLOSED:
                song.closed_dtm = datetime.now()
        song.status = status

    async def update_song_info(
        self,
        song_id: int,
        user_id: int,
        title: str = None,
        singer: str = None,
        thumbnail: str = None,
        status: SongStatus = None,
    ) -> Song:
        if not (song := await self._song_repo.find_by_id_or_none(song_id)):
            raise APIException(Http4XX.SONG_NOT_FOUND)

        check_user_leader_permission(
            user_band=await self._user_band_repo.find_by_user_and_band(
                user_id, song.band_id
            )
        )
        if title:
            song.title = title
        if singer:
            song.singer = singer
        if thumbnail:
            song.thumbnail = thumbnail
        if status and song.status != status:
            self._update_status(song, status)
        return await self._song_repo.save(song)
