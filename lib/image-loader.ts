// next/image לא מוסיף לבד את ה-basePath של GitHub Pages ל-src —
// ה-loader הזה משלים את הקידומת לכל תמונה מקומית.
const raw = process.env.NEXT_PUBLIC_BASE_PATH || "";
const basePath = raw ? (raw.startsWith("/") ? raw : "/" + raw) : "";

export default function imageLoader({ src, width }: { src: string; width: number }) {
  const url = src.startsWith("/") ? `${basePath}${src}` : src;
  // הקבצים סטטיים — פרמטר הרוחב נדרש רק כדי לרצות את next/image (השרת מתעלם ממנו)
  return `${url}?w=${width}`;
}
