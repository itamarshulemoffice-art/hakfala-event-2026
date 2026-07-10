import { Hero } from "@/components/Hero";
import { Nav } from "@/components/Nav";
import {
  PainSection,
  ChangeSection,
  AgendaSection,
  ReceptionSection,
  YossiSection,
  PanelSection,
  ItamarSection,
  WhyDifferentSection,
  ForWhomSection,
  WhatIfNotSection,
  OfferSection,
} from "@/components/sections";
import { RegistrationForm } from "@/components/RegistrationForm";
import { FAQSection } from "@/components/FAQ";
import { ClosingSection } from "@/components/Closing";
import { StickyBar } from "@/components/StickyBar";
import { ExitPopup } from "@/components/ExitPopup";
import { Icon } from "@/components/Icons";
import { EVENT } from "@/lib/site";

/* שורת המחץ החוזרת של המותג */
function PunchBanner() {
  return (
    <section className="border-y border-[var(--line)] bg-[#050505] py-12 px-5 text-center">
      <p className="mx-auto max-w-3xl text-xl sm:text-2xl font-extrabold leading-snug text-white">
        באירוע רגיל אתם מגיעים <span className="text-[var(--muted)]">לשמוע.</span>
        <br className="hidden sm:block" /> באירוע הכפלה עסקית מחכה לכם{" "}
        <span className="text-gold">צוות שלם</span> כדי לקחת אתכם קדימה.
      </p>
    </section>
  );
}

/* רצועת ההטבה */
function BonusBand() {
  return (
    <section className="section" style={{ background: "linear-gradient(180deg,#000,#0a0503)" }}>
      <div className="wrap-narrow">
        <div className="flex flex-col items-center gap-5 rounded-3xl border border-[rgba(212,175,55,0.35)] bg-gradient-to-b from-[#161206] to-[#0a0a0a] p-8 text-center sm:flex-row sm:text-right glow-gold">
          <span className="flex h-20 w-20 flex-shrink-0 items-center justify-center rounded-2xl gold-fill">
            <Icon name="gift" width={38} height={38} className="text-black" />
          </span>
          <div>
            <p className="text-sm font-bold uppercase tracking-widest text-[var(--gold-2)]">ההטבה שלך</p>
            <h3 className="mt-1 text-2xl font-extrabold text-white">מתנה בשווי {EVENT.giftValue} לכל משתתף</h3>
            <p className="mt-2 text-[var(--muted)]">
              המתנה תיחשף באירוע ותאפשר לכם להמשיך את תהליך ההתקדמות גם אחרי שתצאו מהאולם.
              בנוסף — תוכלו לסמן בהרשמה שאתם מעוניינים בשיחת מיקוד ראשונית עם אחד מיועצי הכפלה עסקית.
            </p>
          </div>
        </div>
      </div>
    </section>
  );
}

export default function Home() {
  return (
    <main>
      <Nav />
      <Hero />
      <PainSection />
      <ChangeSection />
      <AgendaSection />
      <ReceptionSection />
      <YossiSection />
      <PanelSection />
      <PunchBanner />
      <ItamarSection />
      <WhyDifferentSection />
      <ForWhomSection />
      <WhatIfNotSection />
      <BonusBand />
      <OfferSection />
      <RegistrationForm />
      <FAQSection />
      <ClosingSection />
      <StickyBar />
      <ExitPopup />
    </main>
  );
}
