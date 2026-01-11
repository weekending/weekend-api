import MemberList from "./MemberList";

export default function About() {
  return (
    <>
      <div className="mt-18 md:mt-24 p-3 text-center">
        <h1 className="text-[36px] md:text-[42px] font-bold">About Us</h1>
      </div>
      <div className="md:w-[560px] m-5 md:mx-auto pt-10 md:pt-20 pb-10 md:pb-40">
        <p className="text-[16px] md:text-[20px]/[35px]">
          안녕하세요. 밴드 <span className="font-bold">윅엔드</span>입니다.<br/><br/>
          매일을 바쁘게 살아가는 여섯 명이 음악을 향한 열정 하나로 주말마다 모였습니다. 우리 밴드는 감성적인 얼터너티브 록부터, 파워풀한 브릿팝까지 다양한 장르를 넘나들며 노래하고 있습니다.<br/><br/>
          좋은 음악, 좋은 사람들과 함께하는 시간을 즐기며, 언제든 무대에서 여러분을 만나고 싶습니다!
        </p>
      </div>
      <div className="pb-40">
        {/* <MemberList/> */}
      </div>
    </>
  );
}
