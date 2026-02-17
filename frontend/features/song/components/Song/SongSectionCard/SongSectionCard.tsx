import Link from "next/link";
import { ChevronRight } from "lucide-react"
import { TSong } from "@features/song/types";
import SongSectionCardItem from "./SongSectionCardItem";

type SongSectionCardProps = {
  title: string;
  songs: TSong[];
  link: string;
};

export default function SongSectionCard({ title, songs, link }: SongSectionCardProps) {
  return (
    <>
      <div className="flex items-center justify-between mb-4">
        <h2 className="text-lg font-semibold">{title}</h2>
        <Link
          href={link}
          className="flex items-center gap-0.5 text-sm text-gray-6 hover:text-foreground transition-colors"
        >
          전체보기
          <ChevronRight size={16} />
        </Link>
      </div>
      <div className="grid grid-cols-3 md:grid-cols-4 lg:grid-cols-6 gap-3 md:gap-4">
        {songs.map((song) => (
          <SongSectionCardItem key={song.id} song={song} />
        ))}
      </div>
    </>
  );
}
