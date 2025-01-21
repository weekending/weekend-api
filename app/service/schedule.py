from app.common.utils import normalize_date, normalize_time, to_weekday
from app.models.schedule import Schedule


class ScheduleService:
    async def get_schedules(self, group_id: int) -> list[dict]:
        schedules = await Schedule.find_active_schedules(group_id)
        return [
            {
                "id": schedule.id,
                "year": schedule.date.year,
                "date": normalize_date(schedule.date),
                "weekday": to_weekday(schedule.date),
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
