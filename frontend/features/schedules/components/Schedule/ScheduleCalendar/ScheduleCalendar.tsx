import { DayPicker } from "react-day-picker";

type ScheduleCalendarProps = {
  setMonth: React.Dispatch<React.SetStateAction<Date>>;
  scheduleDates: Date[];
};

export default function ScheduleCalendar({ setMonth, scheduleDates }: ScheduleCalendarProps) {
  return (
    <DayPicker
      mode="single"
      onMonthChange={setMonth}
      modifiers={{
        highlight: scheduleDates,
      }}
      modifiersClassNames={{
        highlight: "highlight",
      }}
      classNames={{
        months: "relative max-w-fit mx-auto",
        nav: "absolute top-0 right-0 flex h-[44px]",
        button_previous: "cursor-pointer",
        button_next: "cursor-pointer",
        month_caption: "flex items-center h-[44px] text-[20px] font-semibold",
        weekday: "py-2 text-[14px] font-semibold",
        month_grid: "border-separate border-spacing-3 sm:border-spacing-4 lg:border-spacing-5",
        weeks: "w-full",
        day: "w-10 text-center",
        day_button: "w-8 md:w-10 h-8 md:h-10 text-center",
        today: "font-bold",
        selected: "",
      }}
    />
  );
}
