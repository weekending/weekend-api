from fastapi import APIRouter, Depends, Request
from starlette.templating import Jinja2Templates

from app.application.port.input import ScheduleUseCase
from app.application.service.schedule_service import ScheduleService
from app.common.utils import format_time, to_weekday, urlx_for

router = APIRouter(include_in_schema=False)

template = Jinja2Templates("app/adapter/inbound/web/templates/")
template.env.globals["url_for"] = urlx_for


def get_song_context(schedule, is_edit: bool = False):
    return {
        "title": schedule.title,
        "date": f'{schedule.day.strftime("%Y.%m.%d")} ({to_weekday(schedule.day)})',
        "time": f'{format_time(schedule.start_time)} ~ {format_time(schedule.end_time)}',
        "location": schedule.location,
        "user_count": len(schedule.users),
        "usernames": ", ".join([u.name for u in schedule.users]),
        "memo": schedule.memo or "",
        "is_edit": is_edit
    }


@router.get("/")
async def main(request: Request):
    """메인 화면"""
    return template.TemplateResponse(request, "/index.html")


@router.get("/login")
async def login(request: Request):
    """로그인 화면"""
    return template.TemplateResponse(request, "/login.html")


@router.get("/songs")
async def song_list(request: Request):
    """곡 리스트 화면"""
    return template.TemplateResponse(request, "/song/song.html")


@router.get("/songs/register")
async def register(request: Request):
    """곡 등록 화면"""
    return template.TemplateResponse(request, "/song/register.html")


@router.get("/schedule")
async def schedule_list(request: Request):
    """일정 리스트"""
    return template.TemplateResponse(request, "/schedule/schedule.html")


@router.get("/schedule/register")
async def register_schedule(request: Request):
    """일정 상세 수정"""
    return template.TemplateResponse(
        request,
        "/schedule/schedule-detail.html",
        context={
            "title": "일정 등록",
            "is_register": True,
            "is_edit": True,
        }
    )


@router.get("/schedule/{schedule_id}")
async def schedule_detail(
    schedule_id: int,
    request: Request,
    service: ScheduleUseCase = Depends(ScheduleService),
):
    """일정 상세"""
    schedule = await service.get_schedule_info(schedule_id)
    return template.TemplateResponse(
        request,
        "/schedule/schedule-detail.html",
        context={
            "title": schedule.title,
            "date": f'{schedule.day.strftime("%Y.%m.%d")} ({to_weekday(schedule.day)})',
            "time": f'{format_time(schedule.start_time)} ~ {format_time(schedule.end_time)}',
            "location": schedule.location,
            "user_count": len(schedule.users),
            "usernames": ", ".join([u.name for u in schedule.users]),
            "memo": schedule.memo or "",
            "is_register": False,
            "is_edit": False,
        }
    )


@router.get("/schedule/{schedule_id}/edit")
async def edit_schedule_detail(
    schedule_id: int,
    request: Request,
    service: ScheduleUseCase = Depends(ScheduleService),
):
    """일정 상세 수정"""
    schedule = await service.get_schedule_info(schedule_id)
    return template.TemplateResponse(
        request,
        "/schedule/schedule-detail.html",
        context={
            "title": schedule.title,
            "date": schedule.day.strftime("%Y-%m-%d"),
            "start_time": schedule.start_time,
            "end_time": schedule.end_time,
            "location": schedule.location,
            "user_count": len(schedule.users),
            "usernames": ", ".join([u.name for u in schedule.users]),
            "memo": schedule.memo or "",
            "is_register": False,
            "is_edit": True,
        }
    )
