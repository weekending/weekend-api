interface WrapperProps {
  children: React.ReactNode;
}

export default function Wrapper({ children }: WrapperProps) {
  return (
    <div className="flex justify-center min-h-screen">
      <div className="w-full max-w-[1080]">
        {children}
      </div>
    </div>
  );
}
