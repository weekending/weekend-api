from fastapi import APIRouter, Depends, Request
from starlette.templating import Jinja2Templates

from app.common.utils import urlx_for
from app.service.song import SongService

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
    service: SongService = Depends(SongService),
):
    """메인 화면"""
    return template.TemplateResponse(
        request,
        "/index.html",
        context=await service.get_group_info(group_id=group_id),
    )


@router.get("/register", include_in_schema=False)
async def register(request: Request):
    """등록 화면"""
    return template.TemplateResponse(request, "/register.html")
