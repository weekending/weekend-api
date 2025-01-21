import asyncio

from app.models.song import Song, SongStatus
from app.schemas.song import SongInfo, SongStatusInfo


class SongService:
    async def get_group_info(self, group_id: int) -> dict:
        result = await asyncio.gather(
            self.get_songs_by_status(group_id, SongStatus.INPROGRESS),
            self.get_songs_by_status(group_id, SongStatus.PENDING),
            self.get_songs_by_status(group_id, SongStatus.CLOSED),
        )
        return {
            "in_progress": result[0],
            "pending": result[1],
            "closed": result[2],
        }

    async def create_song(self, group_id: int, song_info: SongInfo) -> dict:
        song = Song(group_id=group_id, **song_info.model_dump())
        await song.save()
        return song.to_dict()

    async def remove_song(self, song_id: int):
        song = await Song.find_one(Song.id == song_id)
        await song.delete()

    async def update_status(self, song_id: int, song_info: SongStatusInfo) -> dict:
        song = await Song.find_one(Song.id == song_id)
        song.status = song_info.status
        await song.save()
        return song.to_dict()

    async def get_songs_by_status(self, group_id: int, status: SongStatus):
        songs = await Song.find(
            Song.is_active.is_(True),
            Song.status == status,
            Song.group_id == group_id,
        )
        return [song.to_dict() for song in songs]
