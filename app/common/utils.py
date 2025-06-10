from datetime import date, datetime, time, timedelta, timezone
from random import randint

from fastapi import Request
from jinja2 import pass_context
from starlette.datastructures import URL

from app.common.http import Http4XX
from app.common.exception import APIException
from app.domain import MemberType, UserBand


weekdays = ["월", "화", "수", "목", "금", "토", "일"]


def to_weekday(d: date) -> str:
    return weekdays[d.weekday()]


def format_time(t: time):
    return (
        f"{'오전' if t.hour < 12 else '오후'} "
        f"{t.hour if t.hour <= 12 else t.hour - 12}:{str(t.minute).zfill(2)}"
    )


def format_dt(dt: datetime) -> str:
    if datetime.now().date() == dt.date():
        return dt.strftime("%H:%M")
    return dt.strftime("%Y-%m-%d")


@pass_context
def urlx_for(context: dict, name: str, **path_params) -> URL:
    request: Request = context["request"]
    http_url = request.url_for(name, **path_params)
    if scheme := request.headers.get("x-forwarded-proto"):
        return http_url.replace(scheme=scheme)
    return http_url


def generate_name() -> str:
    first = ["가지런한",  "고요한", "날카로운", "눈부신", "부드러운", "용감한", "용맹한", "지혜로운"]
    second = ["꿈속의", "들판의", "절벽의", "천국의", "초원의",  "태양의", "폭풍의", "협곡의"]
    last = ["고향", "날개", "독수리", "물고기", "별빛", "불꽃", "은하수", "향기"]
    return " ".join(
        func[randint(0, len(func) - 1)] for func in [first, second, last]
    )


def check_user_leader_permission(user_band: UserBand):
    if not user_band:
        raise APIException(Http4XX.BAND_NOT_REGISTERED)
    elif user_band.member_type != MemberType.LEADER:
        raise APIException(Http4XX.PERMISSION_DENIED)
