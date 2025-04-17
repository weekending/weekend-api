from fastapi import APIRouter, Depends, Request
from fastapi.openapi.docs import get_redoc_html
from starlette.exceptions import HTTPException
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from app.application.port.input import UserUseCase
from app.application.service.user_service import UserService
from app.common.auth import cookie
from app.common.auth.schemas import JWTAuthorizationCredentials
from app.common.utils import urlx_for

router = APIRouter()

template = Jinja2Templates("app/adapter/inbound/web/templates/")
template.env.globals["url_for"] = urlx_for


@router.get("/docs", include_in_schema=False)
async def redoc_html(
    credentials: JWTAuthorizationCredentials = Depends(cookie),
    service: UserUseCase = Depends(UserService),
) -> HTMLResponse:
    """API 문서"""
    user = await service.get_user_info(credentials.user_id)
    if not user or not user.is_admin:
        raise HTTPException(status_code=302, headers={"Location": "/docs/login"})
    return get_redoc_html(openapi_url="/openapi.json", title="윅엔드")


@router.get("/docs/login", include_in_schema=False)
async def redoc_login(request: Request) -> HTMLResponse:
    """API 문서 로그인"""
    return template.TemplateResponse("/document.html", {"request": request})
