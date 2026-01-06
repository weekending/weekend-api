export default function AuthWrapper({ children }: { children: React.ReactNode }) {
  return (
    <div className="w-full max-w-[400px] mx-auto p-4">
      {children}
    </div>
  );
}
