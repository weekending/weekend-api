from fastapi import APIRouter, Request

from app.common.template import template

router = APIRouter()


@router.get("/")
async def main(request: Request):
    """메인 화면"""
    return template.TemplateResponse(request, "/index.html")
