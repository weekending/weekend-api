import HomeBackground from "./HomeBackground";
import HomeSocial from "./HomeSocial";

export default function HomeHeader() {
  return (
    <HomeBackground>
      <div className="w-full">
        <div className="max-w-[1000px] mx-auto p-5">
          <h1 className="py-6
            text-[40px] sm:text-[48px] md:text-[54px] lg:text-[60px] xl:text-[72px]
            text-white font-bold leading-[1.2] tracking-tight"
          >
            2026년에도<br/><span className="font-extrabold text-[#F7E67B]">윅엔드</span>는<br/>계속됩니다!
          </h1>
          <p className="pb-12
            text-[16px] md:text-[18px] lg:text-[20px] xl:text-[24px]
            text-white"
          >
            Not professionals, but passionate. Not stars, but shining together.
          </p>
          <HomeSocial/>
        </div>
      </div>
    </HomeBackground>
  );
}
