import { Reveal, Stagger, Item } from "./Reveal";
import { CTA } from "./CTA";
import { Icon } from "./Icons";
import { XOStrip } from "./XOStrip";
import { SpeakerPhoto } from "./SpeakerPhoto";
import {
  PAIN_QUESTIONS,
  THREE_PILLARS,
  RECEPTION_BENEFITS,
  YOSSI_POINTS,
  PANELISTS,
  PANEL_QUESTIONS,
  MECHANISMS,
  WHY_DIFFERENT,
  FOR_WHOM,
  WHAT_IF_NOT,
  OFFER_SUMMARY,
  AGENDA,
  EVENT_META,
  CTAS,
} from "@/lib/site";

/* ---------- עזרי layout ---------- */
function Tag({ children }: { children: React.ReactNode }) {
  return <span className="pill">{children}</span>;
}

function Punch({ children }: { children: React.ReactNode }) {
  return (
    <Reveal>
      <div className="relative mx-auto mt-12 max-w-3xl overflow-hidden rounded-2xl border border-[rgba(212,175,55,0.3)] bg-gradient-to-b from-[#161206] to-[#0b0b0b] p-8 text-center glow-gold">
        <span className="text-gold text-5xl leading-none">”</span>
        <p className="mt-2 text-xl sm:text-2xl font-extrabold leading-snug text-white">{children}</p>
      </div>
    </Reveal>
  );
}

/* ============================================================
   מקטע שני — כאב בעל העסק
   ============================================================ */
const DAILY = ["לקוחות", "עובדים", "הצעות מחיר", "ספקים", "גבייה", "שיווק", "תזרים", "טלפונים", "הודעות", "בעיות שצריך לפתור עכשיו"];

export function PainSection() {
  return (
    <section className="section" id="pain">
      <div className="wrap-narrow">
        <Reveal>
          <h2 className="text-center font-extrabold" style={{ fontSize: "clamp(1.8rem,4.5vw,2.8rem)" }}>
            אתה לא צריך שמישהו יסביר לך <span className="text-gold">מה זו עבודה קשה.</span>
          </h2>
          <p className="mt-5 text-center text-lg text-[var(--muted)]">אתה קם בבוקר עם העסק בראש:</p>
        </Reveal>

        <div className="mt-7 flex flex-wrap justify-center gap-2.5">
          {DAILY.map((d, i) => (
            <Reveal key={d} i={i}>
              <span className="rounded-lg border border-[var(--line)] bg-[#0d0d0d] px-3.5 py-1.5 text-sm text-[#cfcbc3]">{d}</span>
            </Reveal>
          ))}
        </div>

        <Reveal>
          <p className="mx-auto mt-8 max-w-2xl text-center text-[var(--muted)]">
            ועוד רשימת משימות שלא נגמרת. יש לך עסק עם עובד אחד, שלושה או שישה עובדים.
            כבר בנית משהו: יש לקוחות, יש הכנסות, יש הצלחות. אבל עמוק בפנים אתה יודע
            שהעסק עדיין לא נמצא במקום שהוא יכול להיות בו. כי קשה לך לענות על כמה שאלות פשוטות:
          </p>
        </Reveal>

        <Stagger className="mt-9 grid gap-3 sm:grid-cols-2">
          {PAIN_QUESTIONS.map((q) => (
            <Item key={q}>
              <div className="flex h-full items-start gap-3 rounded-xl border border-[var(--line)] bg-[#0c0c0c] p-4">
                <Icon name="target" width={20} height={20} className="mt-0.5 flex-shrink-0 text-[var(--gold-3)]" />
                <span className="text-[#d8d4cd]">{q}</span>
              </div>
            </Item>
          ))}
        </Stagger>

        <Punch>
          אם העסק שלך תלוי בך בכל דבר, אין לך עדיין מנגנון צמיחה. יש לך עומס.
        </Punch>
      </div>
    </section>
  );
}

