"use client";
import Nav from "@features/common/components/Nav";
import Wrapper from "@features/common/components/Wrapper";
import NoticeSection from "./NoticeSection";
import { TNotice } from "../types";

const noticeList: TNotice[] = [
  { id: 2, title: "윅엔드 키링 제작 안내", created_dtm: "2025.08.27" },
  { id: 1, title: "윅엔드 첫번째 합동 공연 Music Lounge Sum 신청", created_dtm: "2025.08.09" },
]

export default function Notice() {
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
