import { useQuery } from "@tanstack/react-query";
import getSongs from "@features/song/requests/getSongs";
import SongSectionVertical from "./SongSectionVertical";
import SongSectionCard from "./SongSectionCard";

export default function Song() {
  const { data: pendingSongs = [] } = useQuery({
    queryKey: ["songs", "PENDING"],
    queryFn: () => getSongs({ bandId: 1, status: "PENDING", size: 6 }).then(res => res.data.data),
  });

  const { data: inProgressingSongs = [] } = useQuery({
    queryKey: ["songs", "INPROGRESS"],
    queryFn: () => getSongs({ bandId: 1, status: "INPROGRESS", size: 6 }).then(res => res.data.data),
  });

  const { data: closedSongs = [] } = useQuery({
    queryKey: ["songs", "CLOSED"],
    queryFn: () => getSongs({ bandId: 1, status: "CLOSED", size: 6 }).then(res => res.data.data),
  });

  return (
    <div className="pt-18">
      <div className="w-full mx-auto max-w-[1080px] p-5">
        <h1 className="text-2xl font-bold mb-8">SONGS</h1>
        <div className="mb-16">
          <SongSectionCard title="연습 중인 곡" songs={inProgressingSongs}/>
        </div>
        <div className="flex flex-col md:flex-row gap-12 mb-16">
          <SongSectionVertical title="대기" songs={pendingSongs} />
          <SongSectionVertical title="종료" songs={closedSongs} />
        </div>
      </div>
    </div>
  );
}
