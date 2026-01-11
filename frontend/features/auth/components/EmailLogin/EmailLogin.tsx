"use client";
import { AxiosError } from "axios";
import Cookies from "js-cookie";
import { useRouter } from "next/navigation";
import { useState } from "react";
import login from "@features/auth/requests/login";
import Button from "@features/common/components/Button";
import ErrorMessage from "@features/common/components/ErrorMessage";
import { Input } from "@features/common/components/Input";
import AuthWrapper from "../AuthWrapper";

export default function EmailLogin() {
  const router = useRouter();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const requestLogin = async () => {
    setLoading(true);
    setError("");
    try {
      const res = await login(email, password)
      Cookies.set("access_token", res.data.data.token, { expires: 7 });
      router.push("/");
    } catch (err: unknown) {
      if (err instanceof AxiosError) {
        setError(err.response?.data.message);
      } else {
        setError("로그인 에러");
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <AuthWrapper>
      <div className="p-4">
        <h1 className="text-4xl font-bold mb-6">로그인</h1>
        <div className="flex flex-col gap-3">
          <Input
            id="loginEmail"
            placeholder="이메일"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
          <Input
            id="loginPassword"
            placeholder="비밀번호"
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            onKeyDown={(e) => {
              if (["Enter"].includes(e.key)) {
                requestLogin();
              }
            }}
          />
          <ErrorMessage message={error} />
          <Button
            onClick={requestLogin}
            disabled={!email || !password}
          >
            로그인
          </Button>
        </div>
      </div>
    </AuthWrapper>
  );
}
