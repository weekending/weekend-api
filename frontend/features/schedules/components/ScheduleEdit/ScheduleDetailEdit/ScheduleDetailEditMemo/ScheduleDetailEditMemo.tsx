import ScheduleDetailLogo from "@features/schedules/components/ScheduleDetail/ScheduleDetailLogo";
import ScheduleEditTextarea from "../ScheduleEditText/ScheduleEditTextarea";

type ScheduleDetailMemoProps = {
  memo: string;
  onChange: (e: React.ChangeEvent<HTMLTextAreaElement>) => void;
};

export default function ScheduleDetailEditMemo({ memo, onChange }: ScheduleDetailMemoProps) {
  return (
    <div className="flex gap-2 mb-1">
      <ScheduleDetailLogo src="/img/memo.png" alt="memo"/>
      <ScheduleEditTextarea value={memo} onChange={onChange} rows={6} placeholder="메모 입력"/>
    </div>
  );
}
