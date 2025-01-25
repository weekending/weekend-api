from datetime import date, time

from pydantic import BaseModel


class ScheduleInfo(BaseModel):
    date: date
    start_time: time | None = None
    end_time: time | None = None
    title: str | None = None
    location: str | None = None
    memo: str | None = None
