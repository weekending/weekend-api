import pytest

from app.application.service.user_service import UserService
from app.common.exception import APIException
from app.common.http import Http4XX
from .factory import BandFactory, UserFactory


@pytest.mark.asyncio
async def test_일정_사용자_조회(user_band_repo, user_repo):
    user = UserFactory.generate()
    user_repo.find_by_id_or_none.return_value = user

    service = UserService(user_band_repo, user_repo)
    result = await service.get_user_info(user_id=1)

    assert result is user
    user_repo.find_by_id_or_none.assert_called_once()


@pytest.mark.asyncio
async def test_존재하지_않는_사용자_조회(user_band_repo, user_repo):
    user_repo.find_by_id_or_none.return_value = None

    service = UserService(user_band_repo, user_repo)
    with pytest.raises(APIException) as exc:
        await service.get_user_info(user_id=1)
    assert exc.value.http == Http4XX.USER_NOT_FOUND


@pytest.mark.asyncio
async def test_일정_사용자_가입_밴드_조회(user_band_repo, user_repo):
    user_band_repo.find_user_bands.return_value = (
        BandFactory.generate(),
        BandFactory.generate(),
        BandFactory.generate(),
    )

    service = UserService(user_band_repo, user_repo)
    result = await service.get_user_bands(user_id=1)

    assert len(list(result)) == 3
    user_band_repo.find_user_bands.assert_called_once()
