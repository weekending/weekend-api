type ScheduleEditInputProps = React.InputHTMLAttributes<HTMLInputElement>;

export default function ScheduleEditInput(props: ScheduleEditInputProps) {
  return <input
    className="w-full p-1 text-[#202020] focus:outline-none placeholder-[#A0A0A0]"
    {...props}
  />;
}
