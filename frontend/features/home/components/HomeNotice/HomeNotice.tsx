import { ChevronRight } from "lucide-react";
import Link from "next/link";
import { TNotice } from "@features/notice/types";
import HomeNoticeItem from "./HomeNoticeItem";

type HomeNoticeProps = {
  notices: TNotice[];
};

export default function HomeNotice({notices}: HomeNoticeProps) {
  return (
    <div className="py-20">
      <div className="w-full mx-auto max-w-[1080px] p-5">
        <div className="flex items-center justify-between mb-10">
          <div>
            <h2 className="text-2xl font-bold mb-2">공지사항</h2>
            <p className="text-gray-6">밴드 소식을 확인하세요</p>
          </div>
          <Link
            href="/notice/"
            className="text-sm text-gray-6 hover:text-foreground flex items-center gap-1 transition-colors"
          >
            전체보기 <ChevronRight size={14} />
          </Link>
        </div>
        <div className="space-y-0 divide-y rounded-lg border border-gray-300 overflow-hidden">
          {notices.map((notice) => (
            <HomeNoticeItem
              key={notice.id}
              notice={notice}
            />
          ))}
        </div>
      </div>
    </div>
  );
};
