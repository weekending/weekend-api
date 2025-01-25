from pydantic import BaseModel

from app.models import SongStatus


class SongInfo(BaseModel):
    title: str
    singer: str


class SongStatusInfo(BaseModel):
    status: SongStatus
