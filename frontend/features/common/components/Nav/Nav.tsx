import Image from "next/image";
import Link from "next/link";
import { useEffect, useState } from "react";

export type Menu = {
  name: string;
  link: string;
};

const menuList: Menu[] = [
  { name: "ABOUT", link: "/about" },
  { name: "SONGS", link: "/songs" },
  { name: "SCHEDULES", link: "/schedules" },
  { name: "NOTICE", link: "/notice" },
  { name: "SHOP", link: "/shop" },
]

export default function Nav() {
  const [open, setOpen] = useState(false);

  useEffect(() => {
    if (open) {
      document.body.classList.add("no-scroll");
    } else {
      document.body.classList.remove("no-scroll");
    }
  }, [open]);

  return (
    <nav className="fixed w-full border-b border-gray-300 bg-white z-999">
      <div className="flex flex-wrap justify-between max-w-[1080] ml-auto mr-auto p-2">
        <div>
          <Link href="/">
            <Image
              src="/img/weekend.png"
              alt="weekend"
              width={120}
              height={0}
              style={{ height: 'auto', objectFit: 'cover'}}
              unoptimized
            />
          </Link>
        </div>
        <button className="block md:hidden" onClick={() => setOpen(!open)}>
          <Image src="/img/menu.svg" alt="menu" width={30} height={30}/>
        </button>
        <div className={`overflow-hidden md:flex gap-5 w-full md:w-auto md:max-h-full font-semibold ${open ? "h-screen pt-6" : "max-h-0"}`}>
          {menuList.map((menu, idx) => (
            <div key={idx} className="flex">
              <Link href={menu.link} className="w-full px-4 py-2 md:p-2 text-[18px] md:text-[15px]">{menu.name}</Link>
            </div>
          ))}
        </div>
      </div>
    </nav>
  );
}
