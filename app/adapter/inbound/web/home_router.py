from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates

from app.common.utils import urlx_for

router = APIRouter(include_in_schema=False)

template = Jinja2Templates("app/adapter/inbound/web/templates/")
template.env.globals["url_for"] = urlx_for


@router.get("/")
async def main(request: Request):
    """메인 화면"""
    return template.TemplateResponse(request, "/index.html")


@router.get("/login")
async def login(request: Request):
    """로그인 화면"""
    return template.TemplateResponse(request, "/login.html")


@router.get("/songs")
async def register(request: Request):
    """곡 리스트 화면"""
    return template.TemplateResponse(request, "/song/song.html")


@router.get("/songs/register")
async def register(request: Request):
    """곡 등록 화면"""
    return template.TemplateResponse(request, "/song/register.html")
