import { Status } from "@features/song/types";

type StatusItem = {
  status: Status | null;
  text: string;
};

export const statusChoices: StatusItem[] = [
  { status: null, text: "전체" },
  { status: Status.PENDING, text: "대기" },
  { status: Status.INPROGRESS, text: "연습중" },
  { status: Status.CLOSED, text: "종료" },
];
