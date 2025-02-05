from app.common.utils import normalize_day, normalize_time, to_weekday
from app.models import PermissionType, Schedule, User
from app.schemas.schedule import ScheduleInfo


class ScheduleService:
    async def create_schedule(self, data: ScheduleInfo, user_id: int):
        user = await User.find_one(
            User.id == user_id,
            User.is_active.is_(True),
            User.permission.in_([PermissionType.LEADER, PermissionType.ADMIN]),
        )
        schedule = Schedule(band_id=user.band_id, **data.model_dump())
        await schedule.save()

    async def get_schedules(self, band_id: int) -> list[dict]:
        schedules = await Schedule.find_active_schedules(band_id)
        return [
            {
                "id": schedule.id,
                "year": schedule.day.year,
                "day": normalize_day(schedule.day),
                "weekday": to_weekday(schedule.day),
                "start_time": (
                    normalize_time(schedule.start_time)
                    if schedule.start_time
                    else None
                ),
                "end_time": (
                    normalize_time(schedule.end_time)
                    if schedule.end_time
                    else None
                ),
                "users": [{"name": u.name} for u in schedule.users],
                "title": schedule.title,
                "location": schedule.location,
                "memo": schedule.memo,
            }
            for schedule in schedules
        ]
