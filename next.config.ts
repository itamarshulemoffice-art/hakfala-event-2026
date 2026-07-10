import type { NextConfig } from "next";

// בסיס הנתיב ל-GitHub Pages (project site יושב תחת /<repo>/).
// נשלט ע"י משתנה סביבה כדי שפיתוח מקומי יישאר ב-"/".
const raw = process.env.NEXT_PUBLIC_BASE_PATH || "";
const basePath = raw ? (raw.startsWith("/") ? raw : "/" + raw) : "";

const nextConfig: NextConfig = {
  output: "export",
  basePath: basePath || undefined,
  assetPrefix: basePath || undefined,
  images: { unoptimized: true },
  trailingSlash: true,
};

export default nextConfig;
