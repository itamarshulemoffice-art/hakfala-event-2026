// מזריק את מפתח ה-CRM לדפי הנחיתה הסטטיים אחרי ה-build.
// המפתח מגיע מהסוד CRM_KEY ב-GitHub ולעולם לא נשמר ב-repo.
// בלי סוד, הדפים נשארים עם ה-placeholder והטופס עובר לוואטסאפ.
import { readFileSync, writeFileSync, existsSync } from "node:fs";

const key = (process.env.CRM_KEY || "").trim();
const files = ["out/hachshara/index.html", "out/hachshara/webinar/index.html", "out/hachshara/syllabus/index.html", "out/hachshara/ai-quiz/index.html", "out/hachshara/status/index.html", "out/hachshara/sales/index.html"];

if (!key) { console.log("CRM_KEY not set: forms fall back to WhatsApp."); process.exit(0); }
if (!/^[\w.~-]+$/.test(key)) { console.error("CRM_KEY has unexpected characters."); process.exit(1); }

for (const f of files) {
  if (!existsSync(f)) { console.error(`missing ${f}`); process.exit(1); }
  const src = readFileSync(f, "utf8");
  if (!src.includes("%%CRM_KEY%%")) { console.error(`no placeholder in ${f}`); process.exit(1); }
  writeFileSync(f, src.split("%%CRM_KEY%%").join(key));
  console.log(`CRM key injected: ${f}`);
}
