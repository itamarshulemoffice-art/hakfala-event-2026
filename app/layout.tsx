import type { Metadata } from "next";
import { Assistant } from "next/font/google";
import "./globals.css";

const assistant = Assistant({
  variable: "--font-assistant",
  subsets: ["hebrew", "latin"],
  weight: ["400", "500", "600", "700", "800"],
  display: "swap",
});

export const metadata: Metadata = {
  metadataBase: new URL("https://itamarshulem.co.il"),
  title: "אירוע הכפלה עסקית 2026 | 20.07 · בית שמש",
  description:
    "ערב אחד שמרכז ידע, תוכנית ואנשים כדי לקחת את העסק שלך לרמה הבאה. הרצאת AI ושיווק של יוסי לוי, פאנל מומחים, הרצאת ההכפלה של איתמר שולם וצוות יועצים. בהפרדה, לגברים ולנשים. מספר המקומות מוגבל.",
  openGraph: {
    title: "אירוע הכפלה עסקית 2026",
    description:
      "האירוע העסקי שנבנה במיוחד לבעלי עסקים במגזר החרדי. 20.07.2026 · בית שמש.",
    type: "website",
    locale: "he_IL",
  },
  robots: { index: true, follow: true },
};

export default function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="he" dir="rtl" className={`${assistant.variable} antialiased`}>
      <body>{children}</body>
    </html>
  );
}
