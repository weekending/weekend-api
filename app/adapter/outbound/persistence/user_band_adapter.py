from typing import Iterable

from sqlalchemy import insert, select

from app.adapter.outbound.persistence.entity import BandEntity, user_band_entity
from app.adapter.outbound.persistence.reporitory.base import BaseRepository
from app.application.port.output import UserBandRepositoryPort
from app.domain import Band, UserBand


class UserBandPersistenceAdapter(BaseRepository, UserBandRepositoryPort):
    async def save(self, user_band: UserBand):
        await self._session.execute(
            insert(user_band_entity).values(
                user_id=user_band.user_id,
                band_id=user_band.band_id,
                member_type=user_band.member_type,
            )
        )
        await self._session.commit()

    async def exists(self, user_id: int, band_id: int) -> bool:
        result = await self._session.execute(
            select(user_band_entity).where(
                user_band_entity.c.user_id == user_id,
                user_band_entity.c.band_id == band_id,
            ).limit(1)
        )
        return result.scalar_one_or_none() is not None

    async def find_user_bands(self, user_id: int) -> Iterable[Band]:
        result = await self._session.execute(
            select(BandEntity)
            .select_from(
                user_band_entity.join(
                    BandEntity, user_band_entity.c.band_id == BandEntity.id
                )
            )
            .where(user_band_entity.c.user_id == user_id)
        )
        return map(lambda band: band.to_domain(), result.scalars())
