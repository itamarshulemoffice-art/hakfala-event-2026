/* מוטיב החתימה של המותג: פס XOXO — איקסים זהב ועיגולים */
export function XOStrip({ className = "", flip = false }: { className?: string; flip?: boolean }) {
  return (
    <div
      className={className}
      aria-hidden
      style={{
        height: 46,
        width: "100%",
        transform: flip ? "scaleY(-1)" : undefined,
        backgroundImage: "url(\"data:image/svg+xml," + encodeURIComponent(SVG) + "\")",
        backgroundRepeat: "repeat-x",
        backgroundPosition: "center",
        backgroundSize: "auto 46px",
        opacity: 0.9,
      }}
    />
  );
}

const SVG = `<svg xmlns='http://www.w3.org/2000/svg' width='184' height='46' viewBox='0 0 184 46'>
  <defs>
    <linearGradient id='g' x1='0' y1='0' x2='1' y2='1'>
      <stop offset='0' stop-color='#f7ead0'/>
      <stop offset='0.35' stop-color='#e7cf8f'/>
      <stop offset='0.6' stop-color='#d4af37'/>
      <stop offset='1' stop-color='#8a6410'/>
    </linearGradient>
  </defs>
  <g transform='translate(0,3)'>
    <!-- X -->
    <g transform='translate(4,4)'>
      <path d='M2 2 L32 32 M32 2 L2 32' stroke='url(#g)' stroke-width='9' stroke-linecap='square'/>
    </g>
    <!-- O -->
    <circle cx='66' cy='21' r='16' fill='none' stroke='#ffffff' stroke-width='7'/>
    <!-- X -->
    <g transform='translate(88,4)'>
      <path d='M2 2 L32 32 M32 2 L2 32' stroke='url(#g)' stroke-width='9' stroke-linecap='square'/>
    </g>
    <!-- O -->
    <circle cx='150' cy='21' r='16' fill='none' stroke='url(#g)' stroke-width='7'/>
  </g>
</svg>`;
