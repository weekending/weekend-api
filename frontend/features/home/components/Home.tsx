import { useEffect, useState } from "react";
import getSchedules from "@features/schedules/requests/getSchedules";
import { TSchedule } from "@features/schedules/types";
import getSongs from "@features/song/requests/getSongs";
import { TSongs } from "@features/song/types";
import getNoticeList from "@features/notice/requests/getNoticeList";
import {TNotice} from "@features/notice/types"
import HomeHeader from "./HomeHeader";
import HomeNotice from "./HomeNotice";
import HomeSchedule from "./HomeSchedule"
import HomeSong from "./HomeSong";

export default function Home() {
  const [songs, setSongs] = useState<TSongs[]>([]);
  const [schedules, setSchedules] = useState<TSchedule[]>([]);
  const [notices, setNotices] = useState<TNotice[]>([]);

  useEffect(() => {
    const today = new Date()
    const endDate = new Date(today.getFullYear(), today.getMonth() + 3, 0);
    (async () => {
      const [songResp, scheduleResp, noticeResp] = await Promise.all([
        getSongs(1, "INPROGRESS"),
        getSchedules(1, today.toISOString().slice(0, 10), endDate.toISOString().slice(0, 10)),
        getNoticeList(1),
      ]);
      setSongs(songResp.data.data);
      setSchedules(scheduleResp.data.data);
      setNotices(noticeResp.data.data);
    })();
  }, []);

  return (
    <>
      <HomeHeader/>
      <HomeSong songs={songs} />
      <HomeSchedule schedules={schedules} />
      <HomeNotice notices={notices} />
    </>
  )
}
