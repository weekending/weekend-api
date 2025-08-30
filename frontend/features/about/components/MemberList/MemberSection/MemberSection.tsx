import Image from "next/image";

export type TMember = {
  name: string;
  image: string;
  position: string;
};

type MemberSectionProps = {
  member: TMember;
  onClick: React.MouseEventHandler<HTMLDivElement>;
  isActive: boolean;
};

export default function MemberSection({ member, onClick, isActive }: MemberSectionProps) {
  return (
    <>
      <div className="cursor-pointer p-2" onClick={onClick}>
        <h2 className={`text-[28px] md:text-[36px] lg:text-[48px] font-bold ${isActive ? "" : "md:text-[#C0C0C0]"}`}>
          {member.name}
        </h2>
      </div>
      <div className="flex-1 block md:hidden pb-10">
        <Image
          src={member.image}
          alt="profile"
          width={600}
          height={750}
          unoptimized
        />
      </div>
    </>
  )
}
