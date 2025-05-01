import pytest

from app.application.service.song_service import SongService
from app.common.exception import APIException
from app.common.http import Http4XX
from app.domain import MemberType, SongStatus
from .factory import SongFactory, UserBandFactory


@pytest.mark.asyncio
async def test_연습곡_리스트_조회(song_repo, user_band_repo):
    song_repo.find_by_band.return_value = [
        SongFactory.generate(),
        SongFactory.generate(),
        SongFactory.generate(),
    ]

    service = SongService(song_repo, user_band_repo)
    result = await service.get_song_list(1, 1, None)

    assert len(result) == 3
    song_repo.find_by_band.assert_called_once()


@pytest.mark.asyncio
async def test_연습곡_생성(song_repo, user_band_repo):
    song = SongFactory.generate()
    user_band_repo.find_by_user_and_band.return_value = UserBandFactory.generate(
        member_type=MemberType.LEADER
    )
    song_repo.save.return_value = song

    service = SongService(song_repo, user_band_repo)
    result = await service.create_song(1, 1, "타이틀", "가수")

    assert result is song
    song_repo.save.assert_called_once()


@pytest.mark.asyncio
async def test_가입하지_않은_밴드에_연습곡_생성_실패(song_repo, user_band_repo):
    user_band_repo.find_by_user_and_band.return_value = None

    service = SongService(song_repo, user_band_repo)
    with pytest.raises(APIException) as exc:
        await service.create_song(1, 1, "타이틀", "가수")
    assert exc.value.http == Http4XX.BAND_NOT_REGISTERED


@pytest.mark.asyncio
async def test_일반_권한으로_연습곡_생성_실패(song_repo, user_band_repo):
    user_band_repo.find_by_user_and_band.return_value = UserBandFactory.generate(
        member_type=MemberType.NORMAL
    )

    service = SongService(song_repo, user_band_repo)
    with pytest.raises(APIException) as exc:
        await service.create_song(1, 1, "타이틀", "가수")
    assert exc.value.http == Http4XX.PERMISSION_DENIED


@pytest.mark.asyncio
async def test_연습곡_정보_조회(song_repo, user_band_repo):
    song = SongFactory.generate()
    song_repo.find_by_id_or_none.return_value = song

    service = SongService(song_repo, user_band_repo)
    result = await service.get_song_info(song_id=1)

    assert result is song
    song_repo.find_by_id_or_none.assert_called_once()


@pytest.mark.asyncio
async def test_존재하지_않는_연습곡_조회(song_repo, user_band_repo):
    song_repo.find_by_id_or_none.return_value = None

    service = SongService(song_repo, user_band_repo)
    with pytest.raises(APIException) as exc:
        await service.get_song_info(song_id=1)
    assert exc.value.http == Http4XX.SONG_NOT_FOUND


@pytest.mark.asyncio
async def test_연습곡_제거(song_repo, user_band_repo):
    user_band_repo.find_by_user_and_band.return_value = UserBandFactory.generate(
        member_type=MemberType.LEADER
    )
    song_repo.remove.return_value = None

    service = SongService(song_repo, user_band_repo)
    await service.remove_song(1, 1)

    song_repo.remove.assert_called_once()


@pytest.mark.asyncio
async def test_존재하지_않는_연습곡_제거(song_repo, user_band_repo):
    song_repo.find_by_id_or_none.return_value = None

    service = SongService(song_repo, user_band_repo)
    with pytest.raises(APIException) as exc:
        await service.remove_song(1, 1)
    assert exc.value.http == Http4XX.SONG_NOT_FOUND


@pytest.mark.asyncio
async def test_가입하지_않은_밴드_연습곡_제거_실패(song_repo, user_band_repo):
    user_band_repo.find_by_user_and_band.return_value = None

    service = SongService(song_repo, user_band_repo)
    with pytest.raises(APIException) as exc:
        await service.remove_song(1, 1)
    assert exc.value.http == Http4XX.BAND_NOT_REGISTERED


