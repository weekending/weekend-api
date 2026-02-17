import request from "@features/common/utils/request";

interface SongsParams {
  bandId: number;
  status?: string | null;
  page?: number;
  size?: number;
}

export default async function getSongs({ bandId, status, page = 1, size = 10 }: SongsParams) {
  const api = await request();
  return await api.get("/api/songs", { params: { band_id: bandId, status, page, size }});
}
