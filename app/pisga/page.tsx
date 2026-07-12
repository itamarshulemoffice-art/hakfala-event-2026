import type { Metadata } from "next";
import Image from "next/image";
import { Reveal, Stagger, Item } from "@/components/Reveal";
import { SpeakerImage } from "@/components/pisga/SpeakerImage";
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
} from "@/lib/pisga";

export const metadata: Metadata = {
  title: "פסגת העסקים החרדית 2026 | 20.07 · בית שמש",
  description:
    "הכנס השנתי למנהיגות, חדשנות וצמיחה עסקית. השמות שמובילים את עולם העסקים החרדי — על במה אחת. מגיעים בגלל השמות, יוצאים עם כיוון ברור לעסק.",
};

const featured = PISGA_SPEAKERS.filter((s) => s.featured);
const rest = PISGA_SPEAKERS.filter((s) => !s.featured);

/* עזרי layout */
function CTAButton({ children, className = "" }: { children: React.ReactNode; className?: string }) {
  return (
    <a href="#register" className={`btn-gold ${className}`}>
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

function FaceCaption({ name, small = false }: { name: string; small?: boolean }) {
  return (
    <div className="cap">
      <p className={`font-extrabold text-white ${small ? "text-base" : "text-lg"}`}>{name}</p>
    </div>
  );
}

export default function Pisga() {
  return (
    <main>
      {/* ===== HERO ===== */}
      <header className="relative overflow-hidden" style={{ background: "radial-gradient(120% 90% at 50% -10%, #14110a 0%, #000 62%)" }}>
        <div className="absolute inset-0 grid-bg grid-bg-fade" aria-hidden />
        <XOStrip />
        <div className="relative z-10 mx-auto max-w-6xl px-5 pt-10 pb-16 text-center">
          <Image src="/logo-white.png" alt="הכפלה עסקית" width={140} height={60} priority className="mx-auto h-11 w-auto opacity-95" />
          <Reveal>
            <p className="mt-8 text-sm font-bold tracking-wide text-[var(--gold-2)]">{E.brandLine}</p>
            <h1 className="mt-3 font-extrabold tracking-tight" style={{ fontSize: "clamp(2.4rem,7vw,4.8rem)", lineHeight: 1.02 }}>
              פסגת העסקים <span className="text-gold">החרדית 2026</span>
            </h1>
            <p className="mx-auto mt-4 max-w-2xl text-lg sm:text-xl text-[#d8d4cd]">{E.subtitle}</p>
            <p className="mx-auto mt-5 max-w-2xl text-base sm:text-lg font-bold text-white">{E.punch}</p>
          </Reveal>

          {/* פנים המרצים — הלב של הדף */}
          <div className="mt-12">
            <Stagger className="mx-auto grid max-w-3xl grid-cols-2 gap-4">
              {featured.map((s) => (
                <Item key={s.slug}>
                  <SpeakerImage img={s.img} name={s.name} className="aspect-[4/5] w-full">
                    <FaceCaption name={s.name} />
                  </SpeakerImage>
                </Item>
              ))}
            </Stagger>
            <Stagger className="mx-auto mt-4 grid max-w-3xl grid-cols-2 gap-4 sm:grid-cols-4">
              {rest.map((s) => (
                <Item key={s.slug}>
                  <SpeakerImage img={s.img} name={s.name} className="aspect-[4/5] w-full" rounded="rounded-xl">
                    <FaceCaption name={s.name} small />
                  </SpeakerImage>
                </Item>
              ))}
            </Stagger>
          </div>

          <Reveal>
            <div className="mt-11 flex justify-center">
              <Countdown />
            </div>
            <div className="mt-8">
              <CTAButton>אני רוצה להיות בפסגה</CTAButton>
            </div>
            <div className="mt-8">
              <EventMeta />
            </div>
          </Reveal>
        </div>
      </header>

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
          <Title>האנשים שבגללם אתם רוצים להיות בחדר</Title>

          <Stagger className="mt-12 grid gap-6 md:grid-cols-2">
            {featured.map((s) => (
              <Item key={s.slug}>
                <SpeakerDetail s={s} big />
              </Item>
            ))}
          </Stagger>
          <Stagger className="mt-6 grid gap-6 sm:grid-cols-2">
            {rest.map((s) => (
              <Item key={s.slug}>
                <SpeakerDetail s={s} />
              </Item>
            ))}
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
        eyebrow="הרצאת הפתיחה · יוסי לוי · 90 דקות"
        title="איך משווקים בעולם שבו AI משנה הכול?"
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

/* כרטיס מרצה מפורט */
function SpeakerDetail({ s, big = false }: { s: (typeof PISGA_SPEAKERS)[number]; big?: boolean }) {
  return (
    <div className="card h-full overflow-hidden sm:flex">
      <SpeakerImage
        img={s.img}
        name={s.name}
        rounded="rounded-none"
        className={`w-full flex-shrink-0 ${big ? "aspect-[5/4] sm:aspect-auto sm:w-52" : "aspect-[5/4] sm:aspect-auto sm:w-40"}`}
      />
      <div className="p-6">
        <h3 className={`font-extrabold text-white ${big ? "text-2xl" : "text-xl"}`}>{s.name}</h3>
        <p className="mt-1 text-sm text-[var(--gold-2)]">{s.title}</p>
        <p className="mt-3 text-sm text-[#cfcbc3]">{s.authority}</p>
        <p className="mt-2 text-sm text-[var(--muted)]">{s.brings}</p>
      </div>
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
