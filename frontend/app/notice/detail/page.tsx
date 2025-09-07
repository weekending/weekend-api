import { Suspense } from "react";
import NoticeDetail from "@features/notice/components/NoticeDetail";

export default function NoticeDetailPage() {
  return (
    <Suspense>
      <NoticeDetail/>
    </Suspense>
  );
}
