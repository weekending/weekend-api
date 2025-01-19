from pydantic import BaseModel

from app.models.song import SongStatus


class SongInfo(BaseModel):
    title: str
    singer: str
    user_id: int | None = None


class SongStatusInfo(BaseModel):
    status: SongStatus
