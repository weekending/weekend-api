interface SongSectionProps {
  title: string;
  singer: string;
  image: string;
}

export default function SongItem({title, singer, image}: SongSectionProps) {
  return (
    <div className="items-center pb-8">
      <div className="pb-2">
        <img
          src={image}
          alt="weekend"
          width={300}
          height={300}
        />
      </div>
      <div className="">
        <h2 className="text-[18px] font-semibold">{title}</h2>
        <p className="text-[15px]">{singer}</p>
      </div>
    </div>
  )
}
