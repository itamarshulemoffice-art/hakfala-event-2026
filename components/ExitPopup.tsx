"use client";

import { useEffect, useState } from "react";
import { AnimatePresence, motion } from "framer-motion";
import { CHECKOUT_URL, CTAS } from "@/lib/site";
import { Icon } from "./Icons";
import { XOStrip } from "./XOStrip";

const BENEFITS = ["הרצאות דגל", "פאנל מומחים", "שיחת מיקוד ראשונית", "מתנה בשווי 300 ₪", "חיבורים עסקיים"];

export function ExitPopup() {
  const [open, setOpen] = useState(false);

  useEffect(() => {
    if (typeof window === "undefined") return;
    if (sessionStorage.getItem("hakfala_popup")) return;

    let fired = false;
    const trigger = () => {
      if (fired) return;
      fired = true;
      setOpen(true);
      sessionStorage.setItem("hakfala_popup", "1");
    };

    // אחרי 40 שניות
    const timer = setTimeout(trigger, 40000);
    // או ביציאה מהעמוד (exit intent) בדסקטופ
    const onLeave = (e: MouseEvent) => { if (e.clientY <= 0) trigger(); };
    document.addEventListener("mouseleave", onLeave);

    return () => { clearTimeout(timer); document.removeEventListener("mouseleave", onLeave); };
  }, []);

  const close = () => setOpen(false);
  const href = CHECKOUT_URL;

  return (
    <AnimatePresence>
      {open && (
        <motion.div
          className="fixed inset-0 z-50 flex items-center justify-center p-4"
          initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}
        >
          <div className="absolute inset-0 bg-black/80 backdrop-blur-sm" onClick={close} />
          <motion.div
            initial={{ scale: 0.92, y: 20, opacity: 0 }}
            animate={{ scale: 1, y: 0, opacity: 1 }}
            exit={{ scale: 0.95, opacity: 0 }}
            transition={{ type: "spring", stiffness: 280, damping: 26 }}
            className="relative w-full max-w-md overflow-hidden rounded-3xl border border-[rgba(212,175,55,0.4)] bg-[#0a0a0a] glow-gold"
          >
            <XOStrip />
            <button onClick={close} aria-label="סגור" className="absolute left-4 top-14 flex h-8 w-8 items-center justify-center rounded-full border border-[var(--line-strong)] text-[var(--muted)] hover:text-white">
              ✕
            </button>
            <div className="p-7 text-center">
              <p className="text-sm font-bold uppercase tracking-widest text-[var(--gold-2)]">רגע לפני שאתם יוצאים</p>
              <h3 className="mt-3 text-2xl font-extrabold text-white">
                האם גם העסק שלכם עובד קשה מדי <span className="text-gold">בלי תוכנית צמיחה ברורה?</span>
              </h3>
              <p className="mt-3 text-sm text-[var(--muted)]">הירשמו עכשיו לאירוע הכפלה עסקית וקבלו:</p>

              <ul className="mt-4 space-y-2 text-right">
                {BENEFITS.map((b) => (
                  <li key={b} className="flex items-center gap-2.5 text-sm text-[#d8d4cd]">
                    <span className="flex h-5 w-5 items-center justify-center rounded-full gold-fill">
                      <Icon name="check" width={12} height={12} className="text-black" />
                    </span>
                    {b}
                  </li>
                ))}
              </ul>

              <a href={href} onClick={close} target={href.startsWith("#") ? undefined : "_blank"} rel="noopener" className="btn-gold mt-6 w-full">
                <Icon name="arrow" width={20} height={20} style={{ transform: "scaleX(-1)" }} />
                {CTAS.popup}
              </a>
            </div>
          </motion.div>
        </motion.div>
      )}
    </AnimatePresence>
  );
}
