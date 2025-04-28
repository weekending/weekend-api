from fastapi import APIRouter, Depends, Request

from app.application.port.input import SongUseCase
from app.application.service.song_service import SongService
from app.common.auth.authentication import JWTAuthorizationCredentials
from app.common.permission import cookie_authenticated
from app.common.template import template
from app.domain.song import SongStatus

router = APIRouter(prefix="/songs")


@router.get("")
async def song_list(request: Request):
    """곡 리스트"""
    return template.TemplateResponse(request, "/song/song.html")


@router.get("/register")
async def register_song(
    request: Request,
    credential: JWTAuthorizationCredentials = Depends(cookie_authenticated),
):
    """곡 등록"""
    return template.TemplateResponse(
        request,
        "/song/song-detail.html",
        context={"nav_title": "연습곡 등록", "is_register": True, "is_edit": True},
    )


@router.get("/{song_id}")
async def song_detail(
    song_id: int,
    request: Request,
    service: SongUseCase = Depends(SongService),
):
    """곡 상세"""
    song = await service.get_song_info(song_id)
    return template.TemplateResponse(
        request,
        "/song/song-detail.html",
        context={
            "title": song.title,
            "singer": song.singer,
            "thumbnail": song.thumbnail,
            "status": song.status,
            "created_dtm": song.created_dtm.strftime("%Y.%m.%d"),
            "in_progress_dtm": (
                song.in_progress_dtm.strftime("%Y.%m.%d")
                if song.in_progress_dtm
                else "-"
            ),
            "closed_dtm": (
                song.closed_dtm.strftime("%Y.%m.%d")
                if song.closed_dtm
                else "-"
            ),
            "is_edit": False,
        },
    )


@router.get("/{song_id}/edit")
async def song_detail(
    song_id: int,
    request: Request,
    credential: JWTAuthorizationCredentials = Depends(cookie_authenticated),
    service: SongUseCase = Depends(SongService),
):
    """곡 상세"""
    song = await service.get_song_info(song_id)
    return template.TemplateResponse(
        request,
        "/song/song-detail.html",
        context={
            "title": song.title,
            "singer": song.singer,
            "thumbnail": song.thumbnail,
            "status": song.status,
            "status_list": list(SongStatus),
            "is_edit": True,
        },
    )
