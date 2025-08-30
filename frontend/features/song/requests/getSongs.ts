import request from "@features/common/utils/request";

export default async function getSongs(band_id: number, status?: string | null ) {
  const api = await request();
  return await api.get("/api/songs", { params: { band_id, status }});
}
