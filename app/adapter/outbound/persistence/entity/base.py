from datetime import datetime
from typing import TypeVar

from pydantic import BaseModel
from sqlalchemy import Column, DateTime
from sqlalchemy.orm import DeclarativeBase

_T = TypeVar("_T")


class Base(DeclarativeBase):
    __abstract__ = True

    updated_dtm = Column(DateTime, comment="수정 일시")
    created_dtm = Column(
        DateTime, nullable=False, default=datetime.now, comment="생성 일시"
    )

    @classmethod
    def from_domain(cls: type[_T], domain: BaseModel) -> _T:
        return cls(**domain.model_dump())

    def to_domain(self, **kwargs):
        return self.__domain__(
            **{
                col: getattr(self, col)
                for col in self.__domain__.model_fields.keys()
            }
        )
