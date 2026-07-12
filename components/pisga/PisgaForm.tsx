"use client";

import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Icon } from "../Icons";
import { XOStrip } from "../XOStrip";
import { PISGA_EVENT } from "@/lib/pisga";

type F = { name: string; phone: string; email: string; business: string; field: string };
const EMPTY: F = { name: "", phone: "", email: "", business: "", field: "" };

export function PisgaForm() {
  const [f, setF] = useState<F>(EMPTY);
  const [err, setErr] = useState<Record<string, boolean>>({});
  const [sent, setSent] = useState(false);
  const set = (k: keyof F, v: string) => setF((p) => ({ ...p, [k]: v }));

  function submit(e: React.FormEvent) {
    e.preventDefault();
    const x: Record<string, boolean> = {};
    if (f.name.trim().length < 2) x.name = true;
    if (!/^0\d{8,9}$/.test(f.phone.replace(/[-\s]/g, ""))) x.phone = true;
    if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(f.email)) x.email = true;
    setErr(x);
    if (Object.keys(x).length === 0) setSent(true);
  }

  return (
    <section className="section" id="register" style={{ background: "linear-gradient(180deg,#0a0503,#000)" }}>
      <div className="wrap-narrow">
        <div className="overflow-hidden rounded-3xl border border-[rgba(212,175,55,0.35)] bg-[#0a0a0a] glow-gold">
          <XOStrip />
          <div className="p-6 sm:p-10">
            <AnimatePresence mode="wait">
              {!sent ? (
                <motion.div key="f" exit={{ opacity: 0 }}>
                  <div className="text-center">
                    <h2 className="font-extrabold" style={{ fontSize: "clamp(1.7rem,4.5vw,2.5rem)" }}>
                      שמרו לעצמכם <span className="text-gold">מקום בפסגה</span>
                    </h2>
                    <p className="mt-3 text-[var(--muted)]">
                      {PISGA_EVENT.date} · {PISGA_EVENT.location} · מספר המקומות מוגבל
                    </p>
                  </div>
                  <form onSubmit={submit} noValidate className="mt-8 grid gap-5 sm:grid-cols-2">
                    <div>
                      <label className="label">שם מלא</label>
                      <input className="field" style={err.name ? { borderColor: "#c0392b" } : undefined} placeholder="השם שלך" value={f.name} onChange={(e) => set("name", e.target.value)} />
                    </div>
                    <div>
                      <label className="label">טלפון</label>
                      <input type="tel" inputMode="tel" className="field" style={err.phone ? { borderColor: "#c0392b" } : undefined} placeholder="050-0000000" value={f.phone} onChange={(e) => set("phone", e.target.value)} />
                    </div>
                    <div>
                      <label className="label">דוא״ל</label>
                      <input type="email" inputMode="email" dir="ltr" className="field" style={err.email ? { borderColor: "#c0392b" } : undefined} placeholder="you@example.com" value={f.email} onChange={(e) => set("email", e.target.value)} />
                    </div>
                    <div>
                      <label className="label">שם העסק</label>
                      <input className="field" placeholder="שם העסק" value={f.business} onChange={(e) => set("business", e.target.value)} />
                    </div>
                    <div className="sm:col-span-2">
                      <label className="label">תחום הפעילות</label>
                      <input className="field" placeholder="התחום שלך" value={f.field} onChange={(e) => set("field", e.target.value)} />
                    </div>
                    <div className="sm:col-span-2">
                      <button type="submit" className="btn-gold w-full">
                        <Icon name="arrow" width={20} height={20} style={{ transform: "scaleX(-1)" }} />
                        אני רוצה להיות בפסגת העסקים החרדית
                      </button>
                    </div>
                  </form>
                </motion.div>
              ) : (
                <motion.div key="s" initial={{ opacity: 0, y: 12 }} animate={{ opacity: 1, y: 0 }} className="py-6 text-center">
                  <div className="mx-auto flex h-16 w-16 items-center justify-center rounded-full gold-fill">
                    <Icon name="check" width={30} height={30} className="text-black" />
                  </div>
                  <h2 className="mt-6 font-extrabold" style={{ fontSize: "clamp(1.6rem,4vw,2.3rem)" }}>
                    המקום שלכם <span className="text-gold">נשמר</span>
                  </h2>
                  <p className="mx-auto mt-3 max-w-md text-[var(--muted)]">
                    ניצור אתכם קשר עם כל הפרטים לקראת הפסגה. נתראה בבית שמש.
                  </p>
                </motion.div>
              )}
            </AnimatePresence>
          </div>
        </div>
      </div>
    </section>
  );
}
