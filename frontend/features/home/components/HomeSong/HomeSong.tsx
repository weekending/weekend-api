import { TSongs } from "@features/song/types";
import HomeSongItem from "./HomeSongItem";

type HomeSongProps = {
  songs: TSongs[];
};

export default function HomeSong({ songs }: HomeSongProps) {
  return (
    <div className="py-20">
      <div className="w-full mx-auto max-w-[1080px] p-5">
        <h2 className="text-2xl font-bold mb-2">현재 연습 중인 곡</h2>
        <p className="text-gray-6 mb-10">저희 밴드는 감성적인 얼터너티브 록부터, 파워플한 브릿팝까지 다양한 장르를 넘나들며 노래하고 있습니다.</p>
        <div className="flex-1">
          <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-4">
            {songs.map((song, idx) => (
              <HomeSongItem
                key={idx}
                title={song.title}
                singer={song.singer}
                image={song.thumbnail}
              />
            ))}
          </div>
        </div>
      </div>
    </div>
  )
}
