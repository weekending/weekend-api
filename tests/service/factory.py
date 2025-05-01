from datetime import date, datetime, time

from bcrypt import gensalt, hashpw

from app.domain import Band, MemberType, Schedule, Song, SongStatus, User, UserBand
from app.common.auth.schemas import (
    JWTAuthorizationCredentials,
)


class BandFactory:
    @staticmethod
    def generate() -> Band:
        return Band(id=1, name="밴드", thumbnail=None, is_active=True)


class ScheduleFactory:
    @staticmethod
    def generate() -> Schedule:
        return Schedule(
            id=1,
            band_id=1,
            title="일정",
            day=date(2025, 1, 1),
            start_time=time(12, 0),
            end_time=time(14, 0),
            location="장소",
            memo="메모",
            is_active=True,
            users=[],
        )


class SongFactory:
    @staticmethod
    def generate() -> Song:
        return Song(
            id=1,
            band_id=1,
            user_id=1,
            title="타이틀",
            singer="가수",
            thumbnail=None,
            status=SongStatus.PENDING,
            is_active=True,
            created_dtm=datetime.now(),
            in_progress_dtm=None,
            closed_dtm=None,
        )


class UserBandFactory:
    @staticmethod
    def generate(member_type: MemberType = None) -> UserBand:
        return UserBand(
            id=1,
            user_id=1,
            band_id=1,
            member_type=member_type or MemberType.NORMAL,
            user=None,
        )


class UserFactory:
    @staticmethod
    def generate(password: str = None) -> User:
        return User(
            id=1,
            name="test",
            email="test@test.com",
            password=(
                hashpw(password.encode(), salt=gensalt()).decode()
                if password else ""
            ),
            is_active=True,
            is_admin=False,
        )
