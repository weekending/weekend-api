"use client";
import { Suspense } from "react";
import ScheduleDetail from "@features/schedules/components/ScheduleDetail/ScheduleDetail";
import Footer from "@features/common/components/Footer";
import Nav from "@features/common/components/Nav";
import Wrapper from "@features/common/components/Wrapper";

export default function ScheduleDetailPage() {
  return (
    <>
      <Nav/>
      <Wrapper>
        <Suspense>
          <ScheduleDetail/>
        </Suspense>
      </Wrapper>
      <Footer/>
    </>
  );
}
