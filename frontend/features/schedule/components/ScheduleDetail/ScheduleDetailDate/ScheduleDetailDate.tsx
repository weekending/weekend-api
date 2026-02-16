import { CalendarIcon, Clock } from "lucide-react";
import { format } from "date-fns";
import { ko } from "date-fns/locale";
import { formatTime24to12 } from "@features/common/utils/dateFormat";
import { TSchedule } from "@features/schedule/types";

type ScheduleDetailDateProps = {
  schedule: TSchedule;
};

export default function ScheduleDetailDate({ schedule }: ScheduleDetailDateProps) {
  return (
    <div className="space-y-3 mb-6">
      <div className="flex items-center gap-2 text-foreground">
        <CalendarIcon size={18} className="text-gray-6 shrink-0" />
        <span>{format(schedule.day, "yyyy년 M월 d일 (EEEE)", { locale: ko })}</span>
      </div>
      <div className="flex items-center gap-2 text-foreground">
        <Clock size={18} className="text-gray-6 shrink-0" />
        <span>{formatTime24to12(schedule.start_time)} - {formatTime24to12(schedule.end_time)}</span>
      </div>
    </div>
  );
}
