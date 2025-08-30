type ButtonProps = React.ButtonHTMLAttributes<HTMLButtonElement>;

export default function Button({ children, ...props }: ButtonProps) {
  return (
    <button className="w-full h-12 rounded bg-[#404040] text-white cursor-pointer disabled:opacity-20" {...props}>
      {children}
    </button>
  );
}
