import request from "@features/common/utils/request";

export default async function getNoticeList(page: number) {
  const api = await request();
  return await api.get("/api/notice", { params: { page }});
}
