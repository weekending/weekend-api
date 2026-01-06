import request from "@features/common/utils/request";

export default async function updateSchedules(
  scheduleId: number,
  title: string,
  day: string,
  startTime: string,
  endTime: string,
  location?: string,
  memo?: string
) {
  const api = await request();
  return await api.patch(
    `/api/schedules/${scheduleId}`,
    {
      title,
      day,
      start_time: startTime,
      end_time: endTime,
      location,
      memo
    }
  );
}
