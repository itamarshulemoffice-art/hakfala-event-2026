"use client";

import Image from "next/image";
import { useState } from "react";
import { Icon } from "./Icons";

function initials(name: string) {
  return name.trim().split(" ").slice(0, 2).map((w) => w[0]).join("");
}

/**
 * מציג תמונת מרצה מ-`public/speakers/<slug>.jpg`.
 * אם אין תמונה — מוצג עיגול/מסגרת זהב עם ראשי התיבות (placeholder ממותג).
 * להוספת תמונה: פשוט שים קובץ בשם ה-slug בתיקייה public/speakers/ — אין צורך לגעת בקוד.
 */
export function SpeakerPhoto({
  slug,
  name,
  className = "",
  rounded = "rounded-2xl",
  ext = "jpg",
}: {
  slug: string;
  name: string;
  className?: string;
  rounded?: string;
  ext?: string;
}) {
  const [failed, setFailed] = useState(false);

  return (
    <div
      className={`relative overflow-hidden ${rounded} border border-[rgba(212,175,55,0.4)] bg-gradient-to-b from-[#1a1710] to-[#0a0a0a] ${className}`}
    >
      {!failed ? (
        <Image
          src={`/speakers/${slug}.${ext}`}
          alt={name}
          fill
          sizes="(max-width: 768px) 100vw, 360px"
          className="object-cover object-top"
          onError={() => setFailed(true)}
          unoptimized
        />
      ) : (
        <div className="flex h-full w-full flex-col items-center justify-center gap-1.5">
          <Icon name="users" width={26} height={26} className="text-[var(--gold-4)] opacity-70" />
          <span className="text-gold text-2xl font-extrabold leading-none">{initials(name)}</span>
          <span className="text-[10px] tracking-wide text-[var(--muted-2)]">תמונת מרצה</span>
        </div>
      )}
    </div>
  );
}
