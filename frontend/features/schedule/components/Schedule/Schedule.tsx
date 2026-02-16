import { useRouter, useSearchParams } from "next/navigation";
import { useEffect, useState } from "react";
import { format } from "date-fns"
import { ko } from "date-fns/locale";
import { isAuthenticated } from "@features/auth/utils/checkAuth";
import { dateToYYMMDD } from "@features/common/utils/dateFormat";
import AddButton from "@features/common/components/AddButton";
import getSchedules from "@features/schedule/requests/getSchedules";
import { TSchedule } from "@features/schedule/types";
import ScheduleCalendar from "./ScheduleCalendar";
import ScheduleSection from "./ScheduleSection";

export default function Schedule() {
  const router = useRouter();
  const [schedules, setSchedules] = useState<TSchedule[]>([]);
  const [scheduleDates, setScheduleDates] = useState<Date[]>([]);
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  const searchParams = useSearchParams();
  const queryMonth = searchParams.get("month");
  const month = queryMonth ? new Date(queryMonth) : new Date();

  const setMonth = (date: Date) => {
    router.push(`/schedules/?month=${dateToYYMMDD(date)}`)
  }

  useEffect(() => {
    setIsLoggedIn(isAuthenticated());
  }, []);

  useEffect(() => {
    const start = new Date(month.getFullYear(), month.getMonth(), 1);
    const end = new Date(month.getFullYear(), month.getMonth() + 1, 0);
    (async () => {
      const response = await getSchedules(1, start.toISOString().slice(0, 10), end.toISOString().slice(0, 10));
      const dates = response.data.data.map(
        (s: { day: string; }) => new Date(s.day)
      );
      setSchedules(response.data.data);
      setScheduleDates(dates);
    })();
  }, [queryMonth]);

  return (
    <div className="pt-18">
      <div className="w-full mx-auto max-w-[1080px] p-5">
        <h1 className="text-2xl font-bold tracking-tight mb-8">SCHEDULES</h1>

        <div className="flex flex-col md:flex-row gap-8">
          <div className="shrink-0">
            <ScheduleCalendar
              month={month}
              setMonth={setMonth}
              scheduleDates={scheduleDates}
            />
          </div>
          <div className="flex-1 min-w-0">
            <h2 className="text-lg font-semibold mb-4">
              {format(month, "yyyy년 M월", { locale: ko })} 스케줄
            </h2>
            {schedules.length === 0 ? (
              <p className="text-gray-6">이번 달 스케줄이 없습니다.</p>
            ) : (
              <div className="space-y-3">
                {schedules.map((schedule) => (
                  <ScheduleSection key={schedule.id} schedule={schedule} />
                ))}
              </div>
            )}
          </div>
        </div>
      </div>

      {isLoggedIn && (
        <AddButton
          onClick={() => router.push("/schedules/create")}
          ariaLabel="스케줄 생성"
        />
      )}
    </div>
  );
}
