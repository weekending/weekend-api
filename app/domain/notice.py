from datetime import datetime

from pydantic import BaseModel


class Notice(BaseModel):
    id: int = None
    title: str
    content: str
    is_active: bool
    updated_dtm: datetime | None = None
    created_dtm: datetime
  