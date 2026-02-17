from datetime import datetime

from pydantic import BaseModel, Field

from app.domain.playlist import Playlist
from .base import BaseErrorResponse
from .song import SongResponse


class PlaylistCreateBody(BaseModel):
    band_id: int = Field(title="밴드 PK")
    title: str = Field(title="플레이리스트 제목", examples=["공연 셋리스트"])
    description: str | None = Field(default=None, title="설명", examples=["2월 공연 셋리스트"])


class PlaylistResponse(BaseModel):
    id: int = Field(title="플레이리스트 PK")
    title: str = Field(title="제목")
    description: str | None = Field(title="설명")
    thumbnail: str | None = Field(title="썸네일 이미지")
    is_active: bool = Field(title="활성화 여부")
    created_dtm: datetime = Field(title="생성 일시")
    updated_dtm: datetime | None = Field(title="수정 일시")

    @staticmethod
    def from_domain(playlist: Playlist) -> "PlaylistResponse":
        return PlaylistResponse(
            id=playlist.id,
            title=playlist.title,
            description=playlist.description,
            thumbnail=playlist.thumbnail,
            is_active=playlist.is_active,
            created_dtm=playlist.created_dtm,
            updated_dtm=playlist.updated_dtm,
        )


class PlaylistDetailResponse(PlaylistResponse):
    songs: list[SongResponse] = Field(title="곡 목록")

    @staticmethod
    def from_domain(playlist: Playlist) -> "PlaylistDetailResponse":
        return PlaylistDetailResponse(
            id=playlist.id,
            title=playlist.title,
            description=playlist.description,
            thumbnail=playlist.thumbnail,
            is_active=playlist.is_active,
            songs=[SongResponse.from_domain(s) for s in playlist.songs],
            created_dtm=playlist.created_dtm,
            updated_dtm=playlist.updated_dtm,
        )


class PlaylistNotFoundResponse(BaseErrorResponse):
    """찾을 수 없음"""

    response_extra = {
        "examples": {
            "플레이리스트가 없는 경우": {
                "value": {"detail": "플레이리스트를 찾을 수 없습니다."}
            },
        }
    }
