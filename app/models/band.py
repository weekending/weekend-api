from typing import Union
from uuid import uuid4

from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    ScalarResult,
    String,
    Text,
    select,
)
from sqlalchemy.orm import Mapped, relationship, selectinload

from app.core.database import execute_query
from app.core.settings import get_settings
from .base import BaseModel
from .user import User, band_user


def generate_hash() -> str:
    return uuid4().hex[:18]


class Band(BaseModel):
    __tablename__ = "t_band"

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False, comment="밴드명")
    thumbnail = Column(Text, comment="썸네일 이미지")
    is_active = Column(Boolean, default=True, nullable=False, comment="활성화 여부")
    links = relationship("BandLink", back_populates="band")
    users: Mapped[list[User]] = relationship(User, secondary=band_user, back_populates="bands")

    @classmethod
    async def find_one(cls, *whereclause) -> Union["Band", None]:
        result = await execute_query(
            select(cls)
            .options(selectinload(cls.links))
            .where(*whereclause)
        )
        return result.scalar_one_or_none()

    @classmethod
    async def find_user_bands(cls, user_id: int) -> ScalarResult["Band"]:
        result = await execute_query(
            select(cls)
            .select_from(band_user.join(cls, band_user.c.band_id == cls.id))
            .where(band_user.c.user_id == user_id)
        )
        return result.scalars()

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
