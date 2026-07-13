"use client";

import Image from "next/image";
import { useState } from "react";

function initials(name: string) {
  return name.trim().split(" ").slice(0, 2).map((w) => w[0]).join("");
}

/**
 * תמונת מרצה בטיפול duotone זהב-שחור (מתאחד על רקעים שונים), צבע מלא ב-hover.
 * fallback ל-placeholder ממותג אם התמונה חסרה.
 */
export function SpeakerImage({
  img,
  name,
  className = "",
  rounded = "rounded-2xl",
  children,
}: {
  img: string;
  name: string;
  className?: string;
  rounded?: string;
  children?: React.ReactNode;
}) {
  const [failed, setFailed] = useState(false);

  if (failed) {
    return (
      <div className={`relative ${rounded} overflow-hidden border border-[rgba(212,175,55,0.4)] bg-gradient-to-b from-[#1a1710] to-[#070707] ${className}`}>
        <div className="flex h-full w-full flex-col items-center justify-center gap-1">
          <span className="text-gold text-3xl font-extrabold">{initials(name)}</span>
          <span className="text-[11px] tracking-wide text-[var(--muted-2)]">תמונת מרצה</span>
        </div>
        {children}
      </div>
    );
  }

  return (
    <div className={`duotone relative ${rounded} border border-[rgba(212,175,55,0.35)] ${className}`}>
      <Image
        src={img}
        alt={name}
        fill
        sizes="(max-width: 768px) 50vw, 400px"
        className="object-cover object-top"
        onError={() => setFailed(true)}
      />
      {children}
    </div>
  );
}
