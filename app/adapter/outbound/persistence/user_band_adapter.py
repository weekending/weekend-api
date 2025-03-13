from typing import Sequence, Iterable

from sqlalchemy import insert, select

from app.adapter.outbound.persistence.models import (
    BandModel,
    user_band_model,
)
from app.adapter.outbound.persistence.reporitory.base import BaseRepository
from app.application.port.output import UserBandRepositoryPort
from app.domain import Band, UserBand


class UserBandPersistenceAdapter(BaseRepository, UserBandRepositoryPort):
    async def save(self, user_band: UserBand):
        await self._session.execute(
            insert(user_band_model).values(
                user_id=user_band.user_id,
                band_id=user_band.band_id,
                member_type=user_band.member_type,
            )
        )
        await self._session.commit()

    async def find_user_bands(self, user_id: int) -> Iterable[Band]:
        result = await self._session.execute(
            select(BandModel)
            .select_from(
                user_band_model.join(
                    BandModel, user_band_model.c.band_id == BandModel.id
                )
            )
            .where(user_band_model.c.user_id == user_id)
        )
        return map(lambda band: band.to_domain(), result.scalars())
