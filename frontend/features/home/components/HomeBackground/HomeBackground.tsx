import Image from "next/image";

export default function HomeBackground() {
  return (
    <div className="relative mb-40">
      <div className="absolute top-0 left-0 w-full h-full bg-black/25"></div>
      <Image
        src="/img/weekend-banner.png"
        alt="윅엔드"
        width={0}
        height={0}
        sizes="100vw"
        style={{ width: '100%', height: 'auto', maxHeight: '1080px', minHeight: '450px', objectFit: 'cover'}}
        unoptimized
      />
    </div>
  )
}
