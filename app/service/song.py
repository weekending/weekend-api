import asyncio

from app.common.exception import APIException
from app.common.http import Http4XX
from app.schemas.song import SongInfo, SongStatusInfo
from app.models import Song, SongStatus


class SongService:
    async def get_band_info(self, band_id: int) -> dict:
        result = await asyncio.gather(
            self.get_songs_by_status(band_id, SongStatus.INPROGRESS),
            self.get_songs_by_status(band_id, SongStatus.PENDING),
        )
        return {"in_progress": result[0], "pending": result[1]}

    async def create_song(self, data: SongInfo, user_id: int) -> dict:
        song = Song(user_id=user_id, **data.model_dump())
        await song.save()
        return song.to_dict()

    async def remove_song(self, song_id: int):
        song = await Song.find_one(Song.id == song_id)
        if not song:
            raise APIException(Http4XX.SONG_NOT_FOUND)
        await song.delete()

    async def update_status(self, song_id: int, data: SongStatusInfo) -> dict:
        if not (song := await Song.find_one(Song.id == song_id)):
            raise APIException(Http4XX.SONG_NOT_FOUND)
        song.status = data.status
        await song.save()
        return song.to_dict()

    async def get_songs_by_status(self, band_id: int, status: SongStatus):
        songs = await Song.find(
            Song.is_active.is_(True),
            Song.status == status,
            Song.band_id == band_id,
        )
        return [song.to_dict() for song in songs]
