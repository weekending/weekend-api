from sqlalchemy import delete, select

from app.adapter.outbound.persistence.models import SongModel
from app.adapter.outbound.persistence.reporitory.base import BaseRepository
from app.application.port.output import SongRepositoryPort
from app.domain import Song


class SongPersistenceAdapter(BaseRepository, SongRepositoryPort):
    async def save(self, song: Song) -> Song:
        model = SongModel.from_domain(song)
        self._session.add(model)
        await self._session.commit()
        return model.to_domain()

    async def remove(self, song: Song):
        await self._session.execute(
            delete(SongModel).where(SongModel.id == song.id)
        )

    async def find_by_id_or_none(self, id_: int) -> Song | None:
        result = await self._session.execute(
            select(SongModel).where(SongModel.id == id_)
        )
        if band := result.scalar_one_or_none():
            return band.to_domain()
