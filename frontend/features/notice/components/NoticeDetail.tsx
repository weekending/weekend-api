import Link from "next/link";
import { useSearchParams, notFound } from "next/navigation";
import { useEffect, useState } from "react";
import { isoToYYMMDDHHMMSS } from "@features/common/utils/dateFormat";
import getNoticeInfo from "../requests/getNoticeInfo";
import { TNotice } from "../types";
import NoticeImageSection from "./NoticeImageSection";


export default function NoticeDetail() {
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
        setLoading(false)
      }
    })();
  }, [noticeId]);

  if (!loading) {
    notFound();
  }

  return (
    <div className="p-3">
      <div className="mt-18 md:mt-24 pt-3 pb-5 border-b">
        <div className="m-2">
          <h1 className="pb-2 text-[21px] md:text-[24px] font-semibold leading-[1.2]">{notice?.title}</h1>
          <p className="text-[14px] text-[#808080]">{notice ? isoToYYMMDDHHMMSS(notice.created_dtm) : ""}</p>
        </div>
      </div>
      <div className="pt-12 p-3">
        {notice?.content.split("\n").map((line, idx) => (
          <p className="min-h-5 text-[15px] leading-5" key={idx}>{line}</p>
        ))}
      </div>
      <div className="mx-auto max-w-[540px] mt-10">
        {notice?.images && notice.images.length > 0 && (
          <>
            <div className="relative overflow-hidden">
              <NoticeImageSection images={[notice.images[0]]} />
              <div className="absolute bottom-0 left-0 right-0 h-60 bg-gradient-to-t from-white to-transparent" />
            </div>
            <div className="p-3 text-center">
              <Link
                href={`/notice/detail/images?pk=${noticeId}`}
                className="inline-block px-6 py-2 text-[14px] text-black bg-white border border-gray-400 rounded-lg"
              >
                이미지 전체보기
              </Link>
            </div>
          </>
        )}
      </div>
    </div>
  );
}
