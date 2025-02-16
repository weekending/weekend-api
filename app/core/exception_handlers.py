from starlette.requests import Request

from app.common.exception import APIException
from app.common.response import APIResponse


async def api_exception_handler(
    request: Request, exc: APIException
) -> APIResponse:
    return APIResponse(exc.http)
