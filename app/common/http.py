from enum import Enum

from starlette.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
    HTTP_403_FORBIDDEN,
    HTTP_404_NOT_FOUND,
    HTTP_422_UNPROCESSABLE_ENTITY,
    HTTP_500_INTERNAL_SERVER_ERROR,
)


class BaseStatus(Enum):
    def __init__(self, code: str, message: str, status_code: int):
        self.code = code
        self.message = message
        self.status_code = status_code


class Http2XX(BaseStatus):
    OK = ("S000", "성공", HTTP_200_OK)
    CREATED = ("S001", "생성 완료", HTTP_201_CREATED)


class Http4XX(BaseStatus):
    BAD_REQUEST = ("F000", "유효하지 않은 요청입니다.", HTTP_400_BAD_REQUEST)
    UNAUTHENTICATED = ("F001", "인증 실패.", HTTP_401_UNAUTHORIZED)
    PERMISSION_DENIED = ("F002", "권한이 없습니다.", HTTP_403_FORBIDDEN)
    INVALID_PARAMETER = ("F003", "유효하지 않은 파라미터입니다.", HTTP_422_UNPROCESSABLE_ENTITY)
    DUPLICATED_EMAIL = ("F004", "이미 사용중인 이메일입니다.", HTTP_422_UNPROCESSABLE_ENTITY)
    PASSWORD_MISMATCHED = ("F005", "패스워드가 서로 일치하지 않습니다.", HTTP_422_UNPROCESSABLE_ENTITY)
    AUTHENTICATION_FAILED = ("F006", "이메일 혹은 비밀번호가 일치하지 않습니다.", HTTP_422_UNPROCESSABLE_ENTITY)
    BAND_NOT_FOUND = ("F007", "밴드를 찾을 수 없습니다.", HTTP_404_NOT_FOUND)
    SONG_NOT_FOUND = ("F008", "연습곡을 찾을 수 없습니다.", HTTP_404_NOT_FOUND)
    USER_NOT_FOUND = ("F009", "사용자를 찾을 수 없습니다.", HTTP_404_NOT_FOUND)
    BAND_NOT_REGISTERED = ("F010", "가입하지 않은 밴드입니다.", HTTP_422_UNPROCESSABLE_ENTITY)
    SCHEDULE_NOT_FOUND = ("F011", "일정을 찾을 수 없습니다.", HTTP_404_NOT_FOUND)
    POST_NOT_FOUND = ("F012", "게시물을 찾을 수 없습니다.", HTTP_404_NOT_FOUND)
    INACTIVE_POST = ("F013", "비활성화된 게시물입니다.", HTTP_422_UNPROCESSABLE_ENTITY)
    CATEGORY_NOT_FOUND = ("F014", "카테고리를 찾을 수 없습니다.", HTTP_404_NOT_FOUND)
    ALREADY_PARTICIPATED = ("F015", "이미 참여한 일정입니다.", HTTP_422_UNPROCESSABLE_ENTITY)
    NOTICE_NOT_FOUND = ("F016", "공지를 찾을 수 없습니다.", HTTP_404_NOT_FOUND)
    INACTIVE_NOTICE = ("F017", "비활성화된 공지사항입니다.", HTTP_422_UNPROCESSABLE_ENTITY)


class Http5XX(BaseStatus):
    INTERNAL_SERVER_ERROR = ("E000", "서버 에러", HTTP_500_INTERNAL_SERVER_ERROR)
