from .authentication import (
    Authentication,
    CookieAuthentication,
    CookieForRedocAuthentication,
)

jwt_auth = Authentication()
cookie = CookieAuthentication()
cookie_redoc = CookieForRedocAuthentication()
