import Link from "next/link";
import { ChevronRight } from "lucide-react"
import { TSong } from "@features/song/types";
import SongSectionVerticalItem from "./SongSectionVerticalItem";

type SongSectionProps = {
  title: string;
  songs: TSong[];
};

export default function SongSectionVertical({ title, songs }: SongSectionProps) {
  return (
    <div className="md:flex-1 min-w-0">
      <div className="flex items-center justify-between mb-4">
        <h2 className="text-lg font-semibold">{title}</h2>
        <Link
          href="/songs"
          className="flex items-center gap-0.5 text-sm text-gray-6 hover:text-foreground transition-colors"
        >
          전체보기
          <ChevronRight size={16} />
        </Link>
      </div>
      <div className="divide-y divide-border">
        {songs.map((song) => (
          <SongSectionVerticalItem key={song.id} song={song} />
        ))}
      </div>
    </div>
  );
}
