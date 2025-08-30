export default function AuthWrapper({ children }: { children: React.ReactNode }) {
  return (
    <div className="max-w-[400px] mx-auto">
      {children}
    </div>
  );
}
