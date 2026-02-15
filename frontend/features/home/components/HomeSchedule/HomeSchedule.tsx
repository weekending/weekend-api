import { ChevronRight } from "lucide-react";
import Link from "next/link";
import { TSchedule } from "@features/schedules/types";
import HomeScheduleItem from "./HomeScheduleItem";

type HomeScheduleProps = {
  schedules: TSchedule[];
};

export default function HomeSchedule({schedules}: HomeScheduleProps) {
  return (
    <div className="py-20 bg-gray-50">
      <div className="w-full mx-auto max-w-[1080px] p-5">
        <div className="flex items-center justify-between mb-10">
          <div>
            <h2 className="text-2xl font-bold mb-2">다가오는 스케줄</h2>
            <p className="text-gray-6">다음 일정을 놓치지 마세요</p>
          </div>
          <Link
            href="/schedules/"
            className="text-sm text-gray-6 hover:text-foreground flex items-center gap-1 transition-colors"
          >
            전체보기 <ChevronRight size={14} />
          </Link>
        </div>
        <div className="space-y-4">
          {schedules.map((schedule) => (
            <HomeScheduleItem
              key={schedule.id}
              schedule={schedule}
            />
          ))}
        </div>
      </div>
    </div>
  );
};
