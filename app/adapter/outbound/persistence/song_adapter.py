from sqlalchemy import delete, select

from app.adapter.outbound.persistence.models import SongModel
from app.adapter.outbound.persistence.reporitory.base import BaseRepository
from app.application.port.output import SongRepositoryPort
from app.domain import Song


class SongPersistenceAdapter(BaseRepository, SongRepositoryPort):
    async def save(self, song: Song) -> Song:
        model = await self._save(song, SongModel)
        return model.to_domain()

    async def remove(self, song: Song):
        await self._session.execute(
            delete(SongModel).where(SongModel.id == song.id)
        )

    async def find_by_id_or_none(self, id_: int) -> Song | None:
        if model := await self._find_by_id_or_none(id_, SongModel):
            return model.to_domain()
