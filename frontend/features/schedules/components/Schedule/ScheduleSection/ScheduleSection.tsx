import { TSchedule } from "@features/schedules/types";

function formatTime24to12(timeStr: string) {
  const [hours, minutes, seconds] = timeStr.split(":").map(Number);
  const date = new Date();
  date.setHours(hours, minutes, seconds);
  return date.toLocaleTimeString([], { hour: 'numeric', minute: '2-digit', hour12: true });
}

type ScheduleSectionProps = {
  schedule: TSchedule;
};

export default function ScheduleSection({ schedule }: ScheduleSectionProps) {
  return (
    <div className="flex pb-6">
      <div className="text-center text-[#A0A0A0]">
        <p className="text-[20px]">{schedule.day.slice(8, 10)}</p>
        <p className="text-[13px]">({schedule.weekday})</p>
      </div>
      <div className="ml-4">
        <p className="text-[16px] font-semibold">{schedule.title}</p>
        <div className="text-[14px]">
          <p>{formatTime24to12(schedule.start_time)} ~ {formatTime24to12(schedule.end_time)}</p>
          <p>{schedule.location}</p>
        </div>
      </div>
    </div>
  );
}