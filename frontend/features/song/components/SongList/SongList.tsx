import { useEffect, useState, useRef, useCallback } from "react";
import { useSearchParams, useRouter } from "next/navigation";
import getSongs from "@features/song/requests/getSongs";
import { TSong, Status } from "@features/song/types";
import { statusChoices } from "@features/song/utils";
import SongItem from "./SongItem";

export default function SongList() {
  const [songs, setSongs] = useState<TSong[]>([]);
  const [hasMore, setHasMore] = useState(true);
  const searchParams = useSearchParams();
  const router = useRouter();
  const status = searchParams.get("status") as Status | null;
  const observerRef = useRef<HTMLDivElement | null>(null);
  const pageRef = useRef(1);
  const loadingRef = useRef(false);

  const fetchSongs = useCallback(async (reset: boolean) => {
    if (loadingRef.current) return;
    loadingRef.current = true;
    const currentPage = reset ? 1 : pageRef.current;
    const response = await getSongs({ bandId: 1, status, page: currentPage });
    const data: TSong[] = response.data.data;

    if (data.length === 0) {
      setHasMore(false);
    } else {
      setSongs((prev) => reset ? data : [...prev, ...data]);
      pageRef.current = currentPage + 1;
    }
    loadingRef.current = false;
  }, [status]);

  useEffect(() => {
    setSongs([]);
    pageRef.current = 1;
    setHasMore(true);
    fetchSongs(true);
  }, [fetchSongs]);

  useEffect(() => {
    if (!hasMore) return;
    const observer = new IntersectionObserver((entries) => {
      if (entries[0].isIntersecting) {
        fetchSongs(false);
      }
    });
    const el = observerRef.current;
    if (el) observer.observe(el);
    return () => { if (el) observer.unobserve(el); };
  }, [hasMore, fetchSongs]);

  return (
    <div className="pt-18">
      <div className="w-full mx-auto max-w-[1080px] p-5">
        <h1 className="text-2xl font-bold mb-8">SONGS</h1>
        <div className="flex pb-6">
          {statusChoices.map((choice, idx) => (
            <button
              key={idx}
              className={`p-2 text-[#404040] cursor-pointer ${choice.status === status ? "font-bold border-b-2" : ""}`}
              onClick={() => router.push(choice.status ? `?status=${choice.status}` : "/songs/list")}
            >
              {choice.text}
            </button>
          ))}
        </div>
        <div className="grid md:grid-cols-4 lg:grid-cols-5 gap-3 md:gap-5">
          {songs.map((song, idx) => (
            <SongItem
              key={idx}
              song={song}
            />
          ))}
        </div>
        {hasMore && <div ref={observerRef} className="h-10" />}
      </div>
    </div>
  );
}
