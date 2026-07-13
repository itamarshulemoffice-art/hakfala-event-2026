"use client";

import { Icon } from "../Icons";
import { XOStrip } from "../XOStrip";
import { PISGA_EVENT } from "@/lib/pisga";

export function PisgaForm() {
  return (
    <section className="section" id="register" style={{ background: "linear-gradient(180deg,#0a0503,#000)" }}>
      <div className="wrap-narrow">
        <div className="overflow-hidden rounded-3xl border border-[rgba(212,175,55,0.35)] bg-[#0a0a0a] glow-gold">
          <XOStrip />
          <div className="p-6 sm:p-10">
            <div className="text-center">
              <h2 className="font-extrabold" style={{ fontSize: "clamp(1.7rem,4.5vw,2.5rem)" }}>
                שריינו לעצמכם <span className="text-gold">מקום בפסגה</span>
              </h2>
              <p className="mt-3 text-[var(--muted)]">
                {PISGA_EVENT.date} · פתיחת דלתות: {PISGA_EVENT.time} · {PISGA_EVENT.location} · מספר המקומות מוגבל
              </p>
              <p className="mt-2 text-sm text-[var(--muted-2)]">
                האירוע מתקיים בהפרדה · מתנה לכל משתתף בשווי 300 ₪
              </p>
              <div className="mt-8">
                <a href={PISGA_EVENT.ticketsUrl} target="_blank" rel="noopener" className="btn-gold w-full sm:w-auto">
                  <Icon name="arrow" width={20} height={20} style={{ transform: "scaleX(-1)" }} />
                  לשריון מקום בפסגה &raquo;
                </a>
              </div>
              <p className="mt-4 text-xs text-[var(--muted-2)]">
                הרכישה מאובטחת ומתבצעת דרך מערכת הכרטיסים טיקצ׳אק
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
