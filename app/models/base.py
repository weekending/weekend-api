from datetime import datetime
from typing import Sequence, Type, TypeVar

from sqlalchemy import Column, DateTime, delete, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import declarative_base

from app.core.database import db

T = TypeVar("T", bound="BaseModel")


def include_session(func):
    async def wrapper(*args, **kwargs):
        if "session" in kwargs:
            return await func(*args, **kwargs)

        async with db.get_session() as session:
            return await func(*args, session=session, **kwargs)
    return wrapper


Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True

    updated_dtm = Column(DateTime, comment="수정 일시")
    created_dtm = Column(
        DateTime, comment="생성 일시", nullable=False, default=datetime.now
    )

    @classmethod
    @include_session
    async def find(
        cls: Type[T],
        *whereclause,
        session: AsyncSession = None,
    ) -> Sequence[T]:
        query = select(cls).where(*whereclause).order_by(cls.id.desc())
        result = await session.execute(query)
        return result.scalars().all()

    @classmethod
    @include_session
    async def find_one(
        cls: Type[T],
        *whereclause,
        session: AsyncSession = None,
    ) -> T | None:
        result = await session.execute(select(cls).where(*whereclause))
        return result.scalar_one_or_none()

    @include_session
    async def save(self, session: AsyncSession = None):
        self.updated_dtm = datetime.now()
        session.add(self)
        await session.commit()

    @include_session
    async def delete(self, session: AsyncSession = None):
        query = delete(self.__class__).where(self.__class__.id == self.id)
        await session.execute(query)
        await session.commit()
