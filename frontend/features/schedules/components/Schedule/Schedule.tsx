"use client";
import { useEffect, useState } from "react";
import Nav from "@features/common/components/Nav";
import Wrapper from "@features/common/components/Wrapper";
import getSchedules from "@features/schedules/requests/getSchedules";
import { useScheduleStore } from "@features/schedules/store/useScheduleStore";
import { TSchedule } from "@features/schedules/types";
import ScheduleCalendar from "./ScheduleCalendar";
import ScheduleSection from "./ScheduleSection";

export default function Schedule() {
  const { month, setMonth } = useScheduleStore();
  const [schedules, setSchedules] = useState<TSchedule[]>([]);
  const [scheduleDates, setScheduleDates] = useState<Date[]>([]);

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
  }, [month]);

  return (
    <>
      <Nav/>
      <Wrapper>
        <div className="block md:flex flex-wrap flex-row-reverse mt-18 md:mt-30">
          <div className="block md:hidden p-3 text-center">
            <h1 className="text-[36px] font-bold">SCHEDULES</h1>
          </div>
          <div className="flex-1 p-3">
            <ScheduleCalendar
              month={month}
              setMonth={setMonth}
              scheduleDates={scheduleDates}
            />
          </div>
          <div className="flex-1 md:mr-10 lg:mr-30 p-3">
            <div className="hidden md:block pb-12">
              <h1 className="p-2 text-[42px] font-bold">SCHEDULES</h1>
            </div>
            <div className="mx-auto md:mx-0 border-t p-3">
              {schedules.map((schedule) => (
                <ScheduleSection key={schedule.id} schedule={schedule} />
              ))}
            </div>
          </div>
        </div>
      </Wrapper>
    </>
  );
}
