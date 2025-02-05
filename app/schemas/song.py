from datetime import datetime

from pydantic import BaseModel, Field

from app.models import SongStatus
from .base import BaseErrorResponse


class SongInfo(BaseModel):
    title: str = Field(title="곡 제목", examples=["밥편지"])
    singer: str = Field(title="가수", examples=["아이유"])


class SongStatusInfo(BaseModel):
    status: SongStatus


class SongResponse(BaseModel):
    id: int = Field(title="곡 PK")
    title: str = Field(title="곡 제목", examples=["밥편지"])
    singer: str = Field(title="가수", examples=["아이유"])
    status: SongStatus
    created_dtm: datetime = Field(title="곡 등록 일시")
    in_progress_dtm: datetime = Field(title="연습 시작 일시")
    closed_dtm: datetime = Field(title="종료 처리 일시")


class SongCreateValidationErrorResponse(BaseErrorResponse):
    """파라미터 에러"""

    response_extra = {
        "examples": {
            "아이디가 중복된 경우": {
                "value": {"detail": "중복된 아이디 입니다"}
            }
        }
    }


class SongNotFoundResponse(BaseErrorResponse):
    """찾을 수 없음"""

    response_extra = {
        "examples": {
            "곡이 없는 경우": {
                "value": {"detail": "곡을 찾을 수 없습니다."}
            },
        }
    }

