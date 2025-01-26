from datetime import datetime
from typing import Sequence, Type, TypeVar

from sqlalchemy import delete, select

from .utils import execute_query, add_to_session

T = TypeVar("T", bound="ModelMixin")


class ModelMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    async def find(cls: Type[T], *whereclause) -> Sequence[T]:
        result = await execute_query(
            select(cls).where(*whereclause).order_by(cls.id.desc())
        )
        return result.scalars().all()

    @classmethod
    async def find_one(cls: Type[T], *whereclause) -> T | None:
        result = await execute_query(select(cls).where(*whereclause))
        return result.scalar_one_or_none()

    async def save(self):
        self.updated_dtm = datetime.now()
        await add_to_session(self, commit=True)

    async def delete(self):
        await execute_query(
            delete(self.__class__).where(self.__class__.id == self.id),
            commit=True,
        )
