from app.common.exception import APIException
from app.common.http import Http4XX
from app.models import Band, BandLink, MemberType, User
from app.schemas.band import BandInfo


class BandService:
    async def create_band(self, data: BandInfo, user_id: int):
        """새 밴드를 생성하여 사용자를 `LEADER` 타입으로 설정"""
        band = Band(**data.model_dump())
        await band.save()
        user = await User.find_one(User.id == user_id)
        await user.append_band(band.id, member_type=MemberType.LEADER)
        band_link = BandLink(band_id=band.id)
        await band_link.save()
        return band.to_dict()

    async def get_band_info(self, band_id: int) -> dict:
        band = await Band.find_one(Band.id == band_id)
        if not band:
            raise APIException(Http4XX.BAND_NOT_FOUND)
        return band.to_dict(link_url=band.link_url)

    async def get_user_bands(self, user_id: int):
        bands = await Band.find_user_bands(user_id)
        return [band.to_dict() for band in bands]
