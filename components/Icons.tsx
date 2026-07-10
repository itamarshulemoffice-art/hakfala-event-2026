import type { ReactNode, SVGProps } from "react";

const base = {
  width: 20,
  height: 20,
  viewBox: "0 0 24 24",
  fill: "none",
  stroke: "currentColor",
  strokeWidth: 1.7,
  strokeLinecap: "round" as const,
  strokeLinejoin: "round" as const,
};

export function Icon({ name, ...p }: { name: string } & SVGProps<SVGSVGElement>) {
  const paths: Record<string, ReactNode> = {
    calendar: (<><rect x="3" y="4" width="18" height="17" rx="2" /><path d="M16 2v4M8 2v4M3 10h18" /></>),
    clock: (<><circle cx="12" cy="12" r="9" /><path d="M12 7v5l3 2" /></>),
    pin: (<><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z" /><circle cx="12" cy="10" r="2.5" /></>),
    split: (<path d="M8 4v16M16 4v16M8 8l8 8M16 8l-8 8" />),
    users: (<><circle cx="9" cy="8" r="3.2" /><path d="M2.5 20a6.5 6.5 0 0 1 13 0" /><path d="M16 5.2a3.2 3.2 0 0 1 0 6.1M18 20a6.5 6.5 0 0 0-3-5.5" /></>),
    alert: (<><path d="M12 3 2 20h20L12 3Z" /><path d="M12 10v4M12 17.5v.5" /></>),
    check: (<path d="M4 12.5 9 17.5 20 6.5" strokeWidth={2.2} />),
    arrow: (<path d="M19 12H5M11 6l-6 6 6 6" />),
    gift: (<><rect x="3" y="9" width="18" height="12" rx="1.5" /><path d="M3 13h18M12 9v12" /><path d="M12 9S9.5 4 7 5.5 9 9 12 9Zm0 0s2.5-5 5-3.5S15 9 12 9Z" /></>),
    spark: (<path d="M12 2v6M12 16v6M2 12h6M16 12h6M5 5l3 3M16 16l3 3M19 5l-3 3M8 16l-3 3" />),
    mic: (<><rect x="9" y="2" width="6" height="12" rx="3" /><path d="M5 11a7 7 0 0 0 14 0M12 18v3" /></>),
    target: (<><circle cx="12" cy="12" r="9" /><circle cx="12" cy="12" r="5" /><circle cx="12" cy="12" r="1.4" fill="currentColor" /></>),
    chat: (<path d="M21 12a8 8 0 0 1-11.5 7.2L4 21l1.8-5.5A8 8 0 1 1 21 12Z" />),
    handshake: (<path d="m11 17 2 2 4-4M3 12l4-4 3 3 3-3 4 4M7 8V5M17 8V5" />),
    phone: (<path d="M6 3h4l2 5-3 2a12 12 0 0 0 5 5l2-3 5 2v4a2 2 0 0 1-2 2A17 17 0 0 1 4 6a2 2 0 0 1 2-3Z" />),
    plus: (<path d="M12 5v14M5 12h14" strokeWidth={2} />),
  };
  return (
    <svg {...base} {...p}>
      {paths[name] ?? null}
    </svg>
  );
}
