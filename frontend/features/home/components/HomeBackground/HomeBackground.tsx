import Image from "next/image";

export default function HomeBackground() {
  return (
    <div className="relative mb-20 md:mb-40">
      <div className="absolute top-0 left-0 flex items-center w-full h-full bg-black/33">
        <div className="w-full">
          <div className="max-w-[1000px] mx-auto p-5">
            <h1 className="pb-5 sm:pb-8 lg:pb-12
              text-[40px] sm:text-[48px] md:text-[54px] lg:text-[60px] xl:text-[72px]
              text-white font-bold leading-[1.2] tracking-tight"
            >
              Ordinary Weekdays,<br/>Extraordinary <span className="font-extrabold text-[#F7E67B]">WEEKEND</span>s
            </h1>
            <p className="
              text-[16px] md:text-[18px] lg:text-[20px] xl:text-[24px]
              text-white"
            >
              Not professionals, but passionate. Not stars, but shining together.
            </p>
          </div>
        </div>
      </div>
      <Image
        src="/img/weekend-banner.png"
        alt="윅엔드"
        width={0}
        height={0}
        sizes="100vw"
        style={{ width: '100%', height: 'auto', maxHeight: '1080px', minHeight: '540px', objectFit: 'cover'}}
        unoptimized
      />
    </div>
  )
}
