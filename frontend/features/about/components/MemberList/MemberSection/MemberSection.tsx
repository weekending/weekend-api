import Image from "next/image";

export type TMember = {
  name: string;
  image: string;
  position: string;
};

type MemberSectionProps = {
  member: TMember;
};

export default function MemberSection({ member }: MemberSectionProps) {
  return (
    <div className="shadow-lg pb-10">
      <div className="pb-1">
        <Image
          src={member.image}
          alt="profile"
          width={600}
          height={750}
          unoptimized
        />
      </div>
      <div className="p-4">
        <h2 className={`text-[28px] font-bold`}>{member.name}</h2>
        <p className="text-[16px]">{member.position}</p>
      </div>
    </div>
  )
}
