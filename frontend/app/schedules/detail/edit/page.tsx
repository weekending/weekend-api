"use client";
import { Suspense } from "react";
import Footer from "@features/common/components/Footer";
import Nav from "@features/common/components/Nav";
import Wrapper from "@features/common/components/Wrapper";
import ScheduleEdit from "@features/schedules/components/ScheduleEdit";

export default function ScheduleDetailEditPage() {
  return (
    <>
      <Nav/>
      <Wrapper>
        <Suspense>
          <ScheduleEdit/>
        </Suspense>
      </Wrapper>
      <Footer/>
    </>
  );
}
