import enum

from sqlalchemy import (
    Boolean,
    Column,
    Enum,
    ForeignKey,
    Integer,
    String,
    Text,
)

from .base import BaseModel


class PermissionType(enum.Enum):
    ADMIN = "ADMIN"
    LEADER = "LEADER"
    NORMAL = "NORMAL"
    ANONYMOUS = "ANONYMOUS"

    def is_admin(self) -> bool:
        return self == self.ADMIN


class User(BaseModel):
    __tablename__ = "t_user"

    id = Column(Integer, primary_key=True)
    group_id = Column(Integer, ForeignKey("t_group.id", ondelete="CASCADE"))
    name = Column(String(30), comment="이름", nullable=False)
    password = Column(String(200), comment="비밀번호")
    permission = Column(
        Enum(PermissionType, native_enum=False),
        comment="사용자 권한",
        nullable=False,
        default=PermissionType.NORMAL,
    )
    is_active = Column(Boolean, comment="활성화 여부", nullable=False, default=True)


class Group(BaseModel):
    __tablename__ = "t_group"

    id = Column(Integer, primary_key=True)
    name = Column(String(30), comment="그룹명", nullable=False)
    thumbnail = Column(Text, comment="썸네일 이미지")
    is_active = Column(Boolean, comment="활성화 여부", nullable=False, default=True)
