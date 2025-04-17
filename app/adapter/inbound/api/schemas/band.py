from pydantic import BaseModel, Field

from app.core.settings import get_settings
from app.domain import Band, MemberType
from .base import BaseErrorResponse

settings = get_settings()


class BandInfo(BaseModel):
    name: str = Field(title="밴드명", examples=["대일밴드"])
    member_type: MemberType = Field(title="멤버 권한", default=MemberType.NORMAL)


class BandResponse(BaseModel):
    id: int = Field(title="밴드 PK")
    name: str = Field(title="밴드명", examples=["대일밴드"])
    thumbnail: str | None = Field(title="썸네일 이미지 링크")
    is_active: bool = Field(title="활성화 여부", examples=[True])

    @staticmethod
    def from_domain(band: Band) -> "BandResponse":
        return BandResponse(
            id=band.id,
            name=band.name,
            thumbnail=band.thumbnail,
            is_active=band.is_active,
        )


class BandNotFoundResponse(BaseErrorResponse):
    """찾을 수 없음"""

    response_extra = {
        "examples": {
            "밴드가 없는 경우": {
                "value": {"detail": "밴드를 찾을 수 없습니다."}
            },
        }
    }
