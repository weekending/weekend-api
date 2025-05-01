from uuid import uuid4

from fastapi import Depends

from app.adapter.outbound.persistence import (
    BandPersistenceAdapter,
    UserBandPersistenceAdapter,
)
from app.common.exception import APIException
from app.common.http import Http4XX
from app.domain import Band, BandLink, MemberType, User, UserBand
from ..port.input import BandUseCase
from ..port.output import BandRepositoryPort, UserBandRepositoryPort


class BandService(BandUseCase):
    def __init__(
        self,
        band_repo: BandRepositoryPort = Depends(BandPersistenceAdapter),
        user_band_repo: UserBandRepositoryPort = Depends(UserBandPersistenceAdapter),
    ):
        self._band_repo = band_repo
        self._user_band_repo = user_band_repo

    async def create_band(
        self,
        user_id: int,
        name: str,
        member_type: MemberType,
    ) -> Band:
        """새 밴드를 생성하여 사용자를 `LEADER` 타입으로 설정"""
        band = await self._band_repo.save(
            Band(name=name, thumbnail=None, is_active=True)
        )
        await self._user_band_repo.save(
            UserBand(user_id=user_id, band_id=band.id, member_type=member_type, user=None)
        )
        await self._band_repo.create_link(
            BandLink(band_id=band.id, hash=uuid4().hex[:18], is_active=True)
        )
        return band

    async def get_band_info(self, band_id: int) -> Band:
        if not (band := await self._band_repo.find_by_id_or_none(band_id)):
            raise APIException(Http4XX.BAND_NOT_FOUND)
        return band

    async def get_band_members(self, band_id: int) -> list[UserBand]:
        return await self._user_band_repo.find_band_users(band_id)
