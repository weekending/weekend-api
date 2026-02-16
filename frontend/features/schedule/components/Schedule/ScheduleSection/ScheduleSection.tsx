import { CalendarIcon, MapPin, Clock } from "lucide-react";
import { formatTime24to12 } from "@features/common/utils/dateFormat";
import { format } from "date-fns"
import { ko } from "date-fns/locale";
import { TSchedule } from "@features/schedule/types";
import Link from "next/link";

type ScheduleSectionProps = {
  schedule: TSchedule;
};

export default function ScheduleSection({ schedule }: ScheduleSectionProps) {
  return (
    <Link
      className="block rounded-lg border border-gray-300 p-4 transition-colors hover:bg-muted/50"
      href={`/schedules/detail?pk=${schedule.id}`}
    >
      <div className="flex items-start justify-between gap-4">
        <div className="space-y-1.5">
          <p className="font-semibold">{schedule.title}</p>
          <div className="flex items-center gap-4 text-sm text-gray-6">
            <span className="flex items-center gap-1.5">
              <CalendarIcon size={14} />
              {format(schedule.day, "M월 d일 (EEE)", { locale: ko })}
            </span>
            <span className="flex items-center gap-1.5">
              <Clock size={14} />
              {formatTime24to12(schedule.start_time)}
            </span>
          </div>
          {schedule.location && (
            <p className="flex items-center gap-1.5 text-sm text-gray-6">
              <MapPin size={14} />
              {schedule.location}
            </p>
          )}
        </div>
      </div>
    </Link>
  );
}
