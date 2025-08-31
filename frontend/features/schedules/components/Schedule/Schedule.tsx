"use client";
import { useEffect, useState } from "react";
import Nav from "@features/common/components/Nav";
import Wrapper from "@features/common/components/Wrapper";
import getSchedules from "@features/schedules/requests/getSchedules";
import ScheduleCalendar from "./ScheduleCalendar";
import ScheduleSection from "./ScheduleSection";
import { TSchedule } from "@features/schedules/types";

export default function Schedule() {
  const [month, setMonth] = useState(new Date());
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
            <ScheduleCalendar setMonth={setMonth} scheduleDates={scheduleDates} />
          </div>
          <div className="flex-1 md:mr-10 lg:mr-30 p-3">
            <div className="hidden md:block pb-12 border-b">
              <h1 className="p-2 text-[42px] font-bold">SCHEDULES</h1>
            </div>
            <div className="max-w-[420px] mt-3 mx-auto md:mx-0 p-3">
              {schedules.map((schedule) => (
                <ScheduleSection key={schedule.id} schedule={schedule} />
              ))}
            </div>
          </div>
        </div>
      </Wrapper>
    </>
  )
}
