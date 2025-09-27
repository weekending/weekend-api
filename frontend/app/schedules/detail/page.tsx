import { Suspense } from "react";
import ScheduleDetail from "@features/schedules/components/ScheduleDetail/ScheduleDetail";

export default async function ScheduleDetailPage() {
  return (
    <Suspense>
      <ScheduleDetail/>
    </Suspense>
  );
}
