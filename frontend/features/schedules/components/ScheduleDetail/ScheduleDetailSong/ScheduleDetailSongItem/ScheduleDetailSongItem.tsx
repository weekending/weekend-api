import { TSongs } from "@features/song/types";

type ScheduleDetailSongItemProps = {
  song: TSongs;
};

export default function ScheduleDetailSongItem({ song }: ScheduleDetailSongItemProps) {
  return (
    <div className="flex mb-2 items-center">
      <div className="w-[48px] mr-3">
        <img
          className="rounded-sm"
          src={song.thumbnail}
          alt="weekend"
          width={100}
          height={100}
        />
      </div>
      <div className="leading-[1.2]">
        <p className="pb-1 text-[14px]">{song.title}</p>
      </div>
    </div>
  );
}
