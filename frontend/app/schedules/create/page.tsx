"use client";
import Footer from "@features/common/components/Footer";
import Nav from "@features/common/components/Nav";
import Wrapper from "@features/common/components/Wrapper";
import ScheduleCreate from "@features/schedule/components/ScheduleCreate";

export default function ScheduleDetailEditPage() {
  return (
    <>
      <Nav/>
      <Wrapper>
        <ScheduleCreate/>
      </Wrapper>
      <Footer/>
    </>
  );
}
