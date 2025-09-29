import { TSongs } from "@features/song/types";
import ScheduleDetailSongItem from "./ScheduleDetailSongItem";
import ScheduleDetailLogo from "../ScheduleDetailLogo";

type ScheduleDetailSongProps = {
  songs: TSongs[];
};

export default function ScheduleDetailSong({ songs }: ScheduleDetailSongProps) {
  return (
    <>
      <div className="flex gap-2">
        <ScheduleDetailLogo src="/img/song.png" alt="song" />
        <div className="p-1">
          <p>연습곡 <span>{songs.length}개</span></p>
          <div className="py-4">
            {songs.map((song, idx) => (
              <ScheduleDetailSongItem key={idx} song={song} />
            ))}
          </div>
        </div>
      </div>
    </>
  );
}
