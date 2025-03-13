from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import Mapped, relationship

from app.domain import User
from .band import BandModel, user_band_model
from .base import BaseModel


class UserModel(BaseModel):
    __tablename__ = "t_user"

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False, comment="닉네임")
    email = Column(String(255), unique=True, nullable=False, comment="이메일")
    hashed_password = Column(String(200), comment="비밀번호")
    is_active = Column(Boolean, default=True, nullable=False, comment="활성화 여부")
    is_admin = Column(Boolean, default=False, nullable=False, comment="어드민 여부")
    bands: Mapped[list[BandModel]] = relationship(
        BandModel, secondary=user_band_model, back_populates="users"
    )

    @staticmethod
    def from_domain(user: User) -> "UserModel":
        return UserModel(
            id=user.id,
            name=user.name,
            email=user.email,
            hashed_password=user.password,
            is_active=user.is_active,
            is_admin=user.is_admin,
        )

    def to_domain(self) -> User:
        return User(
            id=self.id,
            name=self.name,
            email=self.email,
            password=self.hashed_password,
            is_active=self.is_active,
            is_admin=self.is_admin,
        )
