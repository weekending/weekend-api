"use client";
import About from "@features/about/components/About";
import Footer from "@features/common/components/Footer";
import Nav from "@features/common/components/Nav";
import Wrapper from "@features/common/components/Wrapper";

export default function AboutPage() {
  return (
    <>
      <Nav/>
      <Wrapper>
        <About/>
        <Footer/>
      </Wrapper>
    </>
  );
}
