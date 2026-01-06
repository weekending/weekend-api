import request from "@features/common/utils/request";

export default async function updateSchedules(
  scheduleId: number,
  title: string,
  day: string,
  start_time: string,
  end_time: string,
  location?: string,
  memo?: string
) {
  const api = await request();
  return await api.patch(
    `/api/schedules/${scheduleId}`,
    { data: { title, day, start_time, end_time, location, memo }}
  );
}
