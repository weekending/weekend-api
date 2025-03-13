from abc import ABC, abstractmethod

from app.domain import Band, MemberType


class BandUseCase(ABC):
    @abstractmethod
    async def create_band(
        self, user_id: int, name: str, member_type: MemberType
    ) -> Band:
        raise NotImplementedError

    @abstractmethod
    async def get_band_info(self, band_id: int) -> Band:
        raise NotImplementedError
