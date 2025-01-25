import enum

from bcrypt import checkpw, gensalt, hashpw
from sqlalchemy import Boolean, Column, Enum, ForeignKey, Integer, String

from .base import BaseModel


class PermissionType(enum.Enum):
    ADMIN = "ADMIN"
    LEADER = "LEADER"
    NORMAL = "NORMAL"
    ANONYMOUS = "ANONYMOUS"

    def is_leader(self) -> bool:
        return self == self.LEADER

    def is_admin(self) -> bool:
        return self == self.ADMIN


class User(BaseModel):
    __tablename__ = "t_user"

    id = Column(Integer, primary_key=True)
    band_id = Column(Integer, ForeignKey("t_band.id", ondelete="CASCADE"))
    name = Column(String(30), nullable=False, comment="닉네임")
    username = Column(String(16), unique=True, nullable=False, comment="아이디")
    hashed_password = Column(String(200), comment="비밀번호")
    permission = Column(
        Enum(PermissionType, native_enum=False),
        default=PermissionType.NORMAL,
        nullable=False,
        comment="사용자 권한",
    )
    is_active = Column(Boolean, default=True, nullable=False, comment="활성화 여부")

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
