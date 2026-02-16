import { DayPicker } from "react-day-picker";
import { ko } from "date-fns/locale";

type ScheduleCalendarProps = {
  month: Date;
  setMonth: (date: Date) => void;
  scheduleDates: Date[];
};

export default function ScheduleCalendar({ month, setMonth, scheduleDates }: ScheduleCalendarProps) {
  return (
    <DayPicker
      mode="single"
      month={month}
      onMonthChange={setMonth}
      modifiers={{
        highlight: scheduleDates,
      }}
      modifiersClassNames={{
        highlight: "highlight",
      }}
      className="rounded-lg border border-gray-300 p-3 pointer-events-auto"
      classNames={{
        months: "relative max-w-fit mx-auto",
        nav: "absolute top-0 right-2 flex h-[36px]",
        button_previous: "cursor-pointer",
        button_next: "cursor-pointer",
        month_caption: "flex items-center h-[44px] p-2 text-[14px] font-semibold",
        weekday: "py-2 text-[14px] text-gray-6 font-normal",
        month_grid: "border-separate border-spacing-2",
        weeks: "w-full",
        day: "w-8 text-center text-sm",
        day_button: "w-8 h-8 text-center",
        today: "font-bold",
        selected: "",
      }}
      locale={ko}
    />
  );
}
