/* אמבלמת הפסגה: דגל שחור מתנופף עם כוכב זהב זוהר וקרני אור — בהשראת הפלייר */
export function SummitEmblem({ className = "" }: { className?: string }) {
  return (
    <svg viewBox="0 0 300 300" className={className} aria-hidden role="img">
      <defs>
        <linearGradient id="goldG" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0" stopColor="#fff3cf" />
          <stop offset="0.45" stopColor="#e7cf8f" />
          <stop offset="0.7" stopColor="#d4af37" />
          <stop offset="1" stopColor="#8a6410" />
        </linearGradient>
        <linearGradient id="poleG" x1="0" y1="0" x2="1" y2="0">
          <stop offset="0" stopColor="#8a6410" />
          <stop offset="0.5" stopColor="#f7ead0" />
          <stop offset="1" stopColor="#8a6410" />
        </linearGradient>
        <linearGradient id="flagG" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0" stopColor="#1c1a15" />
          <stop offset="0.5" stopColor="#0c0b08" />
          <stop offset="1" stopColor="#050505" />
        </linearGradient>
        <radialGradient id="bloomG" cx="50%" cy="50%" r="50%">
          <stop offset="0" stopColor="rgba(212,175,55,0.55)" />
          <stop offset="0.4" stopColor="rgba(212,175,55,0.22)" />
          <stop offset="1" stopColor="rgba(212,175,55,0)" />
        </radialGradient>
        <filter id="starGlow" x="-80%" y="-80%" width="260%" height="260%">
          <feGaussianBlur stdDeviation="4.5" result="b" />
          <feMerge>
            <feMergeNode in="b" />
            <feMergeNode in="SourceGraphic" />
          </feMerge>
        </filter>
      </defs>

      {/* זוהר רקע */}
      <circle cx="150" cy="120" r="120" fill="url(#bloomG)" />

      {/* תורן */}
      <rect x="196" y="18" width="4" height="250" rx="2" fill="url(#poleG)" />
      <circle cx="198" cy="16" r="7" fill="url(#goldG)" />

      {/* דגל מתנופף — קבוצה עם נדנוד עדין */}
      <g style={{ animation: "flag-wave 6s ease-in-out infinite", transformOrigin: "198px 60px", transformBox: "fill-box" }}>
        <path
          d="M196 34 L70 46 C52 62 52 78 66 96 C52 114 52 130 70 146 L196 132 Z"
          fill="url(#flagG)"
          stroke="url(#goldG)"
          strokeWidth="1.5"
        />
        {/* קרני אור מסתובבות */}
        <g style={{ animation: "ray-spin 26s linear infinite", transformOrigin: "128px 90px", transformBox: "fill-box", opacity: 0.5 }}>
          {Array.from({ length: 12 }).map((_, i) => (
            <rect
              key={i}
              x="127"
              y="46"
              width="2"
              height="44"
              rx="1"
              fill="url(#goldG)"
              transform={`rotate(${i * 30} 128 90)`}
            />
          ))}
        </g>
        {/* כוכב זהב זוהר */}
        <g filter="url(#starGlow)" className="star-glow">
          <path
            d="M128 55 L138.5 84 L169 84.5 L144.5 102.5 L153.5 132 L128 114 L102.5 132 L111.5 102.5 L87 84.5 L117.5 84 Z"
            fill="url(#goldG)"
          />
        </g>
      </g>
    </svg>
  );
}
