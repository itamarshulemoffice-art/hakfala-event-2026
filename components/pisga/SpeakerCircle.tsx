"use client";

import Image from "next/image";
import { useState } from "react";

function initials(name: string) {
  return name.trim().split(" ").slice(0, 2).map((w) => w[0]).join("");
}

/** תמונת מרצה עגולה בצבע מלא עם טבעת זהב (בסגנון הפלייר). fallback לראשי תיבות. */
export function SpeakerCircle({
  img,
  name,
  className = "",
}: {
  img: string;
  name: string;
  className?: string;
}) {
  const [failed, setFailed] = useState(false);
  return (
    <div
      className={`relative aspect-square overflow-hidden rounded-full ${className}`}
      style={{
        padding: 3,
        background: "var(--gold-grad)",
        boxShadow: "0 8px 30px -10px rgba(212,175,55,0.5)",
      }}
    >
      <div className="relative h-full w-full overflow-hidden rounded-full bg-[#0a0a0a]">
        {!failed ? (
          <Image
            src={img}
            alt={name}
            fill
            sizes="200px"
            className="object-cover object-top"
            onError={() => setFailed(true)}
          />
        ) : (
          <div className="flex h-full w-full flex-col items-center justify-center bg-gradient-to-b from-[#1a1710] to-[#070707]">
            <span className="text-gold text-2xl font-extrabold">{initials(name)}</span>
          </div>
        )}
      </div>
    </div>
  );
}
