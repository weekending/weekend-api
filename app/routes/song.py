from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from app.common.auth.schemas import JWTAuthorizationCredentials
from app.common.permission import is_authenticated
from app.schemas.song import SongInfo, SongStatusInfo
from app.service.song import SongService

router = APIRouter(prefix="/api/songs")


@router.post("")
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


@router.delete("{song_id}")
async def remove_song(
    song_id: int = 1,
    service: SongService = Depends(SongService),
) -> JSONResponse:
    """곡 제거"""
    return JSONResponse(
        content=await service.remove_song(song_id=song_id),
        status_code=200,
    )


@router.post("{song_id}/status")
async def update_song(
    body: SongStatusInfo,
    song_id: int,
    service: SongService = Depends(SongService),
) -> JSONResponse:
    """곡 상태 변경"""
    return JSONResponse(
        content=await service.update_status(song_id=song_id, song_info=body),
        status_code=200,
    )
