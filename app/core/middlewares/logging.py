import logging
from uuid import uuid4

from starlette.types import ASGIApp, Message, Receive, Scope, Send

logger = logging.getLogger("fastapi.request")


class LoggingMiddleware:
    def __init__(self, app: ASGIApp):
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send):
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        request_logging_msg = self._parse_logging_message(scope)
        logger.info(request_logging_msg)

        async def send_before_logging(message: Message):
            nonlocal request_logging_msg
            await send(message)
            if message["type"] == "http.response.start":
                logger.info(f"{request_logging_msg} - {message["status"]}")

        await self.app(scope, receive, send_before_logging)

    def _parse_logging_message(self, scope: Scope) -> str:
        query = f"?{scope["query_string"].decode()}" if scope.get("query_string") else ""
        return f"{uuid4().hex[:5]} - {scope["method"]} {scope["path"]}{query}"
