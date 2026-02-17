import { TSong } from "@features/song/types";

type SongSectionCardItemProps = {
  song: TSong;
};

export default function SongSectionCardItem({ song }: SongSectionCardItemProps) {
  return (
    <div className="items-center min-w-0">
      <div className="bg-gray-1 rounded-lg">
        <img
          className="w-full aspect-square rounded-lg object-cover mb-2 animate-fade-in"
          style={{ animationDelay: "300ms" }}
          src={song.thumbnail}
          alt={song.title}
        />
      </div>
      <div className="px-1">
        <p className="font-semibold text-foreground truncate w-full text-sm">{song.title}</p>
        <p className="text-sm text-gray-6 truncate w-full">{song.singer}</p>
      </div>
    </div>
  );
}
