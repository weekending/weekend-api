import ScheduleDetailLogo from "@features/schedules/components/ScheduleDetail/ScheduleDetailLogo";
import ScheduleEditInput from "../ScheduleEditText/ScheduleEditInput";

type ScheduleDetailEditLocationProps = {
  location: string;
  onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
};

export default function ScheduleDetailEditLocation({ location, onChange }: ScheduleDetailEditLocationProps) {
  return (
    <div className="flex items-center gap-2 mb-5">
      <ScheduleDetailLogo src="/img/location.png" alt="location"/>
      <div className="flex-1 border-b-1 border-[#CCCCCC]">
        <ScheduleEditInput
          value={location}
          onChange={onChange}
          placeholder="장소"
        />
      </div>
    </div>
  );
}
