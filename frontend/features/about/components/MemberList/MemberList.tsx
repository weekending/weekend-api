import MemberSection from "./MemberSection";
import { TMember } from "./MemberSection/MemberSection";

const memberList: TMember[] = [
  { name: "KIM ANNA", position: "Base Guitar", image: "/img/members/anna.png" },
  { name: "JEONG DOYOUNG", position: "Vocal", image: "/img/members/do0.png" },
  { name: "PARK SOHEE", position: "Electric Guitar", image: "/img/members/sohee.png" },
  { name: "CHO HYEONGDEOK", position: "Electric Guitar", image: "/img/members/hdcho.png" },
  { name: "PARK MINJAE", position: "Drum", image: "/img/members/mjpark.png" },
];

export default function MemberList() {
  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-12 p-5">
      {memberList.map((member, idx) => (
        <MemberSection
          key={idx}
          member={member}
        />
      ))}
    </div>
  )
}
