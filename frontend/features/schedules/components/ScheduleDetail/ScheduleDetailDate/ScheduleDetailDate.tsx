import { formatTime24to12, isoToYYMMDD } from "@features/common/utils/dateFormat";
import { TSchedule } from "@features/schedules/types";
import ScheduleDetailLogo from "../ScheduleDetailLogo";

type ScheduleDetailDateProps = {
  schedule: TSchedule;
};

export default function ScheduleDetailDate({ schedule }: ScheduleDetailDateProps) {
  return (
    <div className="flex gap-2 mb-1">
      <ScheduleDetailLogo src="/img/schedule.png" alt="schedule" />
      <div className="block md:flex gap-2 mb-1 md:mb-0 px-1 py-0 md:py-1 text-[16px]">
        <div className="flex gap-2">
          <p>{isoToYYMMDD(schedule.day)}</p>
          <p>{schedule.weekday}요일</p>
        </div>
        <div className="flex gap-1">
          <p>{formatTime24to12(schedule.start_time)}</p>
          <p>~</p>
          <p>{formatTime24to12(schedule.end_time)}</p>
        </div>
      </div>
    </div>
  );
}
