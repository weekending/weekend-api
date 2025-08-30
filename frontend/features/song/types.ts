export enum Status {
  PEDNING = "PENDING",
  INPROGRESS = "INPROGRESS",
  CLOSED = "CLOSED",
}

export type TSongs = {
  id: number;
  title: string;
  singer: string;
  thumbnail: string;
  status: Status;
  created_dtm: string;
  in_progress_dtm?: string;
  closed_dtm?: string;
}
