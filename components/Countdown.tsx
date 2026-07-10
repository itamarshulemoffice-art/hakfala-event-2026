"use client";

import { useEffect, useState } from "react";
import { EVENT } from "@/lib/site";

function diff() {
  const target = new Date(EVENT.dateISO).getTime();
  const now = Date.now();
  const d = Math.max(0, target - now);
  return {
    days: Math.floor(d / 86400000),
    hours: Math.floor((d / 3600000) % 24),
    mins: Math.floor((d / 60000) % 60),
    secs: Math.floor((d / 1000) % 60),
  };
}

export function Countdown({ compact = false }: { compact?: boolean }) {
  const [t, setT] = useState<ReturnType<typeof diff> | null>(null);

  useEffect(() => {
    setT(diff());
    const id = setInterval(() => setT(diff()), 1000);
    return () => clearInterval(id);
  }, []);

  const units = [
    { v: t?.days ?? 0, l: "ימים" },
    { v: t?.hours ?? 0, l: "שעות" },
    { v: t?.mins ?? 0, l: "דקות" },
    { v: t?.secs ?? 0, l: "שניות" },
  ];

  return (
    <div className={`flex ${compact ? "gap-2" : "gap-2.5 sm:gap-3"}`} dir="ltr">
      {units.map((u) => (
        <div
          key={u.l}
          className="flex flex-col items-center rounded-xl border border-[var(--line)] bg-[#0c0c0c]"
          style={{ minWidth: compact ? 46 : 62, padding: compact ? "6px 8px" : "10px 12px" }}
        >
          <span
            className="text-gold font-extrabold tabular-nums"
            style={{ fontSize: compact ? "1.2rem" : "1.9rem", lineHeight: 1 }}
          >
            {String(u.v).padStart(2, "0")}
          </span>
          <span className="text-[var(--muted-2)]" style={{ fontSize: compact ? ".6rem" : ".72rem", marginTop: 3 }}>
            {u.l}
          </span>
        </div>
      ))}
    </div>
  );
}
