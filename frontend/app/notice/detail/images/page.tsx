"use client";
import { Suspense } from "react";
import Footer from "@features/common/components/Footer";
import NoticeDetailImage from "@features/notice/components/NoticeDetailImage";

export default function NoticeDetailImagPage() {
  return (
    <>
      <Suspense>
        <NoticeDetailImage/>
      </Suspense>
      <Footer/>
    </>
  );
}
