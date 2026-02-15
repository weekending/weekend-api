import Link from "next/link";
import { isoToYYMMDD } from "@features/common/utils/dateFormat";
import { TNotice } from "@features/notice/types";

type HomeNoticeItemProps = {
  notice: TNotice;
};

export default function HomeNoticeItem({notice}: HomeNoticeItemProps) {
  return (
    <Link
      href={`/notice/detail/?pk=${notice.id}`}
      className="flex items-center justify-between px-5 py-4 border-gray-300 hover:bg-gray-100/50 transition-colors"
    >
      <div className="flex items-center gap-1.5 min-w-0">
        {notice.is_new && (
          <span className="shrink-0 text-red text-xs">
            New
          </span>
        )}
        <span className="text-[15px] font-medium truncate">
          {notice.title}
        </span>
      </div>
      <span className="shrink-0 text-sm text-gray-6 ml-4">
        {isoToYYMMDD(notice.created_dtm)}
      </span>
    </Link>
  )
};
