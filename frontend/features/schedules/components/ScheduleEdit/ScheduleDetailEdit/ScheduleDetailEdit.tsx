import { useState } from "react";
import { TSchedule } from "@features/schedules/types";
import ScheduleDetailEditDate from "./ScheduleDetailEditDate";
import ScheduleDetailEditLocation from "./ScheduleDetailEditLocation";
import ScheduleDetailEditMemo from "./ScheduleDetailEditMemo";
import ScheduleDetailEditTitle from "./ScheduleDetailEditTitle";

type ScheduleEditProps = {
  schedule: TSchedule;
};

export default function ScheduleDetailEdit({ schedule }: ScheduleEditProps) {
  const [title, setTitle] = useState(schedule.title);
  const [day, setDay] = useState(schedule.day);
  const [startTime, setStartTime] = useState(schedule.start_time);
  const [endTime, setEndTime] = useState(schedule.end_time);
  const [location, setLocation] = useState(schedule.location);
  const [memo, setMemo] = useState(schedule.memo || "");

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
    </div>
  );
}
