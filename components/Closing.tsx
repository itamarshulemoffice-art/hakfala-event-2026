import Image from "next/image";
import { Reveal } from "./Reveal";
import { CTA } from "./CTA";
import { Icon } from "./Icons";
import { XOStrip } from "./XOStrip";
import { EVENT, EVENT_META, CTAS } from "@/lib/site";

const CLOSING_STEPS = [
  "להסתכל על העסק מלמעלה.",
  "לשמוע לאן העולם הולך.",
  "לקבל תשובות מהאנשים שמובילים אותו.",
  "לפגוש צוות של יועצים.",
  "לבנות מטרות.",
  "לזהות את מנגנוני ההכפלה.",
];

export function ClosingSection() {
  return (
    <section className="relative overflow-hidden" id="closing" style={{ background: "radial-gradient(120% 90% at 50% 120%, #14110a 0%, #000 60%)" }}>
      <XOStrip flip />
      <div className="section aura">
        <div className="wrap-narrow text-center">
          <Reveal>
            <h2 className="font-extrabold" style={{ fontSize: "clamp(2rem,5.5vw,3.4rem)", lineHeight: 1.05 }}>
              אתה יכול להמשיך לרוץ אחרי מה שדחוף.
              <br />
              <span className="text-gold">או לעצור לערב אחד.</span>
            </h2>
          </Reveal>

          <Reveal>
            <div className="mx-auto mt-9 flex max-w-lg flex-wrap justify-center gap-2">
              {CLOSING_STEPS.map((s) => (
                <span key={s} className="rounded-full border border-[var(--line)] bg-[#0c0c0c] px-3.5 py-1.5 text-sm text-[#cfcbc3]">{s}</span>
              ))}
            </div>
          </Reveal>

          <Reveal>
            <p className="mt-10 text-2xl font-extrabold text-white">
              בערב הזה החלטנו לקחת אתכם <span className="text-gold">לרמה הבאה שלכם.</span>
            </p>
          </Reveal>

          {/* כרטיס פרטי האירוע */}
          <Reveal>
            <div className="mx-auto mt-10 max-w-lg rounded-3xl border border-[rgba(212,175,55,0.35)] bg-[#0a0a0a] p-8 glow-gold">
              <Image src="/logo-white.png" alt="הכפלה עסקית" width={140} height={60} className="mx-auto h-12 w-auto" />
              <p className="mt-5 text-xl font-extrabold text-white">אירוע הכפלה עסקית 2026</p>
              <div className="mt-5 flex flex-wrap justify-center gap-2.5">
                {EVENT_META.map((m) => (
                  <span key={m.text} className="inline-flex items-center gap-2 rounded-full border border-[var(--line)] bg-white/[0.02] px-3 py-1.5 text-xs text-[#cfcbc3]">
                    <Icon name={m.icon} width={14} height={14} className="text-[var(--gold-3)]" />
                    {m.text}
                  </span>
                ))}
                <span className="inline-flex items-center gap-2 rounded-full border border-[rgba(212,175,55,0.3)] bg-[rgba(212,175,55,0.06)] px-3 py-1.5 text-xs text-[var(--gold-2)]">
                  <Icon name="gift" width={14} height={14} className="text-[var(--gold-3)]" />
                  מתנה בשווי {EVENT.giftValue} לכל משתתף
                </span>
              </div>
              <div className="mt-7 flex justify-center">
                <CTA>{CTAS.final}</CTA>
              </div>
            </div>
          </Reveal>
        </div>
      </div>

      {/* פוטר */}
      <footer className="border-t border-[var(--line)] py-8 text-center">
        <p className="text-sm text-[var(--muted-2)]">
          © {new Date().getFullYear()} הכפלה עסקית · איתמר שולם ·{" "}
          <a href={`tel:${EVENT.phone}`} className="text-[var(--gold-2)]" dir="ltr">{EVENT.phone}</a>
        </p>
        <p className="mt-1.5 text-xs text-[var(--muted-2)]">תוצאה. או שלא עובדים.</p>
      </footer>
    </section>
  );
}
