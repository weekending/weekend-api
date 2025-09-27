import ScheduleDetailLogo from "../ScheduleDetailLogo";

type ScheduleDetailMemoProps = {
  memo: string;
};

export default function ScheduleDetailMemo({ memo }: ScheduleDetailMemoProps) {
  return (
    <div className="flex gap-2 mb-1">
      <ScheduleDetailLogo src="/img/memo.png" alt="memo"/>
      <div className="flex-1 p-1 text-[#808080] leading-6">
        {memo.split("\n").map((line, idx) => (
          <p className="min-h-5" key={idx}>{line}</p>
        ))}
      </div>
    </div>
  );
}
