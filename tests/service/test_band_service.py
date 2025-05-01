import pytest

from app.application.service.band_service import BandService
from app.common.exception import APIException
from app.common.http import Http4XX
from app.domain import MemberType
from .factory import UserBandFactory, BandFactory


@pytest.mark.asyncio
async def test_밴드_생성(band_repo, user_band_repo):
    band = BandFactory.generate()
    band_repo.save.return_value = band
    band_repo.create_link.return_value = True
    user_band_repo.save.return_value = True

    service = BandService(band_repo, user_band_repo)
    result = await service.create_band(1, "밴드", MemberType.LEADER)

    assert result is band
    band_repo.save.assert_called_once()
    user_band_repo.save.assert_called_once()


@pytest.mark.asyncio
async def test_밴드_정보_조회(band_repo, user_band_repo):
    band = BandFactory.generate()
    band_repo.find_by_id_or_none.return_value = band

    service = BandService(band_repo, user_band_repo)
    result = await service.get_band_info(band_id=1)

    assert result is band
    band_repo.find_by_id_or_none.assert_called_once()


@pytest.mark.asyncio
async def test_존재하지_않는_밴드_조회(band_repo, user_band_repo):
    band_repo.find_by_id_or_none.return_value = None

    service = BandService(band_repo, user_band_repo)
    with pytest.raises(APIException) as exc:
        await service.get_band_info(band_id=1)
    assert exc.value.http == Http4XX.BAND_NOT_FOUND


@pytest.mark.asyncio
async def test_밴드_멤버_조회(band_repo, user_band_repo):
    user_band_repo.find_band_users.return_value = [
        UserBandFactory.generate(),
        UserBandFactory.generate(),
        UserBandFactory.generate(),
    ]

    service = BandService(band_repo, user_band_repo)
    result = await service.get_band_members(band_id=1)

    user_band_repo.find_band_users.assert_called_once()
    assert len(result) == 3
