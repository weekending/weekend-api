import Image from "next/image";

export default function HomeBackground({ children }: { children: React.ReactNode }) {
  return (
    <div className="relative mb-20 md:mb-40">
      <div className="absolute top-0 left-0 flex items-center w-full h-full bg-black/33">
        {children}
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
