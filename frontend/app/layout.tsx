import type { Metadata } from "next";
import localFont from "next/font/local";
import Providers from "./providers";
import "./globals.css";

export const metadata: Metadata = {
  title: "윅엔드",
  description: "평일에는 회사, 주말에는 밴드~ 음악으로 주말을 책임지는 WEEK-END 🎶",
  keywords: "윅엔드, weekend, 밴드, 직장인 밴드",
  openGraph: {
    title: "윅엔드",
    description: "평일에는 회사, 주말에는 밴드~ 음악으로 주말을 책임지는 WEEK-END 🎶",
    url: "https://weekend.miintto.com",
    siteName: "윅엔드",
    images: [
      {
        url: "https://weekend.miintto.com/img/meta-og.png",
        width: 1000,
        height: 540,
      },
    ],
    locale: "ko_KR",
    type: "website",
  },
};

const pretendard = localFont({
  src: "../public/fonts/PretendardVariable.woff2",
  display: "swap",
  weight: "45 920",
  variable: "--font-pretendard",
});

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="ko" className={`${pretendard.variable}`}>
      <body className={`flex flex-col min-h-screen ${pretendard.className}`}>
        <Providers>{children}</Providers>
      </body>
    </html>
  );
}
