import request from "@features/common/utils/request";

export default async function getScheduleInfo(scheduleId: number) {
  const api = await request();
  return await api.get(`/api/schedules/${scheduleId}`);
}
