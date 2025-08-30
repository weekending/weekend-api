interface HomeSongItemProps {
  title: string;
  singer: string;
  image: string;
}

export default function HomeSongItem({title, singer, image}: HomeSongItemProps) {
  return (
    <div className="items-center">
      <div>
        <img
          src={image}
          alt="weekend"
          width={240}
          height={240}
        />
      </div>
    </div>
  )
}
