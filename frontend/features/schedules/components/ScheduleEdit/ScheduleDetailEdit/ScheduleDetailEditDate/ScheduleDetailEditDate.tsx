import ScheduleDetailLogo from "@features/schedules/components/ScheduleDetail/ScheduleDetailLogo";
import ScheduleEditInput from "../ScheduleEditText/ScheduleEditInput/ScheduleEditInput";

type ScheduleDetailEditDateProps = {
  day: string;
  startTime: string;
  endTime: string;
  onChangeDay: (e: React.ChangeEvent<HTMLInputElement>) => void;
  onChangeStartTime: (e: React.ChangeEvent<HTMLInputElement>) => void;
  onChangeEndTime: (e: React.ChangeEvent<HTMLInputElement>) => void;
};

export default function ScheduleDetailEditDate({
  day,
  startTime,
  endTime,
  onChangeDay,
  onChangeStartTime,
  onChangeEndTime
}: ScheduleDetailEditDateProps) {
  return (
    <div className="flex gap-2 mb-3">
      <ScheduleDetailLogo src="/img/schedule.png" alt="schedule" />
      <div className="flex-1 text-[16px]">
        <div className="flex gap-2 items-center">
          <ScheduleEditInput value={day} onChange={onChangeDay} type="date" placeholder="날짜 선택"/>
        </div>
        <div className="gap-3">
          <ScheduleEditInput value={startTime} onChange={onChangeStartTime} type="time"/>
          <ScheduleEditInput value={endTime} onChange={onChangeEndTime} type="time"/>
        </div>
      </div>
    </div>
  );
}