/* ============================================================
   מקטע שלישי — השינוי: ידע · תוכנית · אנשים
   ============================================================ */
export function ChangeSection() {
  return (
    <section className="section aura" id="change" style={{ background: "linear-gradient(180deg,#050505,#000)" }}>
      <div className="wrap">
        <Reveal>
          <div className="text-center">
            <Tag>הבחירה שלנו</Tag>
            <h2 className="mt-5 font-extrabold" style={{ fontSize: "clamp(1.8rem,4.5vw,2.8rem)" }}>
              בערב הזה החלטנו לקחת אתכם <span className="text-gold">לרמה הבאה שלכם.</span>
            </h2>
            <p className="mx-auto mt-5 max-w-2xl text-[var(--muted)]">
              לא עוד ערב נחמד. לא עוד הרצאות שמייצרות התלהבות ומתאדות למחרת בבוקר.
              לא עוד רשימת כלים שצריך „לבדוק מתישהו”. בנינו אירוע שמחבר בין שלושה
              דברים שבעל עסק חייב כדי להתקדם:
            </p>
          </div>
        </Reveal>

        <Stagger className="mt-12 grid gap-5 md:grid-cols-3">
          {THREE_PILLARS.map((p, i) => (
            <Item key={p.title}>
              <div className="card card-gold h-full p-7 text-center">
                <div className="mx-auto flex h-14 w-14 items-center justify-center rounded-2xl gold-fill text-2xl font-extrabold text-black">
                  {i + 1}
                </div>
                <h3 className="mt-5 text-2xl font-extrabold text-white">{p.title}</h3>
                <p className="mt-3 text-[var(--muted)]">{p.desc}</p>
              </div>
            </Item>
          ))}
        </Stagger>

        <Reveal>
          <p className="mx-auto mt-10 max-w-2xl text-center text-sm text-[var(--muted-2)]">
            האירוע נבנה מלכתחילה כחוויה עסקית רחבה: קבלת פנים, כיבוד, נטוורקינג,
            הרצאות ופאנל מומחים, ולא כאירוע סיום פנימי בלבד.
          </p>
        </Reveal>
      </div>
    </section>
  );
}

/* ============================================================
   לוח זמנים — סדר הערב
   ============================================================ */
export function AgendaSection() {
  return (
    <section className="section" id="agenda" style={{ background: "#040404" }}>
      <div className="wrap-narrow">
        <Reveal>
          <div className="text-center">
            <Tag>סדר הערב</Tag>
            <h2 className="mt-5 font-extrabold" style={{ fontSize: "clamp(1.7rem,4vw,2.5rem)" }}>
              איך <span className="text-gold">ייראה הערב</span>
            </h2>
          </div>
        </Reveal>

        <div className="relative mt-12 pr-6">
          <div className="absolute right-[9px] top-2 bottom-2 w-px bg-gradient-to-b from-[var(--gold-3)] via-[var(--line-strong)] to-transparent" />
          <Stagger className="space-y-5">
            {AGENDA.map((a) => (
              <Item key={a.time}>
                <div className="relative flex items-center gap-4">
                  <span className="absolute -right-[26px] h-4 w-4 rounded-full border-2 border-[var(--gold-3)] bg-black" />
                  <div className="flex-1 rounded-xl border border-[var(--line)] bg-[#0c0c0c] p-4 sm:flex sm:items-center sm:justify-between">
                    <div className="flex items-center gap-4">
                      <span className="text-gold font-extrabold tabular-nums" style={{ fontSize: "1.35rem" }} dir="ltr">{a.time}</span>
                      <span className="font-bold text-white">{a.title}</span>
                    </div>
                    <span className="mt-2 inline-block rounded-full border border-[var(--line-strong)] px-3 py-0.5 text-xs text-[var(--gold-2)] sm:mt-0">{a.tag}</span>
                  </div>
                </div>
              </Item>
            ))}
          </Stagger>
        </div>
      </div>
    </section>
  );
}

