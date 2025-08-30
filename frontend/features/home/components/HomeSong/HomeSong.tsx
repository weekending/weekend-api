import Link from "next/link";
import { TSongs } from "@features/song/types";
import HomeSongItem from "./HomeSongItem";

type HomeSongProps = {
  songs: TSongs[];
};

export default function HomeSong({ songs }: HomeSongProps) {
  return (
    <div className="block md:flex md:gap-8 p-5">
      <div className="flex-1 mb-12">
        <h2 className="mb-5 text-[36px] md:text-[42px] font-bold">진행중인 연습곡</h2>
        <div className="max-w-[400px]">
          <p className="text-[18px]">저희 밴드는 감성적인 얼터너티브 록부터, 파워플한 브릿팝까지 다양한 장르를 넘나들며 노래하고 있습니다.</p>
        </div>
      </div>
      <div className="flex-1">
        <div className="grid grid-cols-3 gap-4 pb-4">
          {songs.map((song, idx) => (
            <HomeSongItem
              key={idx}
              title={song.title}
              singer={song.singer}
              image={song.thumbnail}
            />
          ))}
        </div>
        <div className="pt-2 border-t">
          <div className="p-2 text-right">
            <Link href="/songs">
              <p>더 많은 곡 보기</p>
            </Link>
          </div>
        </div>
      </div>
    </div>
  )
}
