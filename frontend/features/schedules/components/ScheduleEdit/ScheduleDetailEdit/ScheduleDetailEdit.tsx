import { useState } from "react";
import { useRouter } from "next/navigation";
import { TSchedule } from "@features/schedules/types";
import updateSchedules from "@features/schedules/requests/updateSchedule";
import ScheduleDetailEditDate from "./ScheduleDetailEditDate";
import ScheduleDetailEditLocation from "./ScheduleDetailEditLocation";
import ScheduleDetailEditMemo from "./ScheduleDetailEditMemo";
import ScheduleDetailEditTitle from "./ScheduleDetailEditTitle";

type ScheduleEditProps = {
  schedule: TSchedule;
};

export default function ScheduleDetailEdit({ schedule }: ScheduleEditProps) {
  const router = useRouter();
  const [title, setTitle] = useState(schedule.title);
  const [day, setDay] = useState(schedule.day);
  const [startTime, setStartTime] = useState(schedule.start_time);
  const [endTime, setEndTime] = useState(schedule.end_time);
  const [location, setLocation] = useState(schedule.location);
  const [memo, setMemo] = useState(schedule.memo || "");

  const saveSchedule = async () => {
    try {
      await updateSchedules(schedule.id, title, day, startTime, endTime, location, memo);
      router.push(`/schedules/detail/?pk=${schedule.id}`);
    } catch (error) {
      console.error("Failed to update schedule:", error);
      alert("스케줄 수정에 실패했습니다.");
    }
  };

  return (
    <div className="p-4">
      <ScheduleDetailEditTitle title={title} onChange={(e) => setTitle(e.target.value)}/>
      <ScheduleDetailEditDate
        day={day}
        startTime={startTime}
        endTime={endTime}
        onChangeDay={(e) => setDay(e.target.value)}
        onChangeStartTime={(e) => setStartTime(e.target.value)}
        onChangeEndTime={(e) => setEndTime(e.target.value)}
      />
      <ScheduleDetailEditLocation location={location} onChange={(e) => setLocation(e.target.value)}/>
      <ScheduleDetailEditMemo memo={memo} onChange={(e) => setMemo(e.target.value)}/>

      <div className="mt-4 flex justify-end gap-2">
        <button
          onClick={saveSchedule}
          className="px-4 py-2 bg-gray-700 text-white rounded cursor-pointer hover:bg-gray-900"
        >
          저장
        </button>
      </div>
    </div>
  );
}