/* ============================================================
   מקטע רביעי — מתחם ההכפלה (לא נטוורקינג רגיל)
   ============================================================ */
export function ReceptionSection() {
  return (
    <section className="section" id="reception" style={{ background: "linear-gradient(180deg,#000,#070604)" }}>
      <div className="wrap">
        <Reveal>
          <div className="text-center">
            <Tag>16:00 · קבלת פנים ומתחם ההכפלה</Tag>
            <h2 className="mt-5 font-extrabold" style={{ fontSize: "clamp(1.8rem,4.5vw,2.8rem)" }}>
              זה לא <span className="text-gold">נטוורקינג רגיל.</span>
            </h2>
          </div>
        </Reveal>

        <Reveal>
          <div className="mx-auto mt-10 grid max-w-4xl gap-4 sm:grid-cols-2">
            <div className="rounded-2xl border border-[var(--line)] bg-[#0a0a0a] p-6">
              <p className="text-sm font-bold text-[var(--muted-2)]">באירוע רגיל</p>
              <p className="mt-2 text-lg text-[#cfcbc3]">אתה מגיע עם כוס קפה ומקווה לפגוש במקרה את האדם הנכון.</p>
            </div>
            <div className="rounded-2xl border border-[rgba(212,175,55,0.35)] bg-gradient-to-b from-[#161206] to-[#0b0b0b] p-6 glow-gold">
              <p className="text-sm font-bold text-[var(--gold-2)]">באירוע הכפלה עסקית</p>
              <p className="mt-2 text-lg font-bold text-white">מחכה לך צוות שלם שמגיע כדי להכיר את העסק שלך ולקחת אותך קדימה.</p>
            </div>
          </div>
        </Reveal>

        <Reveal>
          <p className="mx-auto mt-10 max-w-2xl text-center text-[var(--muted)]">
            יועצי הכפלה עסקית, בוגרי מסלול הכשרת היועצים, לא יגיעו רק כדי לעלות לבמה
            ולקבל תעודה. הם יגיעו כדי להיכנס לפעולה: להכיר בעלי עסקים, לשמוע אתגרים,
            לזהות נקודות תקיעות, לתת כיוון ראשוני ולחבר בין האנשים הנכונים.
          </p>
        </Reveal>

        <Stagger className="mt-12 grid gap-5 md:grid-cols-2 lg:grid-cols-3">
          {RECEPTION_BENEFITS.map((b, i) => (
            <Item key={b.title}>
              <div className="card h-full p-6">
                <div className="flex h-11 w-11 items-center justify-center rounded-xl border border-[rgba(212,175,55,0.3)] bg-[rgba(212,175,55,0.07)]">
                  <Icon name={["chat", "target", "spark", "arrow", "handshake"][i % 5]} className="text-[var(--gold-3)]" />
                </div>
                <h3 className="mt-4 text-lg font-extrabold text-white">{b.title}</h3>
                <p className="mt-2 text-sm text-[var(--muted)]">{b.desc}</p>
              </div>
            </Item>
          ))}
        </Stagger>

        <Reveal>
          <div className="mt-12 text-center">
            <p className="mx-auto max-w-2xl text-lg font-bold text-white">
              לא עוד לעמוד לבד ליד הקפה. הפעם יש צוות שלם שנמצא שם בשביל החיבורים ובשביל לקחת אתכם קדימה.
            </p>
            <div className="mt-7 flex justify-center">
              <CTA>{CTAS.reception}</CTA>
            </div>
          </div>
        </Reveal>
      </div>
    </section>
  );
}

/* ============================================================
   מקטע חמישי — יוסי לוי
   ============================================================ */
