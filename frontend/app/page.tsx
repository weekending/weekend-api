"use client";
import Footer from "@features/common/components/Footer";
import Nav from "@features/common/components/Nav";
import Wrapper from "@features/common/components/Wrapper";
import Home from "@features/home/components/Home";
import HomeHeader from "@features/home/components/HomeHeader";

export default function Main() {
  return (
    <>
      <Nav/>
      <HomeHeader/>
      <Wrapper>
        <Home/>
      </Wrapper>
      <Footer/>
    </>
  );
}
