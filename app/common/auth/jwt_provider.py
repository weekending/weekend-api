from datetime import datetime, timedelta, timezone

from fastapi import Depends
from jwt import decode, encode

from app.core.settings import Settings, get_settings
from app.models import User


class JWTProvider:
    """JWT 토큰 관리"""

    ALGORITHM = "HS256"
    JWT_EXPIRATION_INTERVAL = timedelta(hours=12)

    def __init__(self, settings: Settings = Depends(get_settings)):
        self.secret_key = settings.SECRET_KEY

    def encode_token(self, user: User) -> str:
        now = datetime.now(tz=timezone.utc)
        payload = {
            "user_id": user.id,
            "email": user.email,
            "exp": (now + self.JWT_EXPIRATION_INTERVAL).timestamp(),
            "iat": now.timestamp(),
        }
        return encode(
            payload=payload, key=self.secret_key, algorithm=self.ALGORITHM
        )

    def decode_token(self, token: str) -> dict:
        return decode(jwt=token, key=self.secret_key, algorithms=self.ALGORITHM)