export function YossiSection() {
  return (
    <section className="section aura" id="yossi" style={{ background: "#020202" }}>
      <div className="wrap">
        <Reveal>
          <div className="text-center">
            <Tag>17:00 · הרצאה מרכזית · 60 דקות</Tag>
            <h2 className="mt-5 font-extrabold" style={{ fontSize: "clamp(2rem,5vw,3.2rem)" }}>
              <span className="text-gold">יוסי לוי</span>
            </h2>
            <p className="mx-auto mt-3 text-sm font-bold tracking-widest text-[var(--gold-2)]">
              מהמנטורים העסקיים המובילים בישראל
            </p>
            <p className="mx-auto mt-4 max-w-2xl text-lg text-[#d8d4cd]">
              „אוטומרקי”: חשיפת מערכת השיווק האוטונומית הראשונה
            </p>
          </div>
        </Reveal>

        <Reveal>
          <p className="mx-auto mt-8 max-w-2xl text-center text-[var(--muted)]">
            השאלה אינה האם AI ישפיע על העסק שלכם. השאלה היא אם תשתמשו בו כדי להוביל,
            או שתגלו מאוחר מדי שהשוק התקדם בלעדיכם. בהרצאה סוחפת בת שעה יוסי לוי יחשוף:
          </p>
        </Reveal>

        <Stagger className="mt-12 grid gap-4 md:grid-cols-2">
          {YOSSI_POINTS.map((p, i) => (
            <Item key={p.t}>
              <div className="flex h-full gap-4 rounded-xl border border-[var(--line)] bg-[#0b0b0b] p-5">
                <span className="text-gold text-2xl font-extrabold tabular-nums" dir="ltr">{String(i + 1).padStart(2, "0")}</span>
                <div>
                  <h3 className="font-extrabold text-white">{p.t}</h3>
                  <p className="mt-1 text-sm text-[var(--muted)]">{p.d}</p>
                </div>
              </div>
            </Item>
          ))}
        </Stagger>

        <Reveal>
          <div className="mx-auto mt-12 max-w-3xl rounded-2xl border border-[var(--line)] bg-[#0a0a0a] p-6 sm:p-7">
            <div className="flex flex-col gap-5 sm:flex-row sm:items-start">
              <SpeakerPhoto slug="yossi-levi" name="יוסי לוי" className="h-40 w-full flex-shrink-0 sm:h-32 sm:w-28" />
              <div>
                <p className="text-xl font-extrabold text-white">מי זה יוסי לוי?</p>
                <p className="text-sm text-[var(--gold-2)]">מנטור ומרצה מוביל בעולמות העסקים, השיווק והחדשנות</p>
                <p className="mt-3 text-[var(--muted)]">
                  במהלך שנות פעילותו הכשיר, הדריך וליווה אלפי בעלי עסקים, מנהלים ואנשי מקצוע.
                  מביא לבמה שילוב נדיר בין ראייה עסקית רחבה, הבנה עמוקה של שיווק והיכרות עם
                  השינויים שמשפיעים עכשיו על כל בעל עסק.
                </p>
              </div>
            </div>
          </div>
        </Reveal>

        <Reveal>
          <div className="mt-9 flex justify-center">
            <CTA>{CTAS.yossi}</CTA>
          </div>
        </Reveal>
      </div>
    </section>
  );
}

/* ============================================================
   מקטע שישי — פאנל המומחים
   ============================================================ */
