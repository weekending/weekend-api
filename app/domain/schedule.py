from datetime import date, time

from pydantic import BaseModel

from .song import Song
from .user import User


class Schedule(BaseModel):
    id: int = None
    band_id: int
    title: str
    day: date
    start_time: time | None
    end_time: time | None
    location: str | None
    memo: str | None
    is_active: bool
    songs: list[Song]
    users: list[User]
