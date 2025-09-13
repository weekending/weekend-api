"use client";
import { useSearchParams } from "next/navigation";
import { useEffect, useState } from "react";
import Nav from "@features/common/components/Nav";
import Wrapper from "@features/common/components/Wrapper";
import getScheduleInfo from "@features/schedules/requests/getScheduleInfo";
import { TSchedule } from "@features/schedules/types";
import { formatTime24to12, isoToYYMMDD } from "@features/common/utils/dateFormat";
import Image from "next/image";


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
    <>
      <Nav/>
      <Wrapper>
        <div className="max-w-[500px] mx-auto mt-18 md:mt-24">
          <div className="p-4">
            <div className="ml-8 p-3">
              <h1 className="text-[21px] font-bold">{schedule?.title}</h1>
            </div>
            <div className="flex gap-2 pb-4">
              <div className="p-1">
                <Image
                  src="/img/schedule.png"
                  alt="schedule"
                  width={24}
                  height={24}
                  unoptimized
                />
              </div>
              <div className="px-1 text-[18px]">
                <div className="flex gap-2">
                  <p>{schedule? isoToYYMMDD(schedule.day) : ""}</p>
                  <p>{schedule?.weekday}요일</p>
                </div>
                <div className="flex gap-1">
                  <p>{schedule ? formatTime24to12(schedule.start_time) : ""}</p>
                  <p>~</p>
                  <p>{schedule ? formatTime24to12(schedule.end_time) : ""}</p>
                </div>
              </div>
            </div>
            <div className="flex gap-2 pb-4">
              <div className="p-1">
                <Image
                  src="/img/location.png"
                  alt="location"
                  width={24}
                  height={24}
                  unoptimized
                />
              </div>
              <p className="flex-1 p-1 text-[18px] leading-6">{schedule?.location}</p>
            </div>
            <div className="flex gap-2 pb-2">
              <div className="p-1">
                <Image
                  src="/img/memo.png"
                  alt="memo"
                  width={24}
                  height={24}
                  unoptimized
                />
              </div>
              <div className="flex-1 p-1 leading-6">
                {schedule?.memo.split("\n").map((line, idx) => (
                  <p className="min-h-5" key={idx}>{line}</p>
                ))}
              </div>
            </div>
          </div>
        </div>
      </Wrapper>
    </>
  );
}
