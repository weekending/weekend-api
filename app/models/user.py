import enum

from bcrypt import checkpw, gensalt, hashpw
from sqlalchemy import (
    Boolean,
    Column,
    Enum,
    ForeignKey,
    Integer,
    String,
    Table,
    UniqueConstraint,
    insert,
)
from sqlalchemy.orm import Mapped, relationship

from app.core.database.mixin import execute_query
from .base import BaseModel


class MemberType(enum.Enum):
    LEADER = "LEADER"
    NORMAL = "NORMAL"

    def is_leader(self) -> bool:
        return self == self.LEADER


band_user = Table(
    "t_band_user",
    BaseModel.metadata,
    Column(
        "band_id",
        Integer,
        ForeignKey("t_band.id", ondelete="CASCADE"),
        nullable=False,
    ),
    Column(
        "user_id",
        Integer,
        ForeignKey("t_user.id", ondelete="CASCADE"),
        nullable=False,
    ),
    Column(
        "member_type",
        Enum(MemberType, native_enum=False),
        default=MemberType.NORMAL,
        nullable=False,
        comment="멤버 권한",
    ),
    UniqueConstraint("band_id", "user_id"),
)


class User(BaseModel):
    __tablename__ = "t_user"

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False, comment="닉네임")
    email = Column(String(255), unique=True, nullable=False, comment="이메일")
    hashed_password = Column(String(200), comment="비밀번호")
    is_active = Column(Boolean, default=True, nullable=False, comment="활성화 여부")
    is_admin = Column(Boolean, default=False, nullable=False, comment="어드민 여부")
    bands: Mapped[list["Band"]] = relationship(
        "Band", secondary=band_user, back_populates="users"
    )

    @property
    def password(self):
        raise AttributeError("비밀번호를 가져올 수 없습니다.")

    @password.setter
    def password(self, password: str):
        self.hashed_password = hashpw(
            password=password.encode(), salt=gensalt()
        ).decode()

    def check_password(self, password: str) -> bool:
        return checkpw(password.encode(), self.hashed_password.encode())

    async def append_band(
        self, band_id: int, member_type: MemberType=MemberType.NORMAL
    ):
        await execute_query(
            insert(band_user).values(
                user_id=self.id, band_id=band_id, member_type=member_type
            ),
            commit=True,
        )

    def to_dict(self, **kwargs) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "is_active": self.is_active,
            **kwargs,
        }
