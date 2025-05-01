from datetime import date, time

import pytest

from app.application.service.schedule_service import ScheduleService
from app.common.exception import APIException
from app.common.http import Http4XX
from app.domain import MemberType
from .factory import ScheduleFactory, UserBandFactory


@pytest.mark.asyncio
async def test_일정_생성(schedule_repo, user_band_repo):
    schedule = ScheduleFactory.generate()
    user_band_repo.find_by_user_and_band.return_value = UserBandFactory.generate(
        member_type=MemberType.LEADER
    )
    schedule_repo.save.return_value = schedule

    service = ScheduleService(schedule_repo, user_band_repo)
    result = await service.create_schedule(
        user_id=1,
        band_id=1,
        title="일정",
        day=date(2025, 1, 1),
        start_time=None,
        end_time=None,
        location=None,
        memo=None,
    )

    assert result is schedule
    schedule_repo.save.assert_called_once()


@pytest.mark.asyncio
async def test_가입하지_않은_밴드에_일정_생성_실패(schedule_repo, user_band_repo):
    user_band_repo.find_by_user_and_band.return_value = None

    service = ScheduleService(schedule_repo, user_band_repo)
    with pytest.raises(APIException) as exc:
        await service.create_schedule(1, 1, "타이틀", date(2025, 1, 1))
    assert exc.value.http == Http4XX.BAND_NOT_REGISTERED


@pytest.mark.asyncio
async def test_일반_권한으로_일정_생성_실패(schedule_repo, user_band_repo):
    user_band_repo.find_by_user_and_band.return_value = UserBandFactory.generate(
        member_type=MemberType.NORMAL
    )

    service = ScheduleService(schedule_repo, user_band_repo)
    with pytest.raises(APIException) as exc:
        await service.create_schedule(1, 1, "타이틀", date(2025, 1, 1))
    assert exc.value.http == Http4XX.PERMISSION_DENIED


@pytest.mark.asyncio
async def test_일정_정보_조회(schedule_repo, user_band_repo):
    schedule = ScheduleFactory.generate()
    schedule_repo.find_by_id_with_user.return_value = schedule

    service = ScheduleService(schedule_repo, user_band_repo)
    result = await service.get_schedule_info(schedule_id=1)

    assert result is schedule
    schedule_repo.find_by_id_with_user.assert_called_once()


@pytest.mark.asyncio
async def test_존재하지_않는_일정_조회(schedule_repo, user_band_repo):
    schedule_repo.find_by_id_with_user.return_value = None

    service = ScheduleService(schedule_repo, user_band_repo)
    with pytest.raises(APIException) as exc:
        await service.get_schedule_info(schedule_id=1)
    assert exc.value.http == Http4XX.SCHEDULE_NOT_FOUND


@pytest.mark.asyncio
async def test_일정_리스트_조회(schedule_repo, user_band_repo):
    schedule_repo.find_active_schedules_with_user.return_value = [
        ScheduleFactory.generate(),
        ScheduleFactory.generate(),
        ScheduleFactory.generate(),
    ]

    service = ScheduleService(schedule_repo, user_band_repo)
    result = await service.get_band_schedules(
        1, 1, from_=date(2025, 1, 1), to=date(2025, 1, 1)
    )

    assert len(result) == 3
    schedule_repo.find_active_schedules_with_user.assert_called_once()


@pytest.mark.asyncio
async def test_일정_정보_수정(schedule_repo, user_band_repo):
    title = "변경 일정"
    day = date(2025, 2, 1)
    start_time = time(11, 0)
    end_time = time(13, 0)
    location = "변경 연습실"
    memo = "변경 메모"
    song = ScheduleFactory.generate()
    schedule_repo.find_by_id_with_user.return_value = song
    schedule_repo.save.return_value = song
    user_band_repo.find_by_user_and_band.return_value = UserBandFactory.generate(
        member_type=MemberType.LEADER
    )

    service = ScheduleService(schedule_repo, user_band_repo)
    result = await service.update_schedule_info(
        schedule_id=1,
        user_id=1,
        title=title,
        day=day,
        start_time=start_time,
        end_time=end_time,
        location=location,
        memo=memo,
    )

    assert result is song
    assert result.title == title
    assert result.day == day
    assert result.start_time == start_time
    assert result.end_time == end_time
    assert result.location == location
    assert result.memo == memo
    schedule_repo.find_by_id_with_user.assert_called_once()
    schedule_repo.save.assert_called_once_with(song)


@pytest.mark.asyncio
async def test_존재하지_않는_일정_정보_수정_실패(schedule_repo, user_band_repo):
    schedule_repo.find_by_id_with_user.return_value = None
    user_band_repo.find_by_user_and_band.return_value = None

    service = ScheduleService(schedule_repo, user_band_repo)
    with pytest.raises(APIException) as exc:
        await service.update_schedule_info(
            schedule_id=1,
            user_id=1,
            title="타이틀",
            day=date(2025, 2, 1),
            start_time=time(11, 0),
            end_time=time(13, 0),
        )
    assert exc.value.http == Http4XX.SCHEDULE_NOT_FOUND


@pytest.mark.asyncio
async def test_가입하지_않은_밴드_일정_정보_수정_실패(schedule_repo, user_band_repo):
    schedule_repo.find_by_id_with_user.return_value = ScheduleFactory.generate()
    user_band_repo.find_by_user_and_band.return_value = None

    service = ScheduleService(schedule_repo, user_band_repo)
    with pytest.raises(APIException) as exc:
        await service.update_schedule_info(
            schedule_id=1,
            user_id=1,
            title="타이틀",
            day=date(2025, 2, 1),
            start_time=time(11, 0),
            end_time=time(13, 0),
        )
    assert exc.value.http == Http4XX.BAND_NOT_REGISTERED


@pytest.mark.asyncio
async def test_일반_권한으로_일정_정보_수정_실패(schedule_repo, user_band_repo):
    schedule_repo.find_by_id_with_user.return_value = ScheduleFactory.generate()
    user_band_repo.find_by_user_and_band.return_value = UserBandFactory.generate(
        member_type=MemberType.NORMAL
    )

    service = ScheduleService(schedule_repo, user_band_repo)
    with pytest.raises(APIException) as exc:
        await service.update_schedule_info(
            schedule_id=1,
            user_id=1,
            title="타이틀",
            day=date(2025, 2, 1),
            start_time=time(11, 0),
            end_time=time(13, 0),
        )
    assert exc.value.http == Http4XX.PERMISSION_DENIED
