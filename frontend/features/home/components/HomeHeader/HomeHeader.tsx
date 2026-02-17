import HomeSocial from "./HomeSocial";

export default function HomeHeader() {
  return (
    <div className="relative h-[85vh] min-h-[600px] flex items-center justify-center overflow-hidden">
      <img
        className="absolute inset-0 w-full h-full object-cover"
        src="/img/weekend-banner.jpg"
        alt="윅엔드"
      />
      <div className="absolute inset-0 bg-foreground/60" />

      <div className="relative z-10 text-center px-5">
        <h1 className="text-5xl md:text-7xl font-bold text-background mb-4 animate-fade-in-up">
          RUNNING!
        </h1>
        <p className="text-base md:text-lg text-background/80 max-w-lg mx-auto mb-8 animate-fade-in-up">
          Not professionals, but passionate.<br/>Not stars, but shining together.
        </p>
        <HomeSocial/>
      </div>
    </div>
  );
}
