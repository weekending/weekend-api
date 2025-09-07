import request from "@features/common/utils/request";

export default async function getNoticeInfo(noticeId: number) {
  const api = await request();
  return await api.get(`/api/notice/${noticeId}`);
}
