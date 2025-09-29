"use client";
import Footer from "@features/common/components/Footer";
import Nav from "@features/common/components/Nav";
import Wrapper from "@features/common/components/Wrapper";
import SongList from "@features/song/components/SongList";

export default function SongPage() {
  return (
    <>
      <Nav/>
      <Wrapper>
        <SongList/>
      </Wrapper>
      <Footer/>
    </>
  );
}
