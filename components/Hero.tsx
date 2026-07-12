"use client";

import dynamic from "next/dynamic";
import { motion } from "framer-motion";
import Image from "next/image";
import { CTA } from "./CTA";
import { Icon } from "./Icons";
import { Countdown } from "./Countdown";
import { EVENT, EVENT_META, HERO_INCLUDES, CTAS } from "@/lib/site";

// הסצנה התלת-ממדית נטענת רק בצד הלקוח
const Scene = dynamic(() => import("./Scene"), { ssr: false });

const iconFor: Record<string, string> = {
  calendar: "calendar",
  clock: "clock",
  pin: "pin",
  split: "split",
  users: "users",
  alert: "alert",
};

export function Hero() {
  return (
    <header className="relative overflow-hidden" style={{ background: "radial-gradient(120% 90% at 50% -10%, #14110a 0%, #000 60%)" }}>
      {/* גריד מחברת */}
      <div className="absolute inset-0 grid-bg grid-bg-fade" aria-hidden />

      {/* סצנה תלת-ממדית — עמומה יותר במובייל לשמירה על קריאות */}
      <div className="absolute inset-0 z-0 opacity-55 sm:opacity-100" aria-hidden>
        <Scene />
      </div>

      {/* שכבת קריאוּת — חזקה יותר במובייל */}
      <div className="absolute inset-0 z-0 pointer-events-none sm:hidden" style={{ background: "radial-gradient(75% 60% at 50% 42%, rgba(0,0,0,0.78) 0%, rgba(0,0,0,0.5) 55%, rgba(0,0,0,0.2) 100%)" }} aria-hidden />
      <div className="absolute inset-0 z-0 pointer-events-none hidden sm:block" style={{ background: "radial-gradient(70% 55% at 50% 55%, rgba(0,0,0,0.55) 0%, rgba(0,0,0,0.15) 55%, transparent 100%)" }} aria-hidden />

      <div className="relative z-10 mx-auto max-w-5xl px-5 pt-8 pb-24 text-center">
        {/* לוגו */}
        <motion.div
          initial={{ opacity: 0, y: -12 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6 }}
          className="flex justify-center"
        >
          <Image src="/logo-white.png" alt="הכפלה עסקית — איתמר שולם" width={150} height={64} priority className="h-14 w-auto opacity-95" />
        </motion.div>

        {/* תג תאריך */}
        <motion.div
          initial={{ opacity: 0, y: 16 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, delay: 0.15 }}
          className="mt-9 flex justify-center"
        >
          <span className="pill">
            <span className="live-dot" /> {EVENT.dateLabel} · {EVENT.location}
          </span>
        </motion.div>

        {/* כותרת על */}
        <motion.p
          initial={{ opacity: 0, y: 16 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, delay: 0.25 }}
          className="mt-6 text-lg sm:text-xl font-bold text-[#d8d4cd]"
        >
          בעל עסק, הגיע הזמן להפסיק לרדוף אחרי העסק שלך
        </motion.p>

        {/* כותרת ראשית */}
        <motion.h1
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.7, delay: 0.32 }}
          className="mt-3 font-extrabold tracking-tight"
          style={{ fontSize: "clamp(2.4rem, 7vw, 4.6rem)", lineHeight: 1.02 }}
        >
          ולהתחיל לבנות <span className="text-gold">עסק שיודע לגדול.</span>
        </motion.h1>

        <motion.p
          initial={{ opacity: 0, y: 16 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, delay: 0.42 }}
          className="mx-auto mt-6 max-w-2xl text-[1.05rem] sm:text-lg text-[var(--muted)]"
        >
          לערב אחד אנחנו מרכזים בבית שמש את האנשים, הידע, החדשנות והחיבורים
          שיכולים לקחת את העסק שלך לרמה הבאה. האירוע העסקי שנבנה במיוחד לבעלי
          עסקים במגזר החרדי — שרוצים לקחת שליטה, לייצר סדר ולבנות מנגנונים
          שמביאים צמיחה אמיתית.
        </motion.p>

        {/* ספירה לאחור */}
        <motion.div
          initial={{ opacity: 0, y: 16 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, delay: 0.5 }}
          className="mt-9 flex justify-center"
        >
          <Countdown />
        </motion.div>

        {/* CTA */}
        <motion.div
          initial={{ opacity: 0, y: 16 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, delay: 0.58 }}
          className="mt-8 flex flex-col items-center gap-3"
        >
          <CTA>{CTAS.hero}</CTA>
          <span className="text-sm text-[var(--muted-2)]">
            השאירו פרטים עכשיו ושמרו לעצמכם מקום לפני סגירת ההרשמה.
          </span>
        </motion.div>

        {/* מטא chips */}
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 0.6, delay: 0.7 }}
          className="mt-10 flex flex-wrap justify-center gap-2.5"
        >
          {EVENT_META.map((m) => (
            <span
              key={m.text}
              className="inline-flex items-center gap-2 rounded-full border border-[var(--line)] bg-white/[0.02] px-3.5 py-2 text-sm text-[#cfcbc3]"
            >
              <Icon name={iconFor[m.icon]} width={16} height={16} className="text-[var(--gold-3)]" />
              {m.text}
            </span>
          ))}
        </motion.div>
      </div>

      {/* רשימת מה מחכה לך */}
      <div className="relative z-10 border-t border-[var(--line)] bg-black/40 backdrop-blur-sm">
        <div className="mx-auto max-w-4xl px-5 py-8">
          <p className="text-center text-sm font-bold uppercase tracking-widest text-[var(--gold-2)]">
            בערב אחד מחכים לך
          </p>
          <ul className="mt-5 grid gap-x-8 gap-y-3 sm:grid-cols-2">
            {HERO_INCLUDES.map((item, i) => (
              <motion.li
                key={i}
                initial={{ opacity: 0, x: -12 }}
                whileInView={{ opacity: 1, x: 0 }}
                viewport={{ once: true }}
                transition={{ duration: 0.4, delay: i * 0.05 }}
                className="flex items-start gap-3 text-[#d8d4cd]"
              >
                <span className="mt-1 flex h-5 w-5 flex-shrink-0 items-center justify-center rounded-full gold-fill">
                  <Icon name="check" width={13} height={13} className="text-black" />
                </span>
                <span>{item}</span>
              </motion.li>
            ))}
          </ul>
        </div>
      </div>
    </header>
  );
}
