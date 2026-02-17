import { TSong } from "@features/song/types";

type ScheduleDetailSongItemProps = {
  song: TSong;
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
        <p className="font-medium">{song.title}</p>
        <p className="text-sm text-gray-6">{song.singer}</p>
      </div>
    </div>
  );
}