export function PanelSection() {
  return (
    <section className="section" id="panel" style={{ background: "linear-gradient(180deg,#020202,#070604)" }}>
      <div className="wrap">
        <Reveal>
          <div className="text-center">
            <Tag>לאחר הרצאת יוסי לוי</Tag>
            <h2 className="mt-5 font-extrabold" style={{ fontSize: "clamp(1.9rem,4.8vw,3rem)" }}>
              פאנל <span className="text-gold">העסקים הגדול</span>
            </h2>
            <p className="mx-auto mt-4 max-w-2xl text-[var(--muted)]">
              השאלות הבוערות ביותר על סדר היום והעתיד המזהיר של עולם העסקים החרדי.
              לא נאומים מוכנים. לא תשובות דיפלומטיות. שאלות אמיתיות מהשטח, ותשובות ממי שבנו, הובילו וליוו עסקים בעצמם.
            </p>
          </div>
        </Reveal>

        <div className="mx-auto mt-9 flex max-w-3xl flex-wrap justify-center gap-2">
          {PANEL_QUESTIONS.map((q) => (
            <span key={q} className="rounded-full border border-[var(--line)] bg-[#0c0c0c] px-3 py-1.5 text-xs text-[#cfcbc3]">{q}</span>
          ))}
        </div>

        <Stagger className="mt-12 grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
          {PANELISTS.map((p) => (
            <Item key={p.name}>
              <div className="card h-full overflow-hidden">
                <SpeakerPhoto slug={p.slug} name={p.name} rounded="rounded-none" className="aspect-[4/5] w-full" />
                <div className="p-6">
                  <h3 className="font-extrabold text-white leading-tight">{p.name}</h3>
                  <p className="mt-1 text-xs text-[var(--gold-2)] leading-tight">{p.role}</p>
                  <p className="mt-3 text-sm text-[var(--muted)]">{p.bio}</p>
                </div>
              </div>
            </Item>
          ))}
        </Stagger>

        <Reveal>
          <div className="mt-10 text-center">
            <p className="mx-auto max-w-xl text-[var(--muted-2)]">
              ועוד לא חשפנו הכול. באירוע צפויים להשתתף אישי ציבור, אנשי עסקים ודמויות
              מפתח בעולם העסקים החרדי. חלק מהשמות ייחשפו לקראת האירוע.
            </p>
            <div className="mt-7 flex justify-center">
              <CTA>{CTAS.panel}</CTA>
            </div>
          </div>
        </Reveal>
      </div>
    </section>
  );
}

/* ============================================================
   מקטע שביעי — איתמר שולם
   ============================================================ */
export function ItamarSection() {
  return (
    <section className="section aura" id="itamar" style={{ background: "#010101" }}>
      <div className="wrap">
        <Reveal>
          <div className="text-center">
            <Tag>לאחר הפאנל · ההרצאה המרכזית</Tag>
            <h2 className="mt-5 font-extrabold" style={{ fontSize: "clamp(2rem,5vw,3.2rem)" }}>
              <span className="text-gold">איתמר שולם</span>
            </h2>
            <p className="mx-auto mt-4 max-w-2xl text-lg text-[#d8d4cd]">
              איך לוקחים שליטה על העסק ובונים תוכנית להכפלה עסקית?
            </p>
            <p className="mx-auto mt-4 max-w-2xl text-[var(--muted)]">
              רוב בעלי העסקים מגיעים לאירועים, ממלאים מחברת וחוזרים לעסק בלי לדעת מה
              לעשות קודם. בערב הזה זה לא יקרה. אתם לא אמורים לצאת רק עם השראה, אתם
              אמורים לצאת עם <span className="text-white font-bold">תוכנית מטרות.</span>
            </p>
          </div>
        </Reveal>

        <Reveal>
          <p className="mt-14 text-center text-sm font-bold uppercase tracking-widest text-[var(--gold-2)]">
            מנגנוני ההכפלה המרכזיים
          </p>
        </Reveal>
        <Stagger className="mt-6 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
          {MECHANISMS.map((m) => (
            <Item key={m.t}>
              <div className="card h-full p-6">
                <h3 className="text-lg font-extrabold text-gold">{m.t}</h3>
                <p className="mt-2 text-sm text-[var(--muted)]">{m.d}</p>
              </div>
            </Item>
          ))}
        </Stagger>

        <Punch>אני לא מדבר לאנשים. אני מפעיל אנשים.</Punch>

        <Reveal>
          <div className="mx-auto mt-12 max-w-3xl rounded-2xl border border-[var(--line)] bg-[#0a0a0a] p-6 sm:p-7">
            <div className="flex flex-col gap-5 sm:flex-row sm:items-start">
              <SpeakerPhoto slug="itamar-shulem" name="איתמר שולם" className="h-40 w-full flex-shrink-0 sm:h-32 sm:w-28" />
              <div>
                <p className="text-xl font-extrabold text-white">מי זה איתמר שולם?</p>
                <p className="text-sm text-[var(--gold-2)]">מייסד משרד הייעוץ האסטרטגי „הכפלה עסקית”</p>
                <p className="mt-3 text-[var(--muted)]">
                  אני והצוות שלי מלווים בעלי עסקים בתהליכים שנוגעים בכל מנגנוני העסק:
                  אסטרטגיה, מכירות, שיווק, כוח אדם, פיננסים, מערכות, AI והטמעת תוכניות עבודה.
                  אנחנו לא מאמינים בעוד ידע שנשאר בראש, אלא ביעדים מדידים, בכלים מוכחים,
                  ובליווי שלא נותן לברוח. לא דיבורים. לא תיאוריות. עסק שנמצא בשליטה ויודע לאן הוא מתקדם.
                </p>
              </div>
            </div>
          </div>
        </Reveal>

        <Reveal>
          <div className="mt-9 flex justify-center">
            <CTA>{CTAS.itamar}</CTA>
          </div>
        </Reveal>
      </div>
    </section>
  );
}

