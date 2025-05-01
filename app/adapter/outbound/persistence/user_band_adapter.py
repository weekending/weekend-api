from typing import Iterable

from sqlalchemy import insert, select

from app.adapter.outbound.persistence.entity import BandEntity, UserEntity, user_band_entity
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

    async def find_by_user_and_band(self, user_id: int, band_id: int) -> UserBand | None:
        result = await self._session.execute(
            select(user_band_entity).where(
                user_band_entity.c.user_id == user_id,
                user_band_entity.c.band_id == band_id,
            )
        )
        if band_user := result.fetchone():
            return UserBand(
                id=band_user.id,
                user_id=band_user.user_id,
                band_id=band_user.band_id,
                member_type=band_user.member_type,
                user=None,
            )

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

    async def find_band_users(self, band_id: int) -> list[UserBand]:
        result = await self._session.execute(
            select(user_band_entity, UserEntity)
            .select_from(
                user_band_entity.join(
                    UserEntity, user_band_entity.c.user_id == UserEntity.id
                )
            )
            .where(user_band_entity.c.band_id == band_id)
            .order_by(
                user_band_entity.c.member_type, user_band_entity.c.created_dtm
            )
        )
        return [
            UserBand(
                id=row.id,
                user_id=row.user_id,
                band_id=row.band_id,
                member_type=row.member_type,
                user=row.UserEntity.to_domain(),
            )
            for row in result.all()
        ]
