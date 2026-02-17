import { notFound, useRouter, useSearchParams } from "next/navigation";
import { useEffect, useState } from "react";
import { isAuthenticated } from "@features/auth/utils/checkAuth";
import EditButton from "@features/common/components/EditButton";
import getScheduleInfo from "@features/schedule/requests/getScheduleInfo";
import { TSchedule } from "@features/schedule/types";
import ScheduleDetailDate from "./ScheduleDetailDate";
import ScheduleDetailLocation from "./ScheduleDetailLocation";
import ScheduleDetailMemo from "./ScheduleDetailMemo";
import ScheduleDetailSong from "./ScheduleDetailSong";


export default function ScheduleDetail() {
  const router = useRouter();
  const [schedule, setSchedule] = useState<TSchedule>();
  const [loading, setLoading] = useState(true);
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [notFoundError, setNotFoundError] = useState(false);
  const searchParams = useSearchParams();
  const scheduleId = Number(searchParams.get("pk"));
  
  useEffect(() => {
    setIsLoggedIn(isAuthenticated());
  }, []);

  useEffect(() => {
    (async () => {
      try {
        const response = await getScheduleInfo(scheduleId);
        const scheduleData = response.data.data;
        if (!scheduleData.is_active) {
          setNotFoundError(true);
          return;
        }
        setSchedule(scheduleData);
        setLoading(false);
      } catch {
        setNotFoundError(true);
      }
    })();
  }, [scheduleId]);

  if (notFoundError) {
    notFound();
  }

  if (loading || !schedule) {
    return null;
  }

  return (
    <div className="pt-18">
      <div className="w-full mx-auto max-w-[500px] p-5">
        <h1 className="text-2xl font-bold tracking-tight mb-6">{schedule.title}</h1>
        <ScheduleDetailDate schedule={schedule} />
        {schedule.location && (
          <ScheduleDetailLocation location={schedule.location} />
        )}
        {schedule.memo && (
          <ScheduleDetailMemo memo={schedule.memo} />
        )}
        {schedule.songs.length > 0 && (
          <>
            <hr className="my-6 border-gray-300"/>
            <ScheduleDetailSong songs={schedule.songs} />
          </>
        )}
      </div>

      {isLoggedIn && (
        <EditButton
          onClick={() => router.push(`/schedules/detail/edit/?pk=${scheduleId}`)}
          ariaLabel="스케줄 수정"
        />
      )}
    </div>
  );
}
