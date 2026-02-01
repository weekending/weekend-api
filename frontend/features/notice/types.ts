export type TNoticeImage = {
  id: number;
  type: string;
  image_url: string | null;
  link: string | null;
  sequence: number;
}


export type TNotice = {
  id: number;
  title: string;
  content: string;
  images: TNoticeImage[];
  created_dtm: string;
}
