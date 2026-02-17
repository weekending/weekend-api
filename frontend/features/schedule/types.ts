import { TSong } from "@features/song/types";

export type TSchedule = {
  id: number;
  title: string;
  day: string;
  weekday: string;
  start_time: string;
  end_time: string;
  location: string;
  memo: string;
  is_active: boolean;
  songs: TSong[];
}
