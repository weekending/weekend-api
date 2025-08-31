import { TSchedule } from "@features/schedules/types";

const formatTime24to12 = (timeStr: string) => {
  const [hours, minutes, seconds] = timeStr.split(":").map(Number);
  const date = new Date();
  date.setHours(hours, minutes, seconds);
  return date.toLocaleTimeString([], { hour: 'numeric', minute: '2-digit', hour12: true });
}

function formatDay(date: string) {
  const [year, month, day] = date.split("-");
  return `${month}.${day}`;
}

type ScheduleSectionProps = {
  schedule: TSchedule;
};

export default function ScheduleSection({ schedule }: ScheduleSectionProps) {
  return (
    <div className="flex pb-6">
      <div className="w-[72px] text-center">
        <p className="text-[24px] font-semibold">{formatDay(schedule.day)}</p>
        <p className="text-[16px]/[16px]">({schedule.weekday})</p>
      </div>
      <div className="ml-6">
        <p className="text-[16px]">{schedule.title}</p>
        <div className="text-[14px]/[20px] text-[#808080]">
          <p>{formatTime24to12(schedule.start_time)} ~ {formatTime24to12(schedule.end_time)}</p>
          <p>{schedule.location}</p>
        </div>
      </div>
    </div>
  );
}
