import { formatDay, formatTime24to12 } from "@features/common/utils/dateFormat";
import { TSchedule } from "@features/schedules/types";
import Link from "next/link";

type ScheduleSectionProps = {
  schedule: TSchedule;
};

export default function ScheduleSection({ schedule }: ScheduleSectionProps) {
  return (
    <Link href={`/schedules/detail?pk=${schedule.id}`}>
      <div className="flex px-2 py-5 border-b border-gray-300">
        <div className="text-center">
          <div className="flex justify-center items-center gap-1 w-[72px]">
            <p className="text-[16px]">{formatDay(schedule.day)}</p>
            <p className="text-[14px]">({schedule.weekday})</p>
          </div>
          <p className="text-[14px] text-[#808080]">{formatTime24to12(schedule.start_time)}</p>
        </div>
        <div className="ml-5">
          <p className="text-[16px] font-semibold">{schedule.title}</p>
          <p className="text-[14px] text-[#808080] leading-[1.4]">{schedule.location}</p>
        </div>
      </div>
    </Link>
  );
}
