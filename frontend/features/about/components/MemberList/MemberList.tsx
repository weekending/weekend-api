import Image from "next/image";
import { useState } from "react";
import MemberSection from "./MemberSection";
import { TMember } from "./MemberSection/MemberSection";

const memberList: TMember[] = [
  { name: "ANNA KIM", position: "Base", image: "/img/members/anna.png" },
  { name: "DOYOUNG JEONG", position: "Vocal", image: "/img/members/do0.png" },
  { name: "SOHEE PARK", position: "Electric Guitar / Sub Vocal", image: "/img/members/sohee.png" },
  { name: "HYEONGDEOK CHO", position: "Electric Guitar", image: "/img/members/hdcho.png" },
  { name: "MINJAE PARK", position: "Drum", image: "/img/members/mjpark.png" },
];

export default function MemberList() {
  const [activeProfile, setActiveProfile] = useState(0);
  return (
     <div className="flex gap-10 mx-auto">
      <div className="flex-1 hidden md:block">
        <Image
          src={memberList[activeProfile].image}
          alt="profile"
          width={600}
          height={750}
          unoptimized
        />
      </div>
      <div className="flex-1">
        {memberList.map((member, idx) => (
          <MemberSection
            key={idx}
            member={member}
            onClick={() => setActiveProfile(idx)}
            isActive={idx === activeProfile}
          />
        ))}
      </div>
    </div>
  )
}
