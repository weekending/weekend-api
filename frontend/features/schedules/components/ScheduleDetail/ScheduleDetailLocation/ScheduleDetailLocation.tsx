import ScheduleDetailLogo from "../ScheduleDetailLogo";

type ScheduleDetailLocationProps = {
  location: string;
};

export default function ScheduleDetailLocation({ location }: ScheduleDetailLocationProps) {
  return (
    <div className="flex gap-2 mb-1">
      <ScheduleDetailLogo src="/img/location.png" alt="location" />
      <p className="flex-1 p-1 text-[16px] leading-6">{location}</p>
    </div>
  );
}
