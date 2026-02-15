interface HomeSongItemProps {
  title: string;
  singer: string;
  image: string;
}

export default function HomeSongItem({title, singer, image}: HomeSongItemProps) {
  return (
    <div className="group overflow-hidden rounded-xl border border-gray-300 bg-card hover:border-primary/50 transition-all hover:shadow-md">
      <div className="aspect-square bg-gray-1 flex items-center justify-center overflow-hidden">
        <img
          className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300"
          src={image}
          alt="song"
          width={400}
          height={400}
        />
      </div>
      <div className="p-3.5">
        <p className="font-semibold text-[15px] truncate">{title}</p>
        <p className="text-sm text-gray-6">{singer}</p>
      </div>
    </div>
  )
}
