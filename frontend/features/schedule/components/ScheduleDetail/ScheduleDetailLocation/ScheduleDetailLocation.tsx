import { MapPin } from "lucide-react";

type ScheduleDetailLocationProps = {
  location: string;
};

export default function ScheduleDetailLocation({ location }: ScheduleDetailLocationProps) {
  return (
    <div className="flex items-start gap-2 mb-6">
      <MapPin size={18} className="text-gray-6 shrink-0 mt-0.5" />
      <p>{location}</p>
    </div>
  );
}
