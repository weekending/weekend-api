from typing import ClassVar, Generic, TypeVar

from pydantic import BaseModel, ConfigDict, Field


T = TypeVar("T")


class BaseResponse(BaseModel, Generic[T]):
    code: str = Field(title="코드")
    message: str = Field(title="메시지")
    data: T = Field(title="응답 데이터", default=None)


class SuccessResponse(BaseResponse):
    code: str = Field(title="코드", examples=["S000"])
    message: str = Field(title="메시지", examples=["성공"])


class CreatedResponse(BaseResponse):
    code: str = Field(title="코드", examples=["S001"])
    message: str = Field(title="메시지", examples=["생성 완료"])


class BaseErrorResponse(BaseModel):
    detail: str = Field(title="에러 메시지")

    response_extra: ClassVar[ConfigDict] = ConfigDict()

    @classmethod
    def to_openapi(cls, **kwargs) -> dict:
        kwargs.setdefault("description", cls.__doc__)
        return {
            "model": cls,
            "content": {"application/json": cls.response_extra},
            **kwargs,
        }


class UnauthenticatedResponse(BaseErrorResponse):
    """인증 실패"""

    response_extra = {
        "examples": {
            "권한이 없는 경우": {
                "value": {"detail": "잘못된 인증"}
            },
        }
    }


class PermissionDeniedResponse(BaseErrorResponse):
    """권한 없음"""

    response_extra = {
        "examples": {
            "권한이 없는 경우": {
                "value": {"detail": "권한이 없습니다."}
            },
        }
    }
