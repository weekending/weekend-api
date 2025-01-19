from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from app.service.song import SongService
from app.schemas.song import SongInfo, SongStatusInfo

router = APIRouter(prefix="/api")


@router.post("/songs")
async def register_song(
    body: SongInfo,
    group_id: int = 1,
    service: SongService = Depends(SongService),
) -> JSONResponse:
    """곡 등록"""
    return JSONResponse(
        content=await service.create_song(group_id=group_id, song_info=body),
        status_code=201,
    )


@router.delete("/songs/{song_id}")
async def remove_song(
    song_id: int = 1,
    service: SongService = Depends(SongService),
) -> JSONResponse:
    """곡 제거"""
    return JSONResponse(
        content=await service.remove_song(song_id=song_id),
        status_code=200,
    )


@router.post("/songs/{song_id}/status")
async def update_song(
    body: SongStatusInfo,
    song_id: int = 1,
    service: SongService = Depends(SongService),
) -> JSONResponse:
    """곡 상태 변경"""
    return JSONResponse(
        content=await service.update_status(song_id=song_id, song_info=body),
        status_code=200,
    )
