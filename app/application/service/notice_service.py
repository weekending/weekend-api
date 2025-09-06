from fastapi import Depends

from app.adapter.outbound.persistence import NoticePersistenceAdapter
from app.common.exception import APIException
from app.common.http import Http4XX
from app.domain import Notice
from ..port.input import NoticeUseCase
from ..port.output import NoticeRepositoryPort


class NoticeService(NoticeUseCase):
    def __init__(
        self,
        notice_repo: NoticeRepositoryPort = Depends(NoticePersistenceAdapter),
    ):
        self._notice_repo = notice_repo

    async def get_notice_list(self, size: int, page: int) -> list[Notice]:
        return await self._notice_repo.find_all(
            limit=size, offset=size * (page - 1)
        )

    async def get_notice_info(self, notice_id: int) -> Notice:
        if not (notice := await self._notice_repo.find_by_id_or_none(notice_id)):
            raise APIException(Http4XX.NOTICE_NOT_FOUND)
        elif not notice.is_active:
            raise APIException(Http4XX.INACTIVE_NOTICE)
        return notice
