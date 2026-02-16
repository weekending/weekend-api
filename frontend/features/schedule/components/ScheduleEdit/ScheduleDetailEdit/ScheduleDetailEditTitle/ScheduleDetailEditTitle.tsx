import ScheduleEditInput from "../ScheduleEditText/ScheduleEditInput";

type ScheduleDetailEditTitleProps = {
  title: string;
  onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
};

export default function ScheduleDetailEditTitle({ title, onChange }: ScheduleDetailEditTitleProps) {
  return (
    <div className="flex ml-10 pb-4 text-[20px] font-semibold">
      <div className="flex-1 border-b-1 border-[#CCCCCC]">
        <ScheduleEditInput
          value={title}
          onChange={onChange}
          placeholder="일정을 입력하세요"
        />
      </div>
    </div>
  );
}
