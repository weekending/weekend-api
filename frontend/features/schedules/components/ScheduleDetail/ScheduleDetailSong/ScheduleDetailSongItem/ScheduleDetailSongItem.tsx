import { TSongs } from "@features/song/types";

type ScheduleDetailSongItemProps = {
  song: TSongs;
};

export default function ScheduleDetailSongItem({ song }: ScheduleDetailSongItemProps) {
  return (
    <div className="flex mb-3 items-center">
      <div className="w-[60px] mr-3">
        <img
          className="rounded-md"
          src={song.thumbnail}
          alt="weekend"
          width={240}
          height={240}
        />
      </div>
      <div className="leading-[1.2]">
        <p className="pb-2 text-[16px]">{song.title}</p>
        <p className="text-[14px] text-[#808080]">{song.singer}</p>
      </div>
    </div>
  );
}
