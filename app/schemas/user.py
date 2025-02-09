from pydantic import BaseModel, Field


class UserInfoResponse(BaseModel):
    id: int = Field(title="밴드 PK")
    name: str = Field(title="닉네임", examples=["미민또"])
    email: str = Field(title="이메일", examples=["weekend.dev@gmail.com"])
    is_active: bool = Field(title="활성화 여부", examples=[True])


class UserBandResponse(BaseModel):
    id: int = Field(title="밴드 PK")
    name: str = Field(title="밴드명", examples=["대일밴드"])
    thumbnail: str | None = Field(title="썸네일 이미지 링크", )
    is_active: bool = Field(title="활성화 여부", examples=[True])
