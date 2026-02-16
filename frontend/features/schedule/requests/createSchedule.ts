import request from "@features/common/utils/request";

export default async function createSchedule(
  title: string,
  day: string,
  startTime: string,
  endTime: string,
  location?: string,
  memo?: string
) {
  const api = await request();
  return await api.post(
    "/api/schedules",
    {
      band_id: 1,
      title,
      day,
      start_time: startTime,
      end_time: endTime,
      location,
      memo
    }
  );
}