/* ============================================================
   מקטע שמיני — למה האירוע שונה
   ============================================================ */
export function WhyDifferentSection() {
  return (
    <section className="section" id="why" style={{ background: "linear-gradient(180deg,#070604,#000)" }}>
      <div className="wrap">
        <Reveal>
          <div className="text-center">
            <h2 className="font-extrabold" style={{ fontSize: "clamp(1.8rem,4.5vw,2.8rem)" }}>
              למה האירוע הזה <span className="text-gold">שונה?</span>
            </h2>
            <p className="mx-auto mt-4 max-w-xl text-[var(--muted)]">
              כי הפעם אתם לא מקבלים רק במה. אתם מקבלים מעטפת שלמה סביב העסק שלכם.
            </p>
          </div>
        </Reveal>

        <Stagger className="mt-12 grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
          {WHY_DIFFERENT.map((w, i) => (
            <Item key={w.t}>
              <div className="card h-full p-5">
                <Icon name={["mic", "chat", "target", "users", "handshake", "spark", "gift", "spark"][i]} className="text-[var(--gold-3)]" width={24} height={24} />
                <h3 className="mt-3 font-extrabold text-white">{w.t}</h3>
                <p className="mt-1.5 text-sm text-[var(--muted)]">{w.d}</p>
              </div>
            </Item>
          ))}
        </Stagger>
      </div>
    </section>
  );
}

/* ============================================================
   מקטע תשיעי — למי מיועד
   ============================================================ */
export function ForWhomSection() {
  return (
    <section className="section" id="forwhom" style={{ background: "#020202" }}>
      <div className="wrap-narrow">
        <Reveal>
          <div className="text-center">
            <Tag>בדיקת התאמה</Tag>
            <h2 className="mt-5 font-extrabold" style={{ fontSize: "clamp(1.8rem,4.5vw,2.8rem)" }}>
              למי האירוע <span className="text-gold">מיועד?</span>
            </h2>
            <p className="mt-4 text-[var(--muted)]">האירוע הזה נבנה בשבילך אם:</p>
          </div>
        </Reveal>

        <Stagger className="mt-9 grid gap-3 sm:grid-cols-2">
          {FOR_WHOM.map((f) => (
            <Item key={f}>
              <div className="flex items-start gap-3 rounded-xl border border-[var(--line)] bg-[#0c0c0c] p-4">
                <span className="mt-0.5 flex h-5 w-5 flex-shrink-0 items-center justify-center rounded-full gold-fill">
                  <Icon name="check" width={12} height={12} className="text-black" />
                </span>
                <span className="text-sm text-[#d8d4cd]">{f}</span>
              </div>
            </Item>
          ))}
        </Stagger>

        <Reveal>
          <p className="mt-9 text-center font-bold text-white">
            האירוע פונה לגברים ולנשים ומתקיים בהפרדה מלאה.
          </p>
        </Reveal>
      </div>
    </section>
  );
}

