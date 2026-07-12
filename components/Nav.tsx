"use client";

import { useEffect, useState } from "react";
import Image from "next/image";
import { motion, AnimatePresence } from "framer-motion";
import { CHECKOUT_URL, CTAS } from "@/lib/site";
import { Icon } from "./Icons";

export function Nav() {
  const [show, setShow] = useState(false);
  useEffect(() => {
    const onScroll = () => setShow(window.scrollY > 620);
    window.addEventListener("scroll", onScroll, { passive: true });
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  const href = CHECKOUT_URL;

  return (
    <AnimatePresence>
      {show && (
        <motion.nav
          initial={{ y: -70 }} animate={{ y: 0 }} exit={{ y: -70 }}
          transition={{ type: "spring", stiffness: 260, damping: 26 }}
          className="fixed inset-x-0 top-0 z-40 border-b border-[var(--line)] bg-black/85 backdrop-blur-md"
        >
          <div className="mx-auto flex max-w-6xl items-center justify-between gap-3 px-3 py-2.5 sm:px-4 sm:py-3">
            <Image src="/logo-white.png" alt="הכפלה עסקית" width={104} height={44} className="h-8 w-auto shrink-0 sm:h-9" />
            <a href={href} target={href.startsWith("#") ? undefined : "_blank"} rel="noopener" className="btn-gold shrink-0 whitespace-nowrap" style={{ padding: "0.55rem 1.05rem", fontSize: "0.85rem" }}>
              <Icon name="arrow" width={15} height={15} style={{ transform: "scaleX(-1)" }} />
              {CTAS.sticky}
            </a>
          </div>
        </motion.nav>
      )}
    </AnimatePresence>
  );
}
