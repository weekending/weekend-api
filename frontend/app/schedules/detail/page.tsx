"use client";
import { Suspense } from "react";
import Footer from "@features/common/components/Footer";
import Nav from "@features/common/components/Nav";
import ScheduleDetail from "@features/schedule/components/ScheduleDetail";

export default function ScheduleDetailPage() {
  return (
    <>
      <Nav/>
      <Suspense>
        <ScheduleDetail/>
      </Suspense>
      <Footer/>
    </>
  );
}
