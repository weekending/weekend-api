"use client";
import { Suspense } from "react";
import Footer from "@features/common/components/Footer";
import Nav from "@features/common/components/Nav";
import Wrapper from "@features/common/components/Wrapper";
import Schedule from "@features/schedules/components/Schedule";

export default function SchedulePage() {
  return (
    <>
      <Nav/>
      <Wrapper>
        <Suspense>
          <Schedule/>
        </Suspense>
      </Wrapper>
      <Footer/>
    </>
  );
}
