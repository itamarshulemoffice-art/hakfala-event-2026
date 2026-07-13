import type { Metadata } from "next";
import Image from "next/image";
import { Reveal, Stagger, Item } from "@/components/Reveal";
import { SpeakerImage } from "@/components/pisga/SpeakerImage";
import { SpeakerCircle } from "@/components/pisga/SpeakerCircle";
import { PisgaForm } from "@/components/pisga/PisgaForm";
import { PisgaSticky } from "@/components/pisga/PisgaSticky";
import { Countdown } from "@/components/Countdown";
import { XOStrip } from "@/components/XOStrip";
import { Icon } from "@/components/Icons";
import {
  PISGA_EVENT as E,
  PISGA_SPEAKERS,
  PISGA_TAKEAWAYS,
  PISGA_AGENDA,
  PISGA_YOSSI_POINTS,
  PISGA_PANEL_TOPICS,
  PISGA_ITAMAR_OUTCOMES,
  PISGA_CONNECT,
  PISGA_OFFER,
  PISGA_MORE,
} from "@/lib/pisga";

export const metadata: Metadata = {
  title: "פסגת העסקים החרדית 2026 | 20.07 · בית שמש",
  description:
    "הכנס השנתי למנהיגות, חדשנות וצמיחה עסקית. השמות שמובילים את עולם העסקים החרדי, על במה אחת. מגיעים בגלל השמות, יוצאים עם כיוון ברור לעסק.",
};

/* עזרי layout */
function CTAButton({ children, className = "" }: { children: React.ReactNode; className?: string }) {
  return (
    <a href={E.ticketsUrl} target="_blank" rel="noopener" className={`btn-gold ${className}`}>
      <Icon name="arrow" width={20} height={20} style={{ transform: "scaleX(-1)" }} />
      {children}
    </a>
  );
}

function EventMeta() {
  const items = [E.date, E.time, E.location, "בהפרדה", "מספר המקומות מוגבל"];
  return (
    <div className="flex flex-wrap justify-center gap-2.5">
      {items.map((t) => (
        <span key={t} className="rounded-full border border-[var(--line)] bg-white/[0.02] px-3.5 py-2 text-sm text-[#cfcbc3]">
          {t}
        </span>
      ))}
    </div>
  );
}

function Punch({ children }: { children: React.ReactNode }) {
  return (
    <Reveal>
      <p className="mx-auto mt-8 max-w-2xl text-center text-xl sm:text-2xl font-extrabold leading-snug text-white">
        {children}
      </p>
    </Reveal>
  );
}

function Title({ children }: { children: React.ReactNode }) {
  return (
    <Reveal>
      <h2 className="text-center font-extrabold" style={{ fontSize: "clamp(1.7rem,4.5vw,2.7rem)" }}>
        {children}
      </h2>
    </Reveal>
  );
}

/* צללית הרים אטמוספרית בתחתית ההירו — ערפל וזוהר זהב על הפסגה */
function Mountains() {
  return (
    <div className="pointer-events-none absolute inset-x-0 bottom-0 z-[1]" aria-hidden>
      <svg viewBox="0 0 1440 320" preserveAspectRatio="none" className="h-40 w-full sm:h-56">
        <defs>
          <linearGradient id="haze" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0" stopColor="rgba(212,175,55,0)" />
            <stop offset="0.55" stopColor="rgba(139,101,20,0.10)" />
            <stop offset="1" stopColor="rgba(212,175,55,0.18)" />
          </linearGradient>
          <linearGradient id="ridgeFar" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0" stopColor="#2a1f0b" />
            <stop offset="1" stopColor="#0c0a06" />
          </linearGradient>
        </defs>
        <rect x="0" y="110" width="1440" height="210" fill="url(#haze)" />
        <path d="M0 320 L0 178 L220 96 L430 166 L640 80 L860 166 L1080 100 L1300 172 L1440 110 L1440 320 Z" fill="url(#ridgeFar)" />
        <path d="M0 178 L220 96 L430 166 L640 80 L860 166 L1080 100 L1300 172 L1440 110" fill="none" stroke="rgba(212,175,55,0.28)" strokeWidth="1.5" />
        <path d="M0 320 L0 212 L200 150 L400 206 L600 140 L820 210 L1040 156 L1260 216 L1440 160 L1440 320 Z" fill="#080706" />
        <path d="M0 320 L0 256 L260 206 L520 256 L760 200 L1000 256 L1240 210 L1440 250 L1440 320 Z" fill="#020202" />
      </svg>
    </div>
  );
}

