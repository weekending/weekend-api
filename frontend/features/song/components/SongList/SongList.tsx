"use client";
import { useEffect, useState } from "react";
import Nav from "@features/common/components/Nav";
import Template from "@features/common/components/Template";
import getSongs from "@features/song/requests/getSongs";
import { TSongs, Status } from "@features/song/types";
import SongItem from "./SongItem";

type StatusItem = {
  status: Status | null;
  text: string;
};

const statusChoices: StatusItem[] = [
  { status: null, text: "전체" },
  { status: Status.PEDNING, text: "대기" },
  { status: Status.INPROGRESS, text: "연습중" },
  { status: Status.CLOSED, text: "종료" },
];

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
      <Template>
        <div className="mt-18 md:mt-24 p-3 text-center">
          <h1 className="text-[36px] md:text-[42px] font-bold">SONGS</h1>
        </div>
        <div className="flex p-3">
          {statusChoices.map((choice, idx) => (
            <button
              key={idx}
              className={`p-2 text-[#404040] cursor-pointer ${choice.status === status ? "font-bold" : ""}`}
              onClick={() => setStatus(choice.status)}
            >
              {choice.text}
            </button>
          ))}
        </div>
        <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-5 p-4">
          {songs.map((song, idx) => (
            <SongItem
              key={idx}
              title={song.title}
              singer={song.singer}
              image={song.thumbnail}
            />
          ))}
        </div>
      </Template>
    </>
  )
}
