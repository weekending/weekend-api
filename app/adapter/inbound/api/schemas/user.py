from pydantic import BaseModel, Field

from app.domain import Band, User


class UserInfoResponse(BaseModel):
    id: int = Field(title="밴드 PK")
    name: str = Field(title="닉네임", examples=["미민또"])
    email: str = Field(title="이메일", examples=["weekend.dev@gmail.com"])
    is_active: bool = Field(title="활성화 여부", examples=[True])

    @staticmethod
    def from_domain(user: User) -> "UserInfoResponse":
        return UserInfoResponse(
            id=user.id,
            name=user.name,
            email=user.email,
            is_active=user.is_active,
        )