/* תמונה עגולה על תווית זהב — כרטיס מרצה קומפקטי בהירו */
function SpeakerPill({ s }: { s: (typeof PISGA_SPEAKERS)[number] }) {
  return (
    <div className="flex w-[7.5rem] flex-col items-center sm:w-32">
      <SpeakerCircle img={s.img} name={s.name} className="w-[4.75rem] sm:w-[5.25rem]" />
      <div className="nameplate -mt-3 w-full px-2 pb-2 pt-4 text-center">
        <p className="text-[0.9rem] font-extrabold leading-tight">{s.name}</p>
        <p className="mt-0.5 text-[10px] font-semibold leading-tight opacity-70">{s.pill}</p>
      </div>
    </div>
  );
}

export default function Pisga() {
  return (
    <main>
      {/* ===== HERO ===== */}
      <header className="starfield relative overflow-hidden">
        <XOStrip />
        <div className="relative z-10 mx-auto max-w-6xl px-5 pt-9 pb-44 text-center sm:pb-52">
          <Image src="/logo-white.png" alt="הכפלה עסקית" width={140} height={60} priority className="mx-auto h-20 w-auto opacity-95" />
          <Reveal>
            <p className="mt-8 text-xs font-bold tracking-[0.4em] text-[var(--gold-2)]">פסגת העסקים החרדית 2026</p>
            <h1 className="mt-3 font-extrabold tracking-tight text-white" style={{ fontSize: "clamp(1.6rem,4.2vw,2.9rem)", lineHeight: 1.14 }}>
              השמות המובילים בעולם העסקים החרדי
            </h1>
            <p className="mt-1 font-extrabold text-gold" style={{ fontSize: "clamp(3.2rem,12vw,6.8rem)", lineHeight: 0.98, letterSpacing: "-0.02em" }}>
              על במה אחת
            </p>
            <p className="mx-auto mt-7 max-w-2xl text-base sm:text-lg text-[#d8d4cd]">
              ערב אחד שיחבר אתכם לאנשים, לרעיונות ולהחלטות שיכולים לקחת את העסק שלכם לרמה הבאה.
            </p>
          </Reveal>

          {/* גלריית המרצים — בסגנון הפלייר: תמונה עגולה על תווית זהב */}
          <Stagger className="mx-auto mt-14 flex max-w-6xl flex-wrap justify-center gap-x-3 gap-y-9 sm:gap-x-5">
            {PISGA_SPEAKERS.map((s) => (
              <Item key={s.slug}>
                <SpeakerPill s={s} />
              </Item>
            ))}
          </Stagger>

          <Reveal>
            <div className="mt-16 flex justify-center"><Countdown /></div>
            <div className="mt-8"><CTAButton>אני רוצה להיות בפסגה</CTAButton></div>
            <div className="mt-8"><EventMeta /></div>
          </Reveal>
        </div>
        <Mountains />
      </header>

      {/* ===== 1.5 שני סוגים של בעלי עסקים — הקופי הארוך ===== */}
      <section className="section" style={{ background: "#030303" }}>
        <div className="wrap-narrow">
          <Reveal>
            <h2 className="text-center font-extrabold" style={{ fontSize: "clamp(1.7rem,4.5vw,2.7rem)" }}>
              יש בעלי עסקים <span className="text-gold">שעובדים קשה.</span>
            </h2>
            <p className="mx-auto mt-6 max-w-xl text-center text-lg text-[var(--muted)]">
              רודפים אחרי לקוחות. מכבים שריפות. סוגרים חודש, ופותחים עוד חודש באותו לחץ.
            </p>
          </Reveal>
          <Reveal>
            <p className="mx-auto mt-9 max-w-2xl text-center text-xl sm:text-2xl font-extrabold leading-snug text-white">
              אבל יש בעלי עסקים שעוצרים רגע, מבינים מה תוקע אותם,
              <br />
              <span className="text-gold">ובונים מנגנון שמתחיל לקחת את העסק קדימה.</span>
            </p>
          </Reveal>
          <Reveal>
            <p className="mt-12 text-center text-[var(--muted)]">
              פסגת העסקים החרדית 2026 נבנתה בדיוק בשביל בעלי עסקים שרוצים יותר:
            </p>
          </Reveal>
          <Stagger className="mx-auto mt-5 flex max-w-2xl flex-wrap justify-center gap-2.5">
            {PISGA_MORE.map((m) => (
              <Item key={m}>
                <span className="rounded-full border border-[rgba(212,175,55,0.35)] bg-[#0c0c0c] px-4 py-2 text-sm font-bold text-[var(--gold-2)]">
                  {m}
                </span>
              </Item>
            ))}
          </Stagger>
          <Punch>
            זה לא עוד כנס. <span className="text-gold">זה ערב שיכול לעשות סדר לבעל עסק שרוצה לעלות שלב.</span>
          </Punch>
        </div>
      </section>

      {/* ===== 2. מה יוצא לכם מזה ===== */}
      <section className="section" style={{ background: "linear-gradient(180deg,#050505,#000)" }}>
        <div className="wrap-narrow">
          <Title>מה אתם לוקחים מהערב הזה?</Title>
          <Stagger className="mt-10 grid gap-4 sm:grid-cols-2">
            {PISGA_TAKEAWAYS.map((t, i) => (
              <Item key={t}>
                <div className="flex h-full items-start gap-4 rounded-2xl border border-[var(--line)] bg-[#0c0c0c] p-6">
                  <span className="text-gold text-3xl font-extrabold tabular-nums leading-none" dir="ltr">{i + 1}</span>
                  <span className="text-lg text-[#e6e2da]">{t}</span>
                </div>
              </Item>
            ))}
          </Stagger>
          <Reveal>
            <p className="mt-10 text-center text-lg text-[var(--muted)]">
              לא עוד ערב של השראה. <span className="text-white font-bold">ערב שמחזיר אתכם לעסק עם החלטה.</span>
            </p>
          </Reveal>
        </div>
      </section>

      {/* ===== 3. המשתתפים ===== */}
      <section className="section aura" style={{ background: "#020202" }}>
        <div className="wrap">
          <Title>האנשים שבגללם אתם רוצים להיות שם</Title>
          <Stagger className="mt-12 grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
            {PISGA_SPEAKERS.map((s, i) => {
              const isLastAlone = i === PISGA_SPEAKERS.length - 1;
              return (
                <Item key={s.slug} className={isLastAlone ? "sm:col-span-2 lg:col-span-1 lg:col-start-2" : undefined}>
                  <div className={isLastAlone ? "mx-auto h-full w-full sm:max-w-[calc(50%-0.75rem)] lg:max-w-none" : "h-full"}>
                    <SpeakerDetail s={s} />
                  </div>
                </Item>
              );
            })}
          </Stagger>

          <Reveal>
            <div className="mt-12 flex justify-center">
              <CTAButton>אני רוצה להיות בחדר עם האנשים האלו</CTAButton>
            </div>
          </Reveal>
        </div>
      </section>

      {/* ===== 4. לוח הערב ===== */}
      <section className="section" style={{ background: "#040404" }}>
        <div className="wrap-narrow">
          <Title>מה מחכה לכם בפסגה?</Title>
          <div className="relative mt-12 pr-6">
            <div className="absolute right-[9px] top-2 bottom-2 w-px bg-gradient-to-b from-[var(--gold-3)] via-[var(--line-strong)] to-transparent" />
            <Stagger className="space-y-4">
              {PISGA_AGENDA.map((a) => (
                <Item key={a.time}>
                  <div className="relative flex items-center gap-4">
                    <span className="absolute -right-[26px] h-4 w-4 rounded-full border-2 border-[var(--gold-3)] bg-black" />
                    <div className="flex-1 rounded-xl border border-[var(--line)] bg-[#0c0c0c] p-4 sm:flex sm:items-center sm:gap-5">
                      <span className="text-gold font-extrabold tabular-nums" style={{ fontSize: "1.25rem", minWidth: 72 }} dir="ltr">{a.time}</span>
                      <span className="font-bold text-white">{a.title}</span>
                    </div>
                  </div>
                </Item>
              ))}
            </Stagger>
          </div>
        </div>
      </section>

      {/* ===== 5. הרצאת יוסי לוי ===== */}
      <SpotlightSection
        eyebrow="הרצאת הפתיחה · יוסי לוי, מהמנטורים העסקיים המובילים בישראל"
        title="„אוטומרקי”: חשיפת מערכת השיווק האוטונומית הראשונה"
        img="/speakers/yossi-levi.jpeg"
        name="יוסי לוי"
        points={PISGA_YOSSI_POINTS}
        punch="המטרה: להבין לאן השוק הולך לפני שהוא משאיר אתכם מאחור."
      />

      {/* ===== 6. פאנל ===== */}
      <section className="section" style={{ background: "#020202" }}>
        <div className="wrap-narrow">
          <Reveal>
            <p className="text-center text-sm font-bold uppercase tracking-widest text-[var(--gold-2)]">פאנל הפסגה</p>
          </Reveal>
          <Title>השאלות שכל בעל עסק במגזר החרדי חייב לשאול</Title>
          <div className="mx-auto mt-9 flex max-w-2xl flex-wrap justify-center gap-2.5">
            {PISGA_PANEL_TOPICS.map((t) => (
              <span key={t} className="rounded-full border border-[var(--line)] bg-[#0c0c0c] px-4 py-2 text-sm text-[#d8d4cd]">{t}</span>
            ))}
          </div>
          <Punch>
            שאלות אמיתיות. <span className="text-gold">תשובות מאנשים שעשו את זה בפועל.</span>
          </Punch>
        </div>
      </section>

      {/* ===== 7. הרצאת איתמר ===== */}
      <SpotlightSection
        eyebrow="ההרצאה המרכזית · איתמר שולם"
        title="לא רק להבין. להחליט מה עושים עכשיו."
        img="/speakers/itamar-shulem.png"
        name="איתמר שולם"
        points={PISGA_ITAMAR_OUTCOMES}
        pointsIntro="בסיום ההרצאה תצאו עם:"
        punch="לא עוד מחברת מלאה. כיוון ברור לעסק."
        flip
      />

      {/* ===== 8. מתחם החיבורים ===== */}
      <section className="section" style={{ background: "#040404" }}>
        <div className="wrap-narrow">
          <Title>זה לא נטוורקינג רגיל</Title>
          <Reveal>
            <p className="mx-auto mt-4 max-w-xl text-center text-[var(--muted)]">צוות יועצי הכפלה עסקית יהיה במקום כדי:</p>
          </Reveal>
          <Stagger className="mt-8 grid gap-3 sm:grid-cols-2">
            {PISGA_CONNECT.map((c) => (
              <Item key={c}>
                <div className="flex items-center gap-3 rounded-xl border border-[var(--line)] bg-[#0c0c0c] p-4">
                  <span className="flex h-6 w-6 flex-shrink-0 items-center justify-center rounded-full gold-fill">
                    <Icon name="check" width={13} height={13} className="text-black" />
                  </span>
                  <span className="text-[#e6e2da]">{c}</span>
                </div>
              </Item>
            ))}
          </Stagger>
          <Punch>
            אתם לא מגיעים רק להכיר אנשים. <span className="text-gold">אתם מגיעים כדי ליצור חיבורים שיקדמו את העסק.</span>
          </Punch>
        </div>
      </section>

      {/* ===== 9. סיכום ההצעה ===== */}
      <section className="relative section overflow-hidden" style={{ background: "linear-gradient(180deg,#000,#0a0503)" }}>
        <div className="wrap-narrow">
          <Title>בערב אחד אתם מקבלים:</Title>
          <Stagger className="mx-auto mt-10 grid max-w-2xl gap-3 sm:grid-cols-2">
            {PISGA_OFFER.map((o) => (
              <Item key={o}>
                <div className="flex items-start gap-3 rounded-xl border border-[var(--line)] bg-[#0c0c0c] p-4">
                  <span className="mt-0.5 flex h-5 w-5 flex-shrink-0 items-center justify-center rounded-full gold-fill">
                    <Icon name="check" width={12} height={12} className="text-black" />
                  </span>
                  <span className="text-[#e6e2da]">{o}</span>
                </div>
              </Item>
            ))}
          </Stagger>
          <Reveal>
            <div className="mx-auto mt-12 max-w-2xl rounded-3xl border border-[rgba(212,175,55,0.3)] bg-gradient-to-b from-[#161206] to-[#0b0b0b] p-8 text-center glow-gold">
              <p className="text-2xl sm:text-3xl font-extrabold leading-tight text-white">
                מגיעים בגלל השמות.
                <br />
                <span className="text-gold">יוצאים עם כיוון ברור לעסק.</span>
              </p>
              <div className="mt-7">
                <EventMeta />
              </div>
              <div className="mt-8">
                <CTAButton>אני רוצה להיות בפסגה</CTAButton>
              </div>
            </div>
          </Reveal>
        </div>
      </section>

      {/* ===== 10. טופס ===== */}
      <PisgaForm />

      <footer className="border-t border-[var(--line)] py-8 text-center">
        <p className="text-sm text-[var(--muted-2)]">© {new Date().getFullYear()} הכפלה עסקית · איתמר שולם</p>
        <p className="mt-1.5 text-xs text-[var(--muted-2)]">מגיעים בגלל השמות. יוצאים עם כיוון ברור לעסק.</p>
      </footer>

      <PisgaSticky />
    </main>
  );
}

