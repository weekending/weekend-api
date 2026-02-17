from datetime import datetime

from fastapi import Depends

from app.adapter.outbound.persistence import (
    PlaylistPersistenceAdapter,
    UserBandPersistenceAdapter,
)
from app.common.exception import APIException
from app.common.http import Http4XX
from app.common.utils import check_user_leader_permission
from app.domain.playlist import Playlist
from ..port.input import PlaylistUseCase
from ..port.output import PlaylistRepositoryPort, UserBandRepositoryPort


class PlaylistService(PlaylistUseCase):
    def __init__(
        self,
        playlist_repo: PlaylistRepositoryPort = Depends(PlaylistPersistenceAdapter),
        user_band_repo: UserBandRepositoryPort = Depends(UserBandPersistenceAdapter),
    ):
        self._playlist_repo = playlist_repo
        self._user_band_repo = user_band_repo

    async def get_playlist_list(
        self, band_id: int, page: int, size: int
    ) -> list[Playlist]:
        return await self._playlist_repo.find_by_band(
            band_id, limit=size, offset=size * (page - 1)
        )

    async def create_playlist(
        self, user_id: int, band_id: int, title: str, description: str | None
    ) -> Playlist:
        check_user_leader_permission(
            user_band=await self._user_band_repo.find_by_user_and_band(
                user_id, band_id
            )
        )
        return await self._playlist_repo.save(
            Playlist(
                band_id=band_id,
                title=title,
                description=description,
                thumbnail=None,
                is_active=True,
                songs=[],
                created_dtm=datetime.now(),
                updated_dtm=None,
            )
        )

    async def get_playlist_info(self, playlist_id: int) -> Playlist:
        if not (playlist := await self._playlist_repo.find_by_id_with_songs(playlist_id)):
            raise APIException(Http4XX.PLAYLIST_NOT_FOUND)
        return playlist
