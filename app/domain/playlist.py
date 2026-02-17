from datetime import datetime

from pydantic import BaseModel

from .song import Song


class Playlist(BaseModel):
    id: int = None
    band_id: int
    title: str
    description: str | None
    thumbnail: str | None
    is_active: bool
    songs: list[Song]
    created_dtm: datetime
    updated_dtm: datetime | None
