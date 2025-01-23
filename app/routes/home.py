from fastapi import APIRouter, Depends, Request
from starlette.templating import Jinja2Templates

from app.common.utils import urlx_for
from app.service.schedule import ScheduleService
from app.service.song import SongService, SongStatus

router = APIRouter()

template = Jinja2Templates("app/templates/")
template.env.globals["url_for"] = urlx_for


@router.get("/healthcheck", include_in_schema=False)
def healthcheck() -> str:
    return "ok"


@router.get("/", include_in_schema=False)
async def main(
    request: Request,
    group_id: int = 1,
    song_service: SongService = Depends(SongService),
    schedule_service: ScheduleService = Depends(ScheduleService),
):
    """메인 화면"""
    return template.TemplateResponse(
        request,
        "/index.html",
        context={
            "is_login": False,
            "schedules": await schedule_service.get_schedules(group_id=group_id),
            **await song_service.get_group_info(group_id=group_id),
        },
    )


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
    group_id: int = 1,
    song_service: SongService = Depends(SongService),
):
    """등록 화면"""
    return template.TemplateResponse(
        request, "/pick.html",
        context={
            "songs": await song_service.get_songs_by_status(
                group_id=group_id, status=SongStatus.PENDING
            ),
        }
    )
