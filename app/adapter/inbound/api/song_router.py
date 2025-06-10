from fastapi import APIRouter, Depends, Path, Query

from app.application.port.input import SongUseCase
from app.application.service.song_service import SongService
from app.common.auth.schemas import JWTAuthorizationCredentials
from app.common.http import Http2XX
from app.common.permission import is_authenticated
from app.common.response import APIResponse
from app.domain.song import SongStatus
from .schemas.song import (
    SongCreateValidationErrorResponse,
    SongInfo,
    SongNotFoundResponse,
    SongResponse,
    SongUpdateInfo,
)
from .schemas.base import (
    CreatedResponse,
    PermissionDeniedResponse,
    SuccessResponse,
    UnauthenticatedResponse,
)

router = APIRouter(prefix="/songs", tags=["Song"])


@router.get(
    "",
    summary="곡 목록 조회",
    status_code=200,
    responses={
        200: {"description": "곡 목록 조회 성공", "model": SuccessResponse[SongResponse]},
        400: SongCreateValidationErrorResponse.to_openapi(),
        401: UnauthenticatedResponse.to_openapi(),
        403: PermissionDeniedResponse.to_openapi(),
        422: {},
    },
)
async def song_list(
    band_id: int = Query(title="밴드 PK"),
    status: SongStatus = None,
    # credential: JWTAuthorizationCredentials = Depends(is_authenticated),
    service: SongUseCase = Depends(SongService),
) -> APIResponse:
    """곡 목록 조회"""
    songs = await service.get_song_list(-1, band_id, status)
    return APIResponse(
        Http2XX.OK, data=[SongResponse.from_domain(song) for song in songs]
    )


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
    service: SongUseCase = Depends(SongService),
) -> APIResponse:
    """곡 등록"""
    song = await service.create_song(credential.user_id, **body.model_dump())
    return APIResponse(Http2XX.CREATED, data=SongResponse.from_domain(song))


@router.get(
    "/{song_id}",
    summary="곡 정보 조회",
    responses={
        200: {"description": "곡 조회 성공", "model": SuccessResponse[SongResponse]},
        401: UnauthenticatedResponse.to_openapi(),
        403: PermissionDeniedResponse.to_openapi(),
        404: SongNotFoundResponse.to_openapi(),
        422: {},
    },
)
async def get_song_info(
    song_id: int = Path(title="곡 PK"),
    # credential: JWTAuthorizationCredentials = Depends(is_authenticated),
    service: SongUseCase = Depends(SongService),
) -> APIResponse:
    """곡 조회"""
    song = await service.get_song_info(song_id)
    return APIResponse(Http2XX.OK, data=SongResponse.from_domain(song))


@router.delete(
    "/{song_id}",
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
    credential: JWTAuthorizationCredentials = Depends(is_authenticated),
    service: SongUseCase = Depends(SongService),
) -> APIResponse:
    """곡 제거"""
    return APIResponse(
        Http2XX.OK, data=await service.remove_song(song_id, credential.user_id)
    )


@router.patch(
    "/{song_id}",
    summary="곡 정보 변경",
    responses={
        200: {"description": "곡 정보 변경 성공", "model": SuccessResponse[SongResponse]},
        401: UnauthenticatedResponse.to_openapi(),
        403: PermissionDeniedResponse.to_openapi(),
        404: SongNotFoundResponse.to_openapi(),
        422: {},
    },
)
async def update_song(
    body: SongUpdateInfo,
    song_id: int = Path(title="곡 PK"),
    credential: JWTAuthorizationCredentials = Depends(is_authenticated),
    service: SongUseCase = Depends(SongService),
) -> APIResponse:
    """곡 정보 변경"""
    song = await service.update_song_info(
        song_id, credential.user_id, **body.model_dump()
    )
    return APIResponse(Http2XX.OK, data=SongResponse.from_domain(song))
