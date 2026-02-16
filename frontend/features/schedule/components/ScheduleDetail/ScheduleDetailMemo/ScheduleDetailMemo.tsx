type ScheduleDetailMemoProps = {
  memo: string;
};

export default function ScheduleDetailMemo({ memo }: ScheduleDetailMemoProps) {
  return (
    <div className="rounded-lg bg-gray-1 p-4 mb-6">
      <p className="text-sm font-medium mb-1.5 text-gray-5">메모</p>
      <div className="flex-1 p-1 text-gray-6">
        {memo.split("\n").map((line, idx) => (
          <p key={idx}>{line}</p>
        ))}
      </div>
    </div>
  );
}
