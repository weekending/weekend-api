import axios from "axios";
import Cookies from "js-cookie";

export default async function request() {
  const api = axios.create({
    baseURL: process.env.NEXT_PUBLIC_API_BASE_URL,
  });

  const accessToken = Cookies.get("access_token");
  if (accessToken) {
    api.defaults.headers.common["Authorization"] = `Bearer ${accessToken}`;
  }

  return api;
};
