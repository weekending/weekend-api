import { TSong } from "@features/song/types";
import SongStatus from "./SongStatus";

interface SongItemProps {
  song: TSong;
}

export default function SongItem({ song }: SongItemProps) {
  return (
    <div className="flex md:block items-center min-w-0">
      <div className="w-[60px] md:w-auto mr-3 md:mr-0 mb-0 md:mb-2">
        <img
          className="rounded-md"
          src={song.thumbnail}
          alt="weekend"
          width={240}
          height={240}
        />
      </div>
      <div className="min-h-auto md:min-h-[120px] flex md:block flex-1 justify-between p-1 min-w-0 gap-2">
        <div className="pb-0 md:pb-2 leading-[1.2] flex-1 min-w-0">
          <h2 className="font-semibold text-foreground truncate">{song.title}</h2>
          <p className="text-sm text-gray-6 truncate">{song.singer}</p>
        </div>
        <div className="inline-block text-[13px]">
          <SongStatus status={song.status} />
        </div>
      </div>
    </div>
  );
}
