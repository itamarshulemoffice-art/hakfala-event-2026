"use client";

import { useEffect, useState } from "react";
import { AnimatePresence, motion } from "framer-motion";
import { CHECKOUT_URL, CTAS, EVENT } from "@/lib/site";
import { Icon } from "./Icons";

export function StickyBar() {
  const [show, setShow] = useState(false);

  useEffect(() => {
    const onScroll = () => {
      const y = window.scrollY;
      const nearBottom = window.innerHeight + y > document.body.scrollHeight - 900;
      setShow(y > 700 && !nearBottom);
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  const href = CHECKOUT_URL.startsWith("#") ? CHECKOUT_URL : CHECKOUT_URL;

  return (
    <AnimatePresence>
      {show && (
        <motion.div
          initial={{ y: 90 }}
          animate={{ y: 0 }}
          exit={{ y: 90 }}
          transition={{ type: "spring", stiffness: 260, damping: 28 }}
          className="fixed inset-x-0 bottom-0 z-40"
        >
          <div className="mx-auto max-w-4xl px-3 pb-3">
            <div className="flex items-center justify-between gap-3 rounded-2xl border border-[rgba(212,175,55,0.35)] bg-black/85 px-4 py-3 backdrop-blur-md glow-gold">
              <div className="min-w-0">
                <p className="truncate text-sm font-extrabold text-white">אירוע הכפלה עסקית</p>
                <p className="truncate text-xs text-[var(--muted)]">
                  {EVENT.dateLabel.replace("יום שני | ", "")} · {EVENT.location} · מקומות מוגבלים
                </p>
              </div>
              <a href={href} target={href.startsWith("#") ? undefined : "_blank"} rel="noopener" className="btn-gold flex-shrink-0" style={{ padding: "0.7rem 1.3rem", fontSize: "0.95rem" }}>
                <Icon name="arrow" width={17} height={17} style={{ transform: "scaleX(-1)" }} />
                {CTAS.sticky}
              </a>
            </div>
          </div>
        </motion.div>
      )}
    </AnimatePresence>
  );
}
