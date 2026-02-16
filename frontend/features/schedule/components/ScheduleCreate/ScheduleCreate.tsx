import { useState } from "react";
import { useRouter } from "next/navigation";
import ScheduleDetailEditTitle from "../ScheduleEdit/ScheduleDetailEdit/ScheduleDetailEditTitle";
import ScheduleDetailEditDate from "../ScheduleEdit/ScheduleDetailEdit/ScheduleDetailEditDate";
import ScheduleDetailEditLocation from "../ScheduleEdit/ScheduleDetailEdit/ScheduleDetailEditLocation";
import ScheduleDetailEditMemo from "../ScheduleEdit/ScheduleDetailEdit/ScheduleDetailEditMemo";
import createSchedule from "@features/schedule/requests/createSchedule";

export default function ScheduleCreate() {
  const router = useRouter();
  const [title, setTitle] = useState("");
  const [day, setDay] = useState(() => {
    const today = new Date();
    return today.toISOString().split('T')[0];
  });
  const [startTime, setStartTime] = useState("");
  const [endTime, setEndTime] = useState("");
  const [location, setLocation] = useState("");
  const [memo, setMemo] = useState("");
  const [loading, setLoading] = useState(true);

  const saveSchedule = async () => {
    try {
      await createSchedule(title, day, startTime, endTime, location, memo);
      router.push("/schedules");
    } catch (error) {
      console.error("Failed to update schedule:", error);
      alert("스케줄 생성에 실패했습니다.");
    }
  };

  return (
    <div className="max-w-[500px] mx-auto mt-18 md:mt-24">
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
    </div>
  );
}
