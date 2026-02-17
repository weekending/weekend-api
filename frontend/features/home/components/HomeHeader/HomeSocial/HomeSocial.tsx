import Image from "next/image";
import Link from "next/link";

type Social = {
  name: string;
  link: string;
  image: string;
}

const socialList: Social[] = [
  { name: "instagram", link: "https://www.instagram.com/band.weekend.official", image: "/img/instagram.svg" },
  { name: "youtube", link: "https://www.youtube.com/@%EC%9C%85%EC%97%94%EB%93%9C", image: "/img/youtube.svg" },
]

export default function HomeSocial() {
  return (
    <div className="flex justify-center gap-3 animate-fade-in-up">
      {socialList.map((social, idx) => (
        <Link
          className="p-3 rounded-full bg-background/10 hover:bg-white/30 transition-colors"
          key={idx}
          href={social.link}
          target="_blank"
        >
          <Image
            src={social.image}
            alt={social.name}
            width={20}
            height={20}
            unoptimized
          />
        </Link>
      ))}
    </div>
  );
}
