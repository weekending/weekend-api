from fastapi import APIRouter, Depends, Path, Query

from app.application.port.input import PlaylistUseCase
from app.application.service.playlist_service import PlaylistService
from app.common.auth.schemas import JWTAuthorizationCredentials
from app.common.http import Http2XX
from app.common.permission import is_authenticated
from app.common.response import APIResponse
from .schemas.playlist import (
    PlaylistCreateBody,
    PlaylistDetailResponse,
    PlaylistNotFoundResponse,
    PlaylistResponse,
)
from .schemas.base import (
    CreatedResponse,
    PermissionDeniedResponse,
    SuccessResponse,
    UnauthenticatedResponse,
)

router = APIRouter(prefix="/playlists", tags=["Playlist"])


@router.get(
    "",
    summary="플레이리스트 목록 조회",
    status_code=200,
    responses={
        200: {
            "description": "플레이리스트 목록 조회 성공",
            "model": SuccessResponse[PlaylistResponse],
        },
        422: {},
    },
)
async def playlist_list(
    band_id: int = Query(title="밴드 PK"),
    page: int = Query(1, title="페이지 번호"),
    size: int = Query(10, title="페이지 사이즈"),
    service: PlaylistUseCase = Depends(PlaylistService),
) -> APIResponse:
    """플레이리스트 목록 조회"""
    playlists = await service.get_playlist_list(band_id, page, size)
    return APIResponse(
        Http2XX.OK,
        data=[PlaylistResponse.from_domain(p) for p in playlists],
    )


@router.post(
    "",
    summary="플레이리스트 생성",
    status_code=201,
    responses={
        201: {
            "description": "플레이리스트 생성 성공",
            "model": CreatedResponse[PlaylistResponse],
        },
        401: UnauthenticatedResponse.to_openapi(),
        403: PermissionDeniedResponse.to_openapi(),
        422: {},
    },
)
async def create_playlist(
    body: PlaylistCreateBody,
    credential: JWTAuthorizationCredentials = Depends(is_authenticated),
    service: PlaylistUseCase = Depends(PlaylistService),
) -> APIResponse:
    """플레이리스트 생성"""
    playlist = await service.create_playlist(
        credential.user_id, **body.model_dump()
    )
    return APIResponse(Http2XX.CREATED, data=PlaylistResponse.from_domain(playlist))


@router.get(
    "/{playlist_id}",
    summary="플레이리스트 상세 조회",
    responses={
        200: {
            "description": "플레이리스트 조회 성공",
            "model": SuccessResponse[PlaylistDetailResponse],
        },
        404: PlaylistNotFoundResponse.to_openapi(),
        422: {},
    },
)
async def get_playlist_info(
    playlist_id: int = Path(title="플레이리스트 PK"),
    service: PlaylistUseCase = Depends(PlaylistService),
) -> APIResponse:
    """플레이리스트 상세 조회"""
    playlist = await service.get_playlist_info(playlist_id)
    return APIResponse(
        Http2XX.OK, data=PlaylistDetailResponse.from_domain(playlist)
    )
