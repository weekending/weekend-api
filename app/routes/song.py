from fastapi import APIRouter, Depends, Path
from fastapi.responses import JSONResponse

from app.common.auth.schemas import JWTAuthorizationCredentials
from app.common.permission import is_authenticated
from app.schemas.song import (
    SongCreateValidationErrorResponse,
    SongInfo,
    SongNotFoundResponse,
    SongResponse,
    SongStatusInfo,
)
from app.schemas.base import PermissionDeniedResponse, UnauthenticatedResponse
from app.service.song import SongService

router = APIRouter(prefix="/api/songs", tags=["Song"])


@router.post(
    "",
    summary="곡 등록",
    status_code=201,
    responses={
        201: {"description": "곡 등록 성공", "model": SongResponse},
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
) -> JSONResponse:
    """곡 등록"""
    return JSONResponse(
        content=await service.create_song(body, credential.user_id),
        status_code=201,
    )


@router.delete(
    "{song_id}",
    summary="곡 제거",
    responses={
        200: {"description": "곡 제거 성공"},
        401: UnauthenticatedResponse.to_openapi(),
        403: PermissionDeniedResponse.to_openapi(),
        404: SongNotFoundResponse.to_openapi(),
        422: {},
    },
)
async def remove_song(
    song_id: int = Path(title="곡 PK"),
    service: SongService = Depends(SongService),
) -> JSONResponse:
    """곡 제거"""
    return JSONResponse(
        content=await service.remove_song(song_id=song_id),
        status_code=200,
    )


@router.post(
    "{song_id}/status",
    summary="곡 상태 변경",
    responses={
        200: {"description": "곡 상태 변경 성공", "model": SongResponse},
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
) -> JSONResponse:
    """곡 상태 변경"""
    return JSONResponse(
        content=await service.update_status(song_id=song_id, song_info=body),
        status_code=200,
    )
