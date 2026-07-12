"use client";

import { useEffect, useState } from "react";
import { AnimatePresence, motion } from "framer-motion";
import { Icon } from "../Icons";
import { PISGA_EVENT } from "@/lib/pisga";

export function PisgaSticky() {
  const [show, setShow] = useState(false);
  useEffect(() => {
    const onScroll = () => {
      const y = window.scrollY;
      const nearBottom = window.innerHeight + y > document.body.scrollHeight - 820;
      setShow(y > 680 && !nearBottom);
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  return (
    <AnimatePresence>
      {show && (
        <motion.div
          initial={{ y: 90 }} animate={{ y: 0 }} exit={{ y: 90 }}
          transition={{ type: "spring", stiffness: 260, damping: 28 }}
          className="fixed inset-x-0 bottom-0 z-40"
        >
          <div className="mx-auto max-w-3xl px-3 pb-3">
            <div className="flex items-center justify-between gap-3 rounded-2xl border border-[rgba(212,175,55,0.35)] bg-black/85 px-4 py-3 backdrop-blur-md glow-gold">
              <div className="min-w-0">
                <p className="truncate text-sm font-extrabold text-white">פסגת העסקים החרדית 2026</p>
                <p className="truncate text-xs text-[var(--muted)]">{PISGA_EVENT.date} · {PISGA_EVENT.location} · מקומות מוגבלים</p>
              </div>
              <a href="#register" className="btn-gold shrink-0 whitespace-nowrap" style={{ padding: "0.6rem 1.2rem", fontSize: "0.9rem" }}>
                <Icon name="arrow" width={16} height={16} style={{ transform: "scaleX(-1)" }} />
                לשריון מקום
              </a>
            </div>
          </div>
        </motion.div>
      )}
    </AnimatePresence>
  );
}
