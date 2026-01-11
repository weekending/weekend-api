import Image from "next/image";

type AddButtonProps = {
  onClick: () => void;
  icon?: string;
  ariaLabel?: string;
};

export default function AddButton({
  onClick,
  icon = "/img/plus-gray.svg",
  ariaLabel = "추가"
}: AddButtonProps) {
  return (
    <button
      onClick={onClick}
      className="fixed bottom-6 right-6 w-14 h-14 bg-white rounded-full shadow-2xl transition-all flex items-center justify-center text-2xl border border-gray-200 cursor-pointer"
      aria-label={ariaLabel}
    >
      <Image
        className="rounded-sm"
        src={icon}
        alt={ariaLabel}
        width={50}
        height={150}
      />
    </button>
  );
}
