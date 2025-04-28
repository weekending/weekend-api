from fastapi import APIRouter, Request

from app.common.template import template

router = APIRouter()


@router.get("/signup")
async def signup(request: Request):
    """회원가입 화면"""
    return template.TemplateResponse(request, "/auth/signup.html")


@router.get("/login")
async def login(request: Request):
    """로그인 화면"""
    return template.TemplateResponse(request, "/auth/login.html")

