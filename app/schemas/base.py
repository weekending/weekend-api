from typing import ClassVar

from pydantic import BaseModel, ConfigDict, Field


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
