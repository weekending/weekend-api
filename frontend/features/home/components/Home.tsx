import { useEffect, useState } from "react";
import getSongs from "@features/song/requests/getSongs";
import { TSongs } from "@features/song/types";
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
    <HomeSong songs={songs} />
  )
}
