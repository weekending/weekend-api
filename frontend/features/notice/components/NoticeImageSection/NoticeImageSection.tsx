import { TNoticeImage } from "../../types";

type Props = {
  images: TNoticeImage[];
};

export default function NoticeImageSection({ images }: Props) {
  return (
    <div className="p-3 flex flex-col">
      {images
        .sort((a, b) => a.sequence - b.sequence)
        .map((img) =>
          img.image_url ? (
            <div key={img.id}>
              {img.link && img.type === "button" ? (
                <a href={img.link} target="_blank" rel="noopener noreferrer">
                  <img src={img.image_url} alt="" className="w-full" />
                </a>
              ) : (
                <img src={img.image_url} alt="" className="w-full" />
              )}
            </div>
          ) : null
        )}
    </div>
  );
}