@pytest.mark.asyncio
async def test_일반_권한으로_연습곡_제거_실패(song_repo, user_band_repo):
    user_band_repo.find_by_user_and_band.return_value = UserBandFactory.generate(
        member_type=MemberType.NORMAL
    )

    service = SongService(song_repo, user_band_repo)
    with pytest.raises(APIException) as exc:
        await service.remove_song(1, 1)
    assert exc.value.http == Http4XX.PERMISSION_DENIED


@pytest.mark.asyncio
async def test_연습곡_정보_수정(song_repo, user_band_repo):
    title = "변경 타이틀"
    singer = "변경 가수"
    thumbnail = "https://thumbnail.com/img/001"
    song = SongFactory.generate()
    song_repo.find_by_id_or_none.return_value = song
    song_repo.save.return_value = song
    user_band_repo.find_by_user_and_band.return_value = UserBandFactory.generate(
        member_type=MemberType.LEADER
    )

    service = SongService(song_repo, user_band_repo)
    result = await service.update_song_info(1, 1, title, singer, thumbnail)

    assert result is song
    assert result.title == title
    assert result.singer == singer
    assert result.thumbnail == thumbnail
    song_repo.find_by_id_or_none.assert_called_once()
    song_repo.save.assert_called_once_with(song)


@pytest.mark.asyncio
async def test_연습곡_상태_연습중으로_수정(song_repo, user_band_repo):
    song = SongFactory.generate()
    song_repo.find_by_id_or_none.return_value = song
    song_repo.save.return_value = song
    user_band_repo.find_by_user_and_band.return_value = UserBandFactory.generate(
        member_type=MemberType.LEADER
    )

    service = SongService(song_repo, user_band_repo)
    song = await service.update_song_info(
        1, 1, "변경 타이틀", "변경 가수", status=SongStatus.INPROGRESS
    )
    assert song.in_progress_dtm is not None


@pytest.mark.asyncio
async def test_연습곡_상태_종료로_수정(song_repo, user_band_repo):
    await test_연습곡_상태_연습중으로_수정(song_repo, user_band_repo)

    service = SongService(song_repo, user_band_repo)
    song = await service.update_song_info(
        1, 1, "변경 타이틀", "변경 가수", status=SongStatus.CLOSED
    )
    assert song.closed_dtm is not None


@pytest.mark.asyncio
async def test_연습곡_상태_대기로_수정(song_repo, user_band_repo):
    await test_연습곡_상태_연습중으로_수정(song_repo, user_band_repo)

    service = SongService(song_repo, user_band_repo)
    song = await service.update_song_info(
        1, 1, "변경 타이틀", "변경 가수", status=SongStatus.PENDING
    )
    assert song.in_progress_dtm is None
    assert song.closed_dtm is None


@pytest.mark.asyncio
async def test_존재하지_않는_연습곡_정보_수정_실패(song_repo, user_band_repo):
    song_repo.find_by_id_or_none.return_value = None
    user_band_repo.find_by_user_and_band.return_value = None

    service = SongService(song_repo, user_band_repo)
    with pytest.raises(APIException) as exc:
        await service.update_song_info(1, 1, "변경 타이틀", "변경 가수")
    assert exc.value.http == Http4XX.SONG_NOT_FOUND


@pytest.mark.asyncio
async def test_가입하지_않은_밴드_연습곡_정보_수정_실패(song_repo, user_band_repo):
    song_repo.find_by_id_or_none.return_value = SongFactory.generate()
    user_band_repo.find_by_user_and_band.return_value = None

    service = SongService(song_repo, user_band_repo)
    with pytest.raises(APIException) as exc:
        await service.update_song_info(1, 1, "변경 타이틀", "변경 가수")
    assert exc.value.http == Http4XX.BAND_NOT_REGISTERED


@pytest.mark.asyncio
async def test_일반_권한으로_연습곡_정보_수정_실패(song_repo, user_band_repo):
    song_repo.find_by_id_or_none.return_value = SongFactory.generate()
    user_band_repo.find_by_user_and_band.return_value = UserBandFactory.generate(
        member_type=MemberType.NORMAL
    )

    service = SongService(song_repo, user_band_repo)
    with pytest.raises(APIException) as exc:
        await service.update_song_info(1, 1, "변경 타이틀", "변경 가수")
    assert exc.value.http == Http4XX.PERMISSION_DENIED
