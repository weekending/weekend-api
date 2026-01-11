import Cookies from "js-cookie";

export function isAuthenticated(): boolean {
  const accessToken = Cookies.get("access_token");
  return !!accessToken;
}
