from pydantic import BaseModel


class BandInfo(BaseModel):
    name: str
