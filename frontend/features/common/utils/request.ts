import axios from "axios";

export default async function request() {
  const api = axios.create({
    baseURL: process.env.NEXT_PUBLIC_API_BASE_URL,
  });
  return api
};
