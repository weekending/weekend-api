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
from .base import Model


user_band_model = Table(
    "t_user_band",
    Model.metadata,
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


class BandModel(Model):
    __tablename__ = "t_band"

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False, comment="밴드명")
    thumbnail = Column(Text, comment="썸네일 이미지")
    is_active = Column(Boolean, default=True, nullable=False, comment="활성화 여부")
    links = relationship("BandLinkModel", back_populates="band")
    users: Mapped[list["UserModel"]] = relationship(
        "UserModel", secondary=user_band_model, back_populates="bands"
    )

    @staticmethod
    def from_domain(band: Band) -> "BandModel":
        return BandModel(
            id=band.id,
            name=band.name,
            thumbnail=band.thumbnail,
            is_active=band.is_active,
        )

    def to_domain(self) -> Band:
        return Band(
            id=self.id,
            name=self.name,
            thumbnail=self.thumbnail,
            is_active=self.is_active,
        )


class BandLinkModel(Model):
    __tablename__ = "t_band_link"

    id = Column(Integer, primary_key=True)
    band_id = Column(
        Integer, ForeignKey("t_band.id", ondelete="CASCADE"), nullable=False
    )
    band = relationship(BandModel, back_populates="links")
    hash = Column(
        String(20),
        unique=True,
        nullable=False,
        comment="링크",
    )
    is_active = Column(Boolean, default=True, nullable=False, comment="활성화 여부")

    @staticmethod
    def from_domain(band_link: BandLink) -> "BandLinkModel":
        return BandLinkModel(
            id=band_link.id,
            band_id=band_link.band_id,
            hash=band_link.hash,
            is_active=band_link.is_active,
        )

    def to_domain(self) -> BandLink:
        return BandLink(
            id=self.id,
            band_id=self.band_id,
            hash=self.hash,
            link_url=self.link_url,
            is_active=self.is_active,
        )

    @property
    def link_url(self) -> str:
        settings = get_settings()
        return f"{settings.BASE_DOMAIN}/link/{self.hash}"
