"use client";

import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { CHECKOUT_URL, CTAS, EVENT } from "@/lib/site";
import { Icon } from "./Icons";
import { XOStrip } from "./XOStrip";

type Fields = {
  name: string;
  phone: string;
  email: string;
  business: string;
  field: string;
  employees: string;
  challenge: string;
  wantsCall: boolean;
  approve: boolean;
};

const EMPTY: Fields = {
  name: "", phone: "", email: "", business: "", field: "",
  employees: "", challenge: "", wantsCall: false, approve: false,
};

export function RegistrationForm() {
  const [f, setF] = useState<Fields>(EMPTY);
  const [errors, setErrors] = useState<Record<string, boolean>>({});
  const [sent, setSent] = useState(false);

  const set = (k: keyof Fields, v: string | boolean) => setF((p) => ({ ...p, [k]: v }));

  function validate() {
    const e: Record<string, boolean> = {};
    if (f.name.trim().length < 2) e.name = true;
    if (!/^0\d{8,9}$/.test(f.phone.replace(/[-\s]/g, ""))) e.phone = true;
    if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(f.email)) e.email = true;
    if (!f.approve) e.approve = true;
    setErrors(e);
    return Object.keys(e).length === 0;
  }

  function onSubmit(ev: React.FormEvent) {
    ev.preventDefault();
    if (!validate()) return;
    // TODO: כאן אפשר לשלוח את הפרטים ל-CRM / Google Sheets לפני המעבר לתשלום
    setSent(true);
  }

  const goCheckout = () => {
    if (CHECKOUT_URL && !CHECKOUT_URL.startsWith("#")) {
      window.open(CHECKOUT_URL, "_blank", "noopener");
    }
  };

  return (
    <section className="section" id="register" style={{ background: "linear-gradient(180deg,#0a0503,#000)" }}>
      <div className="wrap-narrow">
        <div className="overflow-hidden rounded-3xl border border-[rgba(212,175,55,0.3)] bg-[#0a0a0a] glow-gold">
          <XOStrip />
          <div className="p-6 sm:p-10">
            <AnimatePresence mode="wait">
              {!sent ? (
                <motion.div key="form" exit={{ opacity: 0, y: -10 }}>
                  <div className="text-center">
                    <h2 className="font-extrabold" style={{ fontSize: "clamp(1.7rem,4.5vw,2.6rem)" }}>
                      השאירו פרטים <span className="text-gold">ושמרו לעצמכם מקום</span>
                    </h2>
                    <p className="mt-3 text-[var(--muted)]">
                      {EVENT.dateLabel} · {EVENT.location} · מספר המקומות מוגבל
                    </p>
                  </div>

                  <form onSubmit={onSubmit} className="mt-8 grid gap-5 sm:grid-cols-2" noValidate>
                    <div>
                      <label className="label">שם מלא</label>
                      <input className="field" style={errors.name ? { borderColor: "#c0392b" } : undefined}
                        placeholder="השם שלך" value={f.name} onChange={(e) => set("name", e.target.value)} />
                    </div>
                    <div>
                      <label className="label">מספר טלפון</label>
                      <input type="tel" inputMode="tel" className="field" style={errors.phone ? { borderColor: "#c0392b" } : undefined}
                        placeholder="050-0000000" value={f.phone} onChange={(e) => set("phone", e.target.value)} />
                    </div>
                    <div>
                      <label className="label">כתובת דוא״ל</label>
                      <input type="email" inputMode="email" className="field" style={errors.email ? { borderColor: "#c0392b" } : undefined}
                        placeholder="you@example.com" value={f.email} onChange={(e) => set("email", e.target.value)} dir="ltr" />
                    </div>
                    <div>
                      <label className="label">שם העסק</label>
                      <input className="field" placeholder="שם העסק" value={f.business} onChange={(e) => set("business", e.target.value)} />
                    </div>
                    <div>
                      <label className="label">מה התחום שלכם?</label>
                      <input className="field" placeholder="תחום הפעילות" value={f.field} onChange={(e) => set("field", e.target.value)} />
                    </div>
                    <div>
                      <label className="label">כמה עובדים יש בעסק?</label>
                      <select className="field" value={f.employees} onChange={(e) => set("employees", e.target.value)}>
                        <option value="">בחר/י</option>
                        <option>רק אני</option>
                        <option>1–2</option>
                        <option>3–6</option>
                        <option>מעל 6</option>
                      </select>
                    </div>
                    <div className="sm:col-span-2">
                      <label className="label">מהו האתגר המרכזי שלכם כרגע?</label>
                      <select className="field" value={f.challenge} onChange={(e) => set("challenge", e.target.value)}>
                        <option value="">בחר/י</option>
                        <option>שיווק</option>
                        <option>מכירות</option>
                        <option>עובדים</option>
                        <option>ניהול</option>
                        <option>פיננסים</option>
                        <option>תמחור</option>
                        <option>אחר</option>
                      </select>
                    </div>

                    <div className="sm:col-span-2 space-y-3 pt-1">
                      <label className="chk">
                        <input type="checkbox" checked={f.wantsCall} onChange={(e) => set("wantsCall", e.target.checked)} />
                        <span>אני מעוניין בשיחת מיקוד ראשונית עם אחד מיועצי הכפלה עסקית במהלך האירוע.</span>
                      </label>
                      <label className="chk" style={errors.approve ? { color: "#e07a6f" } : undefined}>
                        <input type="checkbox" checked={f.approve} onChange={(e) => set("approve", e.target.checked)} />
                        <span>בהרשמתי אני מאשר לקבל מאיתמר שולם עדכונים ומסרים הקשורים לאירוע ולפעילות הכפלה עסקית, בהתאם למדיניות הפרטיות.</span>
                      </label>
                    </div>

                    <div className="sm:col-span-2">
                      <button type="submit" className="btn-gold w-full">
                        <Icon name="arrow" width={20} height={20} style={{ transform: "scaleX(-1)" }} />
                        {CTAS.form}
                      </button>
                      <p className="mt-3 text-center text-xs text-[var(--muted-2)]">
                        מילוי הטופס אינו מבטיח מקום עד לקבלת אישור הרשמה סופי או השלמת רכישת הכרטיס.
                      </p>
                    </div>
                  </form>
                </motion.div>
              ) : (
                <motion.div key="success" initial={{ opacity: 0, y: 12 }} animate={{ opacity: 1, y: 0 }} className="text-center py-6">
                  <div className="mx-auto flex h-16 w-16 items-center justify-center rounded-full gold-fill">
                    <Icon name="check" width={30} height={30} className="text-black" />
                  </div>
                  <h2 className="mt-6 font-extrabold" style={{ fontSize: "clamp(1.6rem,4vw,2.4rem)" }}>
                    נרשמתם בהצלחה <span className="text-gold">לאירוע הכפלה עסקית!</span>
                  </h2>
                  <p className="mx-auto mt-4 max-w-xl text-[var(--muted)]">
                    עשיתם את הצעד הראשון בדרך לערב שיכול לשנות את הדרך שבה אתם מנהלים ומגדילים
                    את העסק. כדי להשלים את שריון המקום — המשיכו לרכישת הכרטיס.
                  </p>

                  <div className="mx-auto mt-7 max-w-md rounded-2xl border border-[var(--line)] bg-[#0c0c0c] p-5 text-right">
                    <p className="text-sm font-bold text-[var(--gold-2)]">מומלץ להגיע עם:</p>
                    <ul className="mt-2 space-y-1.5 text-sm text-[#d8d4cd]">
                      <li>· מטרה עסקית אחת שחשוב לכם להשיג.</li>
                      <li>· אתגר מרכזי שאתם רוצים לפתור.</li>
                      <li>· כרטיסי ביקור או פרטי קשר לחיבורים העסקיים.</li>
                    </ul>
                  </div>

                  <div className="mt-8 flex justify-center">
                    <button className="btn-gold" onClick={goCheckout}>
                      <Icon name="arrow" width={20} height={20} style={{ transform: "scaleX(-1)" }} />
                      להשלמת רכישת הכרטיס
                    </button>
                  </div>
                  <p className="mt-5 text-sm text-[var(--muted-2)]">נתראה בבית שמש.</p>
                </motion.div>
              )}
            </AnimatePresence>
          </div>
        </div>
      </div>
    </section>
  );
}
