from typing import Iterable

from fastapi import Depends

from app.adapter.outbound.persistence import (
    UserBandPersistenceAdapter,
    UserPersistenceAdapter,
)
from app.common.exception import APIException
from app.common.http import Http4XX
from app.domain import Band, User
from ..port.input import UserUseCase
from ..port.output import UserBandRepositoryPort, UserRepositoryPort


class UserService(UserUseCase):
    def __init__(
        self,
        user_band_repo: UserBandRepositoryPort = Depends(UserBandPersistenceAdapter),
        user_repo: UserRepositoryPort = Depends(UserPersistenceAdapter),
    ):
        self._user_band_repo = user_band_repo
        self._user_repo = user_repo

    async def get_user_info(self, user_id: int) -> User:
        if not (user := await self._user_repo.find_by_id_or_none(user_id)):
            raise APIException(Http4XX.USER_NOT_FOUND)
        return user

    async def get_user_bands(self, user_id: int) -> Iterable[Band]:
        return await self._user_band_repo.find_user_bands(user_id)