/* כרטיס מרצה מפורט — תמונה עגולה + טקסט */
function SpeakerDetail({ s }: { s: (typeof PISGA_SPEAKERS)[number] }) {
  return (
    <div className="card flex h-full flex-col items-center p-7 text-center">
      <SpeakerCircle img={s.img} name={s.name} className="w-28" />
      <h3 className="mt-5 text-xl font-extrabold text-white">{s.name}</h3>
      <p className="mt-1 text-sm text-[var(--gold-2)]">{s.title}</p>
      <hr className="hr-gold mt-4 w-12" />
      <p className="mt-4 text-sm text-[#cfcbc3]">{s.authority}</p>
      <p className="mt-2 text-sm text-[var(--muted)]">{s.brings}</p>
    </div>
  );
}

/* מקטע זרקור (יוסי / איתמר) — תמונה + נקודות + שורת מחץ */
function SpotlightSection({
  eyebrow, title, img, name, points, pointsIntro, punch, flip = false,
}: {
  eyebrow: string; title: string; img: string; name: string; points: string[]; pointsIntro?: string; punch: string; flip?: boolean;
}) {
  return (
    <section className="section aura" style={{ background: "#010101" }}>
      <div className="wrap">
        <div className={`grid items-center gap-10 md:grid-cols-2 ${flip ? "md:[direction:ltr]" : ""}`}>
          <Reveal className={flip ? "md:[direction:rtl]" : ""}>
            <SpeakerImage img={img} name={name} className="mx-auto aspect-[4/5] w-full max-w-sm" />
          </Reveal>
          <Reveal className={flip ? "md:[direction:rtl]" : ""}>
            <div>
              <p className="text-sm font-bold uppercase tracking-widest text-[var(--gold-2)]">{eyebrow}</p>
              <h2 className="mt-3 font-extrabold" style={{ fontSize: "clamp(1.7rem,4vw,2.6rem)", lineHeight: 1.06 }}>{title}</h2>
              {pointsIntro && <p className="mt-4 text-[var(--muted)]">{pointsIntro}</p>}
              <ul className="mt-5 space-y-3">
                {points.map((p) => (
                  <li key={p} className="flex items-start gap-3">
                    <span className="mt-0.5 flex h-5 w-5 flex-shrink-0 items-center justify-center rounded-full gold-fill">
                      <Icon name="check" width={12} height={12} className="text-black" />
                    </span>
                    <span className="text-[#e6e2da]">{p}</span>
                  </li>
                ))}
              </ul>
              <p className="mt-7 border-r-2 border-r-[var(--gold-4)] pr-4 text-lg font-bold text-white">{punch}</p>
            </div>
          </Reveal>
        </div>
      </div>
    </section>
  );
}
