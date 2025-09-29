"use client";
import { Suspense } from "react";
import Footer from "@features/common/components/Footer";
import Nav from "@features/common/components/Nav";
import Wrapper from "@features/common/components/Wrapper";
import NoticeDetail from "@features/notice/components/NoticeDetail";

export default function NoticeDetailPage() {
  return (
    <>
      <Nav/>
      <Wrapper>
        <Suspense>
          <NoticeDetail/>
        </Suspense>
      </Wrapper>
      <Footer/>
    </>
  );
}
