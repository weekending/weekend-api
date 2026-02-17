import { useQuery } from "@tanstack/react-query";
import getSchedules from "@features/schedule/requests/getSchedules";
import getSongs from "@features/song/requests/getSongs";
import getNoticeList from "@features/notice/requests/getNoticeList";
import HomeHeader from "./HomeHeader";
import HomeNotice from "./HomeNotice";
import HomeSchedule from "./HomeSchedule"
import HomeSong from "./HomeSong";

export default function Home() {
  const today = new Date();
  const endDate = new Date(today.getFullYear(), today.getMonth() + 3, 0);

  const { data: songs = [] } = useQuery({
    queryKey: ["home", "songs", "INPROGRESS"],
    queryFn: () => getSongs({bandId: 1, status: "INPROGRESS"}).then(res => res.data.data),
  });

  const { data: schedules = [] } = useQuery({
    queryKey: ["home", "schedules", today.toISOString().slice(0, 10)],
    queryFn: () => getSchedules(1, today.toISOString().slice(0, 10), endDate.toISOString().slice(0, 10)).then(res => res.data.data),
  });

  const { data: notices = [] } = useQuery({
    queryKey: ["home", "notices"],
    queryFn: () => getNoticeList(1).then(res => res.data.data),
  });

  return (
    <>
      <HomeHeader/>
      <HomeSong songs={songs} />
      <HomeSchedule schedules={schedules} />
      <HomeNotice notices={notices} />
    </>
  )
}
