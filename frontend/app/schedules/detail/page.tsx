"use client";
import { Suspense } from "react";
import Footer from "@features/common/components/Footer";
import Nav from "@features/common/components/Nav";
import Wrapper from "@features/common/components/Wrapper";
import ScheduleDetail from "@features/schedules/components/ScheduleDetail";

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
