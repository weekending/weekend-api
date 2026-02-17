import { TSong } from "@features/song/types";

type SongItemProps = {
  song: TSong;
};

export default function SongSectionVerticalItem({ song }: SongItemProps) {
  return (
    <div className="flex items-center gap-3 py-3 border-gray-200">
      <div className="w-[60px] h-[60px] bg-gray-1 rounded-lg">
        <img
          className="rounded-lg object-cover flex-shrink-0 animate-fade-in"
          style={{ animationDelay: "300ms" }}
          src={song.thumbnail}
          alt={song.title}
        />
      </div>
      <div className="flex-1 min-w-0">
        <p className="font-semibold text-foreground truncate">{song.title}</p>
        <p className="text-sm text-gray-6 truncate">{song.singer}</p>
      </div>
    </div>
  );
}