/* ============================================================
   מקטע עשירי — מה יקרה אם לא תגיעו
   ============================================================ */
export function WhatIfNotSection() {
  return (
    <section className="section" id="whatif" style={{ background: "linear-gradient(180deg,#000,#0a0503)" }}>
      <div className="wrap-narrow">
        <Reveal>
          <h2 className="text-center font-extrabold" style={{ fontSize: "clamp(1.8rem,4.5vw,2.8rem)" }}>
            מה יקרה <span className="text-gold">אם לא תגיעו?</span>
          </h2>
          <p className="mx-auto mt-5 max-w-xl text-center text-[var(--muted)]">
            לא נכתוב לכם שהעסק יקרוס מחר. אבל דבר אחד כן יקרה:
          </p>
        </Reveal>

        <Stagger className="mx-auto mt-9 max-w-xl space-y-2.5">
          {WHAT_IF_NOT.map((w) => (
            <Item key={w}>
              <div className="flex items-center gap-3 rounded-lg border-r-2 border-r-[var(--gold-4)] bg-[#0c0c0c] px-4 py-3 text-[#d8d4cd]">
                <Icon name="arrow" width={16} height={16} className="flex-shrink-0 text-[var(--gold-3)]" style={{ transform: "scaleX(-1)" }} />
                {w}
              </div>
            </Item>
          ))}
        </Stagger>

        <Punch>
          ההחלטה אינה אם העסק שלכם ישתנה. ההחלטה היא מי ינהל את השינוי: אתם או המציאות.
        </Punch>
      </div>
    </section>
  );
}

/* ============================================================
   מקטע שנים עשר — סיכום ההצעה
   ============================================================ */
export function OfferSection() {
  return (
    <section className="section" id="offer" style={{ background: "#010101" }}>
      <XOStrip className="mb-14" />
      <div className="wrap-narrow">
        <Reveal>
          <div className="text-center">
            <Tag>סיכום ההצעה</Tag>
            <h2 className="mt-5 font-extrabold" style={{ fontSize: "clamp(1.8rem,4.5vw,2.8rem)" }}>
              תחשבו מה מחכה לכם <span className="text-gold">בערב אחד:</span>
            </h2>
          </div>
        </Reveal>

        <Stagger className="mt-10 grid gap-3 sm:grid-cols-2">
          {OFFER_SUMMARY.map((o) => (
            <Item key={o}>
              <div className="flex items-start gap-3 rounded-xl border border-[var(--line)] bg-[#0c0c0c] p-4">
                <span className="mt-0.5 flex h-5 w-5 flex-shrink-0 items-center justify-center rounded-full gold-fill">
                  <Icon name="check" width={12} height={12} className="text-black" />
                </span>
                <span className="text-sm text-[#d8d4cd]">{o}</span>
              </div>
            </Item>
          ))}
        </Stagger>

        <Reveal>
          <p className="mt-10 text-center text-xl font-extrabold text-white">
            וכל זה נבנה סביב מטרה אחת: <span className="text-gold">לקחת אתכם לרמה הבאה שלכם.</span>
          </p>
          <div className="mt-8 flex flex-wrap justify-center gap-2.5">
            {EVENT_META.map((m) => (
              <span key={m.text} className="inline-flex items-center gap-2 rounded-full border border-[var(--line)] bg-white/[0.02] px-3.5 py-2 text-sm text-[#cfcbc3]">
                <Icon name={m.icon === "split" ? "split" : m.icon} width={15} height={15} className="text-[var(--gold-3)]" />
                {m.text}
              </span>
            ))}
          </div>
          <div className="mt-8 flex justify-center">
            <CTA>{CTAS.final}</CTA>
          </div>
        </Reveal>
      </div>
    </section>
  );
}
