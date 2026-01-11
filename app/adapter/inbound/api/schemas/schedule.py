from datetime import date, time

from pydantic import BaseModel, Field

from app.common.utils import to_weekday
from app.domain import Schedule
from .song import SongResponse
from .user import UserInfoResponse


class ScheduleInfo(BaseModel):
    band_id: int = Field(title="밴드 PK")
    title: str = Field(title="일정 제목", examples=["합주 연습"])
    day: date = Field(title="날짜", description="`YYYY-MM-DD` 형식")
    start_time: time | None = Field(
        title="시작 시간", default=None, examples=["12:00:00"]
    )
    end_time: time | None = Field(
        title="종료 시간", default=None, examples=["14:00:00"]
    )
    location: str | None = Field(
        default=None, title="위치", examples=["그라운드 합주실 본점 A1"]
    )
    memo: str | None = Field(
        default=None, title="메모", examples=["통기타 대여 필요해보임.."]
    )
    songs: list = Field(default_factory=list, title="곡 리스트")


class ScheduleUpdateInfo(BaseModel):
    title: str | None = Field(default=None, title="일정 제목", examples=["합주 연습"])
    day: date | None = Field(default=None, title="날짜", description="`YYYY-MM-DD` 형식")
    start_time: time | None = Field(
        default=None, title="시작 시간", examples=["12:00:00"]
    )
    end_time: time | None = Field(
        default=None, title="종료 시간", examples=["14:00:00"]
    )
    location: str | None = Field(
        default=None, title="위치", examples=["그라운드 합주실 본점 A1"]
    )
    memo: str | None = Field(
        default=None, title="메모", examples=["통기타 대여 필요해보임.."]
    )


class ScheduleResponse(BaseModel):
    id: int = Field(title="일정 PK")
    day: date
    weekday: str
    start_time: time | None
    end_time: time | None
    title: str
    location: str | None
    memo: str | None
    songs: list[SongResponse]
    users: list[UserInfoResponse]

    @staticmethod
    def from_domain(schedule: Schedule) -> "ScheduleResponse":
        return ScheduleResponse(
            id=schedule.id,
            day=schedule.day,
            weekday=to_weekday(schedule.day),
            start_time=schedule.start_time,
            end_time=schedule.end_time,
            title=schedule.title,
            location=schedule.location,
            memo=schedule.memo,
            songs=[SongResponse.from_domain(song) for song in schedule.songs],
            users=[UserInfoResponse.from_domain(user) for user in schedule.users],
        )
