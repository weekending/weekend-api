from datetime import datetime

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    String,
    Table,
    Text,
    UniqueConstraint,
)
from sqlalchemy.orm import Mapped, relationship

from app.core.settings import get_settings
from app.domain import Band, BandLink, MemberType
from .base import Base


user_band_entity = Table(
    "t_user_band",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column(
        "user_id",
        Integer,
        ForeignKey("t_user.id", ondelete="CASCADE"),
        nullable=False,
    ),
    Column(
        "band_id",
        Integer,
        ForeignKey("t_band.id", ondelete="CASCADE"),
        nullable=False,
    ),
    Column(
        "member_type",
        Enum(MemberType, native_enum=False),
        default=MemberType.NORMAL,
        nullable=False,
        comment="멤버 권한",
    ),
    Column(
        "created_dtm",
        DateTime,
        nullable=False,
        default=datetime.now,
        comment="생성 일시",
    ),
    UniqueConstraint("band_id", "user_id"),
)


class BandEntity(Base):
    __tablename__ = "t_band"
    __domain__ = Band

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False, comment="밴드명")
    thumbnail = Column(Text, comment="썸네일 이미지")
    is_active = Column(Boolean, default=True, nullable=False, comment="활성화 여부")
    links = relationship("BandLinkEntity", back_populates="band")
    users: Mapped[list["UserEntity"]] = relationship(
        "UserEntity", secondary=user_band_entity, back_populates="bands"
    )


class BandLinkEntity(Base):
    __tablename__ = "t_band_link"
    __domain__ = BandLink

    id = Column(Integer, primary_key=True)
    band_id = Column(
        Integer, ForeignKey("t_band.id", ondelete="CASCADE"), nullable=False
    )
    band = relationship(BandEntity, back_populates="links")
    hash = Column(
        String(20),
        unique=True,
        nullable=False,
        comment="링크",
    )
    is_active = Column(Boolean, default=True, nullable=False, comment="활성화 여부")

    @property
    def link_url(self) -> str:
        settings = get_settings()
        return f"{settings.BASE_DOMAIN}/link/{self.hash}"

    @classmethod
    def from_domain( cls, band_link: BandLink) -> "BandLinkEntity":
        return cls(
            id=band_link.id,
            band_id=band_link.band_id,
            hash=band_link.hash,
            is_active=band_link.is_active,
        )
