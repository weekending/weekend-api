import { useSearchParams } from "next/navigation";
import { useEffect, useState } from "react";
import getScheduleInfo from "@features/schedules/requests/getScheduleInfo";
import { TSchedule } from "@features/schedules/types";
import ScheduleDetailDate from "./ScheduleDetailDate";
import ScheduleDetailLocation from "./ScheduleDetailLocation";
import ScheduleDetailMemo from "./ScheduleDetailMemo";
import ScheduleDetailSong from "./ScheduleDetailSong";


export default function ScheduleDetail() {
  const [schedule, setScheule] = useState<TSchedule>();
  const [loading, setLoading] = useState(true);
  const searchParams = useSearchParams();
  const scheduleId = Number(searchParams.get("pk"));

  useEffect(() => {
    (async () => {
      try {
        const response = await getScheduleInfo(scheduleId);
        setScheule(response.data.data);
      } catch {
        setLoading(false)
      }
    })();
  }, [scheduleId]);

  return (
    <div className="max-w-[500px] mx-auto mt-18 md:mt-24">
      <div className="p-4">
        <div className="ml-7 p-4">
          <h1 className="text-[21px] font-bold">{schedule?.title}</h1>
        </div>
        <ScheduleDetailDate schedule={schedule} />
        {schedule && schedule.location && (
          <ScheduleDetailLocation location={schedule.location} />
        )}
        {schedule && schedule.memo && (
          <ScheduleDetailMemo memo={schedule.memo} />
        )}
        {schedule && schedule.songs.length > 0 && (
          <>
            <hr className="my-4 border-gray-100"/>
            <ScheduleDetailSong songs={schedule.songs} />
          </>
        )}
      </div>
    </div>
  );
}
