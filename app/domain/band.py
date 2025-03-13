from pydantic import BaseModel


class Band(BaseModel):
    id: int = None
    name: str
    thumbnail: str | None
    is_active: bool


class BandLink(BaseModel):
    id: int = None
    band_id: int
    hash: str
    link_url: str | None = None
    is_active: bool
