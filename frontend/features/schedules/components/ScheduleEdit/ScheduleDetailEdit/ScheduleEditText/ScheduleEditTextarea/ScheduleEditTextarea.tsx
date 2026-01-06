type ScheduleEditTextareaProps = React.TextareaHTMLAttributes<HTMLTextAreaElement>;

export default function ScheduleEditTextarea( props: ScheduleEditTextareaProps) {
  return <textarea
    className="flex-1 p-2 border-1 border-[#CCCCCC] rounded-lg text-[#404040] resize-none"
    {...props}
  />;
}
