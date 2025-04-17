from fastapi import APIRouter, Depends, Request
from starlette.templating import Jinja2Templates

from app.application.service.schedule_service import ScheduleService
from app.application.service.song_service import SongService, SongStatus
from app.common.utils import urlx_for

router = APIRouter()

template = Jinja2Templates("app/adapter/inbound/web/templates/")
template.env.globals["url_for"] = urlx_for


@router.get("/", include_in_schema=False)
async def main(request: Request):
    """메인 화면"""
    return template.TemplateResponse(request, "/index.html")


@router.get("/login", include_in_schema=False)
async def login(request: Request):
    """로그인 화면"""
    return template.TemplateResponse(request, "/login.html")


@router.get("/register", include_in_schema=False)
async def register(request: Request):
    """등록 화면"""
    return template.TemplateResponse(request, "/register.html")


@router.get("/pick", include_in_schema=False)
async def register(
    request: Request,
    band_id: int = 1,
    song_service: SongService = Depends(SongService),
):
    """등록 화면"""
    return template.TemplateResponse(
        request, "/pick.html",
        context={
            "songs": await song_service.get_songs_by_status(
                band_id=band_id, status=SongStatus.PENDING
            ),
        }
    )
