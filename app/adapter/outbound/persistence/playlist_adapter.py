from sqlalchemy import select
from sqlalchemy.orm import selectinload, with_loader_criteria

from app.adapter.outbound.persistence.entity import SongEntity
from app.adapter.outbound.persistence.entity.playlist import (
    PlaylistEntity,
    playlist_song_entity,
)
from app.adapter.outbound.persistence.reporitory.base import BaseRepository
from app.application.port.output import PlaylistRepositoryPort
from app.domain.playlist import Playlist


class PlaylistPersistenceAdapter(BaseRepository, PlaylistRepositoryPort):
    async def save(self, playlist: Playlist) -> Playlist:
        model = await self._save(playlist, PlaylistEntity)
        return model.to_domain()

    async def find_by_id_with_songs(self, id_: int) -> Playlist | None:
        result = await self._session.execute(
            select(PlaylistEntity)
            .options(
                selectinload(PlaylistEntity.songs),
                with_loader_criteria(SongEntity, SongEntity.is_active == True),
            )
            .where(PlaylistEntity.id == id_)
        )
        if not (playlist := result.scalar_one_or_none()):
            return None
        return playlist.to_domain()

    async def find_by_band(
        self, band_id: int, limit: int, offset: int
    ) -> list[Playlist]:
        query = select(PlaylistEntity).where(
            PlaylistEntity.band_id == band_id,
            PlaylistEntity.is_active.is_(True)
        )
        result = await self._session.execute(
            query.order_by(
                PlaylistEntity.created_dtm.desc(), PlaylistEntity.id.desc()
            )
            .limit(limit)
            .offset(offset)
        )
        return [p.to_domain() for p in result.scalars()]
