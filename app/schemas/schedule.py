from datetime import date, time

from pydantic import BaseModel, Field


class ScheduleInfo(BaseModel):
    band_id: int = Field(title="밴드 PK")
    day: date = Field(title="날짜", description="`YYYY-MM-DD` 형식")
    start_time: time | None = Field(
        title="시작 시간", default=None, examples=["12:00:00"]
    )
    end_time: time | None = Field(
        title="종료 시간", default=None, examples=["14:00:00"]
    )
    title: str | None = Field(title="일정 제목", default=None, examples=["합주 연습"])
    location: str | None = Field(
        title="위치", default=None, examples=["그라운드 합주실 본점 A1"]
    )
    memo: str | None = Field(
        title="메모", default=None, examples=["통기타 대여 필요해보임.."]
    )


class ScheduleResponse(BaseModel):
    id: int = Field(title="일정 PK")
    day: date
    weekday: str
    start_time: time
    end_time: time
    title: str
    location: str
    memo: str
