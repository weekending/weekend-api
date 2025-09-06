import { TSchedule } from "@features/schedules/types";

const formatTime24to12 = (timeStr: string) => {
  const [hours, minutes, seconds] = timeStr.split(":").map(Number);
  const date = new Date();
  date.setHours(hours, minutes, seconds);
  return date.toLocaleTimeString([], { hour: 'numeric', minute: '2-digit', hour12: true });
}

const formatDay = (date: string) => {
  const [year, month, day] = date.split("-");
  return `${month}.${day}`;
}

type ScheduleSectionProps = {
  schedule: TSchedule;
};

export default function ScheduleSection({ schedule }: ScheduleSectionProps) {
  return (
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
  );
}
