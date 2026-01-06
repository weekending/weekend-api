import { useEffect, useState } from "react";
import { TSchedule } from "@features/schedules/types";
import { useSearchParams } from "next/navigation";
import getScheduleInfo from "@features/schedules/requests/getScheduleInfo";
import ScheduleDetailEdit from "./ScheduleDetailEdit";

export default function ScheduleEdit() {
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
  if (!schedule) return;

  return (
    <div className="max-w-[500px] mx-auto mt-18 md:mt-24">
      <ScheduleDetailEdit schedule={schedule}/>
    </div>
  );
}
