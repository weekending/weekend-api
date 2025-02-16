from fastapi import APIRouter, Depends, Path

from app.common.auth.schemas import JWTAuthorizationCredentials
from app.common.http import Http2XX
from app.common.permission import is_authenticated
from app.common.response import APIResponse
from app.schemas.song import (
    SongCreateValidationErrorResponse,
    SongInfo,
    SongNotFoundResponse,
    SongResponse,
    SongStatusInfo,
)
from app.schemas.base import (
    CreatedResponse,
    PermissionDeniedResponse,
    SuccessResponse,
    UnauthenticatedResponse,
)
from app.service.song import SongService

router = APIRouter(prefix="/api/songs", tags=["Song"])


@router.post(
    "",
    summary="곡 등록",
    status_code=201,
    responses={
        201: {"description": "곡 등록 성공", "model": CreatedResponse[SongResponse]},
        400: SongCreateValidationErrorResponse.to_openapi(),
        401: UnauthenticatedResponse.to_openapi(),
        403: PermissionDeniedResponse.to_openapi(),
        422: {},
    },
)
async def register_song(
    body: SongInfo,
    credential: JWTAuthorizationCredentials = Depends(is_authenticated),
    service: SongService = Depends(SongService),
) -> APIResponse:
    """곡 등록"""
    return APIResponse(
        Http2XX.CREATED,
        data=await service.create_song(body, credential.user_id),
    )


@router.delete(
    "{song_id}",
    summary="곡 제거",
    responses={
        200: {"description": "곡 제거 성공", "model": SuccessResponse},
        401: UnauthenticatedResponse.to_openapi(),
        403: PermissionDeniedResponse.to_openapi(),
        404: SongNotFoundResponse.to_openapi(),
        422: {},
    },
)
async def remove_song(
    song_id: int = Path(title="곡 PK"),
    service: SongService = Depends(SongService),
) -> APIResponse:
    """곡 제거"""
    return APIResponse(Http2XX.OK, data=await service.remove_song(song_id))


@router.post(
    "{song_id}/status",
    summary="곡 상태 변경",
    responses={
        200: {"description": "곡 상태 변경 성공", "model": SuccessResponse[SongResponse]},
        401: UnauthenticatedResponse.to_openapi(),
        403: PermissionDeniedResponse.to_openapi(),
        404: SongNotFoundResponse.to_openapi(),
        422: {},
    },
)
async def update_song(
    body: SongStatusInfo,
    song_id: int = Path(title="곡 PK"),
    service: SongService = Depends(SongService),
) -> APIResponse:
    """곡 상태 변경"""
    return APIResponse(Http2XX.OK, data=await service.update_status(song_id, body))
