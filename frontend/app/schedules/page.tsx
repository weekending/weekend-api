"use client";
import { Suspense } from "react";
import Footer from "@features/common/components/Footer";
import Nav from "@features/common/components/Nav";
import Schedule from "@features/schedule/components/Schedule";

export default function SchedulePage() {
  return (
    <>
      <Nav/>
      <Suspense>
        <Schedule/>
      </Suspense>
      <Footer/>
    </>
  );
}
