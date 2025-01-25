from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from app.models import PermissionType
from app.schemas.auth import LoginInfo, SignupInfo
from app.service.auth import AuthService

router = APIRouter(prefix="/api/auth")


@router.post("/signup")
async def signup(
    body: SignupInfo, service: AuthService = Depends(AuthService)
) -> JSONResponse:
    """회원가입"""
    token = await service.signup(body, permission=PermissionType.LEADER)
    return JSONResponse(content={"token": token}, status_code=201)


@router.post("/login")
async def login(
    body: LoginInfo, service: AuthService = Depends(AuthService)
) -> JSONResponse:
    """로그인"""
    return JSONResponse(content={"token": await service.login(body)})
