"use client";
import Footer from "@features/common/components/Footer";
import Nav from "@features/common/components/Nav";
import Wrapper from "@features/common/components/Wrapper";
import Shop from "@features/shop/components/Shop";

export default function ShopPage() {
  return (
    <>
      <Nav/>
      <Wrapper>
        <Shop/>
      </Wrapper>
      <Footer/>
    </>
  );
}
