from typing import Any

from starlette.responses import JSONResponse

from .http import BaseStatus


class APIResponse(JSONResponse):
    def __init__(self, http: BaseStatus, data: Any = None):
        super().__init__(
            content={"code": http.code, "message": http.message, "data": data},
            status_code=http.status_code,
        )
