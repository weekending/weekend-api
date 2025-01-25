from typing import Union
from uuid import uuid4

from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
    Text,
    select,
)
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import relationship, selectinload

from app.core.settings import get_settings
from .base import BaseModel, include_session


def generate_hash() -> str:
    return uuid4().hex[:18]


class Band(BaseModel):
    __tablename__ = "t_band"

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False, comment="밴드명")
    thumbnail = Column(Text, comment="썸네일 이미지")
    is_active = Column(Boolean, default=True, nullable=False, comment="활성화 여부")
    links = relationship("BandLink", back_populates="band")

    @classmethod
    @include_session
    async def find_one(
        cls,
        *whereclause,
        session: AsyncSession = None,
    ) -> Union["Band", None]:
        result = await session.execute(
            select(cls)
            .options(selectinload(cls.links))
            .where(*whereclause)
        )
        return result.scalar_one_or_none()

    @property
    def link_url(self) -> str | None:
        for link in self.links:
            return link.link_url
        return None

    def to_dict(self, **kwargs) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "thumbnail": self.thumbnail,
            "is_active": self.is_active,
            **kwargs
        }


class BandLink(BaseModel):
    __tablename__ = "t_band_link"

    id = Column(Integer, primary_key=True)
    band_id = Column(
        Integer, ForeignKey("t_band.id", ondelete="CASCADE"), nullable=False
    )
    band = relationship(Band, back_populates="links")
    hash = Column(
        String(20),
        default=generate_hash,
        unique=True,
        nullable=False,
        comment="링크",
    )
    is_active = Column(Boolean, default=True, nullable=False, comment="활성화 여부")

    @property
    def link_url(self) -> str:
        settings = get_settings()
        return f"{settings.BASE_DOMAIN}/link/{self.hash}"
