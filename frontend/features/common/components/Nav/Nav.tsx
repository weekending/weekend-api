import Image from "next/image";
import Link from "next/link";
import { useState } from "react";

export default function Nav() {
  const [open, setOpen] = useState(false);

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
        <div className={`overflow-hidden md:flex gap-5 w-full md:w-auto md:max-h-full text-[15px] font-semibold ${open ? "max-h-80" : "max-h-0"}`}>
          <div className="flex pt-3 md:pt-0">
            <Link href="/about" className="w-full p-2">
              ABOUT
            </Link>
          </div>
          <div className="flex">
            <Link href="/songs" className="w-full p-2">
              SONGS
            </Link>
          </div>
          <div className="flex">
            <Link href="/schedules" className="w-full p-2">
              SCHEDULES
            </Link>
          </div>
          <div className="flex">
            <Link href="/shop" className="w-full p-2">
              SHOP
            </Link>
          </div>
        </div>
      </div>
    </nav>
  )
}
