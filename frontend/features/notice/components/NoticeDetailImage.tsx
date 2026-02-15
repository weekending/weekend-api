"use client";

import { useSearchParams, notFound } from "next/navigation";
import { useEffect, useState } from "react";
import getNoticeInfo from "../requests/getNoticeInfo";
import { TNotice } from "../types";
import NoticeImageSection from "./NoticeImageSection";

export default function NoticeDetailImage() {
  const [notice, setNotice] = useState<TNotice>();
  const [loading, setLoading] = useState(true);
  const searchParams = useSearchParams();
  const noticeId = Number(searchParams.get("pk"));
  if (!noticeId) {
    notFound();
  }

  useEffect(() => {
    (async () => {
      try {
        const response = await getNoticeInfo(noticeId);
        setNotice(response.data.data);
      } catch {
        setLoading(false);
      }
    })();
  }, [noticeId]);

  if (!loading) {
    notFound();
  }

  return (
    <div className="mx-auto max-w-[900px]">
      {notice?.images && notice.images.length > 0 && (
        <NoticeImageSection images={notice.images} />
      )}
    </div>
  );
}
