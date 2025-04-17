from sqlalchemy import delete, select

from app.adapter.outbound.persistence.entity import SongEntity
from app.adapter.outbound.persistence.reporitory.base import BaseRepository
from app.application.port.output import SongRepositoryPort
from app.domain import Song


class SongPersistenceAdapter(BaseRepository, SongRepositoryPort):
    async def save(self, song: Song) -> Song:
        model = await self._save(song, SongEntity)
        return model.to_domain()

    async def remove(self, song: Song):
        await self._session.execute(
            delete(SongEntity).where(SongEntity.id == song.id)
        )

    async def find_by_id_or_none(self, id_: int) -> Song | None:
        if model := await self._find_by_id_or_none(id_, SongEntity):
            return model.to_domain()

    async def find_by_band(self, band_id: int) -> list[Song]:
        result = await self._session.execute(
            select(SongEntity)
            .where(
                SongEntity.is_active,
                SongEntity.band_id == band_id,
            )
            .order_by(SongEntity.id.desc())
        )
        return [song.to_domain() for song in result.scalars()]
