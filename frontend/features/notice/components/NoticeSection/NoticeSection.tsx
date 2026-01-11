import { isoToYYMMDD } from "@features/common/utils/dateFormat";
import { TNotice } from "@features/notice/types";
import Link from "next/link";

type NoticeSectionProps = {
  notice: TNotice;
};

export default function NoticeSection({ notice }: NoticeSectionProps) {
  return (
    <Link href={`/notice/detail?pk=${notice.id}`}>
      <div className="flex items-center px-2 py-5 border-b border-gray-300">
        <div className="w-10">
          <p className="text-[14px]">{notice.id}</p>
        </div>
        <div className="flex-1 block md:flex justify-between">
          <p className="pb-1 md:pb-0 text-[16px] font-semibold leading-[1.2]">{notice.title}</p>
          <p className="text-[14px]">{isoToYYMMDD(notice.created_dtm)}</p>
        </div>
      </div>
    </Link>
  );
}
