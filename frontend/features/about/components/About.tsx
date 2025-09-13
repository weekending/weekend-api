"use client";
import Nav from "@features/common/components/Nav";
import Wrapper from "@features/common/components/Wrapper";
import MemberList from "./MemberList";

export default function About() {
  return (
    <>
      <Nav/>
      <Wrapper>
        <div className="mt-18 md:mt-24 p-3 text-center">
          <h1 className="text-[36px] md:text-[42px] font-bold">About Us</h1>
        </div>
        <div className="md:w-[560px] m-5 md:mx-auto pt-10 md:pt-20 pb-10 md:pb-40">
          <p className="text-[16px] md:text-[20px]/[35px]">
            안녕하세요. 밴드 <span className="font-bold">윅엔드</span>입니다.<br/>
            저희는 음악을 사랑하는 직장인들이 모여 결성한 밴드입니다.<br/>
            멤버 각자 직업은 다르지만 음악으로 하나되어 매주마다 땀과 웃음을 나누고 있습니다.<br/>
            좋은 음악, 좋은 사람들과 함께하는 시간을 즐기며, 언제든 무대에서 여러분을 만나고 싶습니다!
          </p>
        </div>
        <div className="pb-40">
          <MemberList/>
        </div>
      </Wrapper>
    </>
  );
}
