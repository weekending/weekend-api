"use client";
import { useSearchParams, notFound } from "next/navigation";
import { useEffect, useState } from "react";
import Nav from "@features/common/components/Nav";
import Wrapper from "@features/common/components/Wrapper";
import getNoticeInfo from "../requests/getNoticeInfo";
import { TNotice } from "../types";
import { isoToYYMMDDHHMMSS } from "@features/common/utils/dateFormat";


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
    <>
      <Nav/>
      <Wrapper>
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
        </div>
      </Wrapper>
    </>
  );
}
