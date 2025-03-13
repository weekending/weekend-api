from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from . import db


class BaseRepository:
    def __init__(self, session: AsyncSession = Depends(db.get_session)):
        self._session = session
