"use client";
import { useEffect, useState } from "react";
import Nav from "@features/common/components/Nav";
import Template from "@features/common/components/Template";
import getSongs from "@features/song/requests/getSongs";
import { TSongs } from "@features/song/types";
import HomeBackground from "./HomeBackground";
import HomeSong from "./HomeSong";

export default function Home() {
  const [songs, setSongs] = useState<TSongs[]>([]);

  useEffect(() => {
    (async () => {
      const response = await getSongs(1, "INPROGRESS");
      setSongs(response.data.data);
    })();
  }, []);

  return (
    <>
      <Nav/>
      <HomeBackground/>
      <Template>
        <HomeSong songs={songs} />
      </Template>
    </>
  )
}
