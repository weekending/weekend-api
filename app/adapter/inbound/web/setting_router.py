from fastapi import APIRouter, Depends, Request
from http.cookies import SimpleCookie

from app.application.port.input import BandUseCase, UserUseCase
from app.application.service.band_service import BandService
from app.application.service.user_service import UserService
from app.common.auth.authentication import JWTAuthorizationCredentials
from app.common.permission import cookie_authenticated
from app.common.template import template

router = APIRouter()


@router.get("/settings")
async def setting(
    request: Request,
    credential: JWTAuthorizationCredentials = Depends(cookie_authenticated),
):
    """설정 화면"""
    return template.TemplateResponse(request, "/setting/setting.html")


@router.get("/settings/members")
async def setting_band_members(
    request: Request,
    credential: JWTAuthorizationCredentials = Depends(cookie_authenticated),
    service: BandUseCase = Depends(BandService),
):
    """멤버 화면"""
    cookie = SimpleCookie()
    cookie.load(request.headers.get("Cookie", ""))
    if band := cookie.get("bandId"):
        band_id = int(band.value)
    else:
        band_id = -1
    members = await service.get_band_members(band_id=band_id)
    return template.TemplateResponse(
        request, "/setting/band-member.html", context={"members": members}
    )


@router.get("/settings/profile")
async def setting_profile(
    request: Request,
    credential: JWTAuthorizationCredentials = Depends(cookie_authenticated),
    service: UserUseCase = Depends(UserService),
):
    """프로필 화면"""
    user = await service.get_user_info(credential.user_id)
    return template.TemplateResponse(
        request, "/setting/profile.html", context={"user": user}
    )
