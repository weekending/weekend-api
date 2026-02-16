import { TSongs } from "@features/song/types";
import ScheduleDetailSongItem from "./ScheduleDetailSongItem";

type ScheduleDetailSongProps = {
  songs: TSongs[];
};

export default function ScheduleDetailSong({ songs }: ScheduleDetailSongProps) {
  return (
    <div>
      <p className="text-sm font-medium text-gray-6 mb-3">연습곡 ({songs.length}개)</p>
      <div className="space-y-2.5">
        {songs.map((song, idx) => (
          <ScheduleDetailSongItem key={idx} song={song} />
        ))}
      </div>
    </div>
  );
}
