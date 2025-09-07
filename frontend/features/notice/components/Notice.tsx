"use client";
import { useEffect, useState } from "react";
import Nav from "@features/common/components/Nav";
import Wrapper from "@features/common/components/Wrapper";
import NoticeSection from "./NoticeSection";
import getNoticeList from "../requests/getNoticeList";
import { TNotice } from "../types";

export default function Notice() {
  const page = 1;
  const [noticeList, setNoticeList] = useState<TNotice[]>([]);

  useEffect(() => {
    (async () => {
      const response = await getNoticeList(page);
      setNoticeList(response.data.data);
    })();
  }, [page]);

  return (
    <>
      <Nav/>
      <Wrapper>
        <div className="p-3">
          <div className="mt-18 md:mt-24 pt-3 pb-8 border-b text-center">
            <h1 className="text-[36px] md:text-[42px] font-bold">Notice</h1>
          </div>
          <div className="p-3">
            {noticeList.map((notice) => (
              <NoticeSection
                key={notice.id}
                notice={notice}
              />
            ))}
          </div>
        </div>
      </Wrapper>
    </>
  );
}
