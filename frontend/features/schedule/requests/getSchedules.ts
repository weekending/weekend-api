import request from "@features/common/utils/request";

export default async function getSchedules(bandId: number, from?: string, to?: string) {
  const api = await request();
  return await api.get("/api/schedules", { params: { band_id: bandId, from, to }});
}
