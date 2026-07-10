"use client";

import { useState } from "react";
import { AnimatePresence, motion } from "framer-motion";
import { FAQ as FAQ_DATA } from "@/lib/site";
import { Icon } from "./Icons";

export function FAQSection() {
  const [open, setOpen] = useState<number | null>(0);
  return (
    <section className="section" id="faq" style={{ background: "#020202" }}>
      <div className="wrap-narrow">
        <h2 className="text-center font-extrabold" style={{ fontSize: "clamp(1.8rem,4.5vw,2.8rem)" }}>
          שאלות <span className="text-gold">נפוצות</span>
        </h2>

        <div className="mt-10 space-y-3">
          {FAQ_DATA.map((item, i) => {
            const isOpen = open === i;
            return (
              <div key={i} className={`rounded-xl border bg-[#0b0b0b] transition-colors ${isOpen ? "border-[rgba(212,175,55,0.4)]" : "border-[var(--line)]"}`}>
                <button
                  onClick={() => setOpen(isOpen ? null : i)}
                  className="flex w-full items-center justify-between gap-4 p-5 text-right"
                  aria-expanded={isOpen}
                >
                  <span className="font-bold text-white">{item.q}</span>
                  <span className={`flex h-7 w-7 flex-shrink-0 items-center justify-center rounded-full border transition-transform ${isOpen ? "border-[var(--gold-3)] rotate-45" : "border-[var(--line-strong)]"}`}>
                    <Icon name="plus" width={16} height={16} className={isOpen ? "text-[var(--gold-3)]" : "text-[var(--muted)]"} />
                  </span>
                </button>
                <AnimatePresence initial={false}>
                  {isOpen && (
                    <motion.div
                      initial={{ height: 0, opacity: 0 }}
                      animate={{ height: "auto", opacity: 1 }}
                      exit={{ height: 0, opacity: 0 }}
                      transition={{ duration: 0.3, ease: "easeInOut" }}
                      className="overflow-hidden"
                    >
                      <p className="px-5 pb-5 text-[var(--muted)]">{item.a}</p>
                    </motion.div>
                  )}
                </AnimatePresence>
              </div>
            );
          })}
        </div>
      </div>
    </section>
  );
}
