from datetime import date, time
from random import randint

from fastapi import Request
from jinja2 import pass_context
from starlette.datastructures import URL


weekdays = ["월", "화", "수", "목", "금", "토", "일"]


def to_weekday(d: date) -> str:
    return weekdays[d.weekday()]


def format_time(t: time):
    return (
        f"{'오전' if t.hour < 12 else '오후'} "
        f"{t.hour if t.hour <= 12 else t.hour - 12}:{str(t.minute).zfill(2)}"
    )


@pass_context
def urlx_for(context: dict, name: str, **path_params) -> URL:
    request: Request = context["request"]
    http_url = request.url_for(name, **path_params)
    if scheme := request.headers.get("x-forwarded-proto"):
        return http_url.replace(scheme=scheme)
    return http_url


def generate_name() -> str:
    return f"name{randint(0, 100)}"
