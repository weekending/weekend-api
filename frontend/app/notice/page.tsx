"use client";
import Footer from "@features/common/components/Footer";
import Nav from "@features/common/components/Nav";
import Wrapper from "@features/common/components/Wrapper";
import Notice from "@features/notice/components/Notice";

export default function NoticePage() {
  return (
    <>
      <Nav/>
      <Wrapper>
        <Notice/>
      </Wrapper>
      <Footer/>
    </>
  );
}
