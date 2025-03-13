from datetime import date, time

from pydantic import BaseModel

from .user import User


class Schedule(BaseModel):
    id: int = None
    band_id: int
    day: date
    start_time: time | None
    end_time: time | None
    title: str | None
    location: str | None
    memo: str | None
    is_active: bool
    users: list[User]
