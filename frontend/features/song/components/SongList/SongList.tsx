"use client";
import { useEffect, useState } from "react";
import Nav from "@features/common/components/Nav";
import Wrapper from "@features/common/components/Wrapper";
import getSongs from "@features/song/requests/getSongs";
import { TSongs, Status } from "@features/song/types";
import { statusChoices } from "@features/song/utils";
import SongItem from "./SongItem";

export default function SongList() {
  const [status, setStatus] = useState<Status | null>(null);
  const [songs, setSongs] = useState<TSongs[]>([]);

  useEffect(() => {
    (async () => {
      const response = await getSongs(1, status);
      setSongs(response.data.data);
    })();
  }, [status]);

  return (
    <>
      <Nav/>
      <Wrapper>
        <div className="mt-18 md:mt-24 p-3 text-center">
          <h1 className="text-[36px] md:text-[42px] font-bold">SONGS</h1>
        </div>
        <div className="flex p-4">
          {statusChoices.map((choice, idx) => (
            <button
              key={idx}
              className={`p-2 text-[#404040] cursor-pointer ${choice.status === status ? "font-bold border-b-2" : ""}`}
              onClick={() => setStatus(choice.status)}
            >
              {choice.text}
            </button>
          ))}
        </div>
        <div className="grid md:grid-cols-4 lg:grid-cols-5 gap-3 md:gap-5 p-4">
          {songs.map((song, idx) => (
            <SongItem
              key={idx}
              song={song}
            />
          ))}
        </div>
      </Wrapper>
    </>
  );
}
