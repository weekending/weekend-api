"use client";
import { Suspense } from "react";
import Footer from "@features/common/components/Footer";
import Nav from "@features/common/components/Nav";
import SongList from "@features/song/components/SongList";

export default function SongListPage() {
  return (
    <>
      <Nav/>
      <Suspense>
        <SongList/>
      </Suspense>
      <Footer/>
    </>
  );
}
