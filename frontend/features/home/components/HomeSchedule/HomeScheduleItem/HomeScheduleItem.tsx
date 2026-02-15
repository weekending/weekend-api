import Link from "next/link";
import { CalendarDays, MapPin } from "lucide-react";
import { formatTime24to12, isoToYYMMDD } from "@features/common/utils/dateFormat";
import { TSchedule } from "@features/schedules/types";

type HomeScheduleItemProps = {
  schedule: TSchedule;
};

export default function HomeScheduleItem({schedule}: HomeScheduleItemProps) {
  return (
    <Link
      href={`/schedules/detail/?pk=${schedule.id}`}
      className="flex sm:items-center gap-4 p-5 rounded-lg border border-gray-300 bg-white hover:bg-gray-100/50 transition-colors"
    >
      <div className="shrink-0 w-14 h-14 rounded-lg bg-skyblue/30 flex flex-col items-center justify-center">
        <span className="text-xs font-bold leading-none">
          {schedule.day.split("-")[1]}월
        </span>
        <span className="text-lg font-bold leading-tight">
          {schedule.day.split("-")[2]}
        </span>
      </div>
      <div className="flex-1 min-w-0">
        <div className="flex items-center gap-2 mb-1">
          <h3 className="font-semibold">{schedule.title}</h3>
        </div>
        <div className="flex flex-col sm:flex-row sm:items-center gap-1 sm:gap-4 text-sm text-gray-6">
          <span className="flex items-center gap-1 truncate">
            <CalendarDays size={14} />
            {isoToYYMMDD(schedule.day)} {formatTime24to12(schedule.start_time)}
          </span>
          { schedule.location && 
          <span className="flex items-center gap-1 min-w-0">
            <MapPin size={14} className="shrink-0" />
            <span className="truncate">{schedule.location}</span>
          </span>
          }
        </div>
      </div>
    </Link>
  );
};
