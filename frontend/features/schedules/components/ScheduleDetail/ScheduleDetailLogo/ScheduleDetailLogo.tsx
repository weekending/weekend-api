import Image from "next/image";

type ScheduleDetailImageProps = {
  src: string;
  alt: string;
};

export default function ScheduleDetailLogo({ src, alt }: ScheduleDetailImageProps) {
  return (
    <div className="p-1">
      <Image
        src={src}
        alt={alt}
        width={24}
        height={24}
        unoptimized
      />
    </div>
  );
}