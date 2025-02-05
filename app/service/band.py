from starlette.exceptions import HTTPException

from app.models import Band, BandLink, User
from app.schemas.band import BandInfo


class BandService:
    async def create_band(self, data: BandInfo, user_id: int):
        band = Band(**data.model_dump())
        await band.save()
        band_link = BandLink(band_id=band.id)
        await band_link.save()
        user = await User.find_one(User.id == user_id)
        user.band_id = band.id
        await user.save()
        return band.to_dict()

    async def get_band_info(self, band_id: int) -> dict:
        band = await Band.find_one(Band.id == band_id)
        if not band:
            raise HTTPException(status_code=404, detail="밴드를 찾을 수 없습니다.")
        return band.to_dict(link_url=band.link_url)
