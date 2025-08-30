import request from "@features/common/utils/request";

export default async function login(email: string, password: string) {
  const api = await request()
  return await api.post("/api/auth/login", { email, password });
}
