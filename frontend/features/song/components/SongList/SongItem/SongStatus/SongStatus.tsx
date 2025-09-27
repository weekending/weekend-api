import { Status } from "@features/song/types";

interface SongStatusProps {
  status: Status;
}

export default function SongStatus({ status }: SongStatusProps) {
  switch (status) {
    case Status.PENDING:
      return (
        <div className="px-2 border-1 border-[#A2CED1] rounded-xl text-[#509A9F]">
          <p>대기</p>
        </div>
      );
    case Status.INPROGRESS:
      return (
        <div className="px-2 border-1 border-[#DFA1A1] rounded-xl text-[#B46363]">
          <p>연습중</p>
        </div>
      );
    case Status.CLOSED:
      return (
        <div className="px-2 border-1 border-[#CCCCCC] rounded-xl text-[#808080]">
          <p>종료</p>
        </div>
      );
  }
}
