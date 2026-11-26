from checkout import fields, script, CSS as CO_CSS
# Full paid-traffic sales page for "מכפיל הסטטוס" (300 NIS). Imported by build-sales-pages.py.
import re

S = {
    "name": "מכפיל הסטטוס",
    "price": "300",
    "lessons_count": "11",
    "access": "[[משך הגישה]]",
    # Itamar's own syllabus, from his course deck "מכפיל הסטטוס" (claude.ai artifact BWeKcEW8BeKRVhVmUUmdir, 19.11.2026).
    "lessons": [
        ("מפת הוואטסאפ", "איפה הסטטוס יושב, ולמה זה אחד המקומות הכי פנויים לעסק"),
        ("למה סטטוס מביא לקוחות", "סגור מול פתוח, וארבעת הצעדים מהיכרות לשיחה"),
        ("מי רואה אתכם", "כלל השמירה ההדדית, הגדרות הפרטיות, וי כחול ואפור"),
        ("ארגז הכלים", "ארבעה סוגי סטטוס, לב ירוק, סמיילי, תיוג ושיתוף"),
        ("סטטוס מול סטורי", "שלושה שינויים שהופכים כל תוכן לסטטוס"),
        ("מעבירים מסר", "מסך אחד רעיון אחד, שישה פתיחים, רצף של ארבעה מסכים"),
        ("לא מפחדים למכור", "נוסחת 60% תוכן ו-40% מכירה, ולמה מוכרים על המקום"),
        ("מוכרים בסטטוס", "בקשה במילה אחת, ומה עונים למי שהגיב"),
        ("מגדילים צפיות", "ארבע דרכים בלי לשלם על פרסום"),
        ("פרסום ממומן בסטטוס", "קמפיין שמביא אנשי קשר, ומודעות בתוך הסטטוס"),
        ("מודדים ויוצאים לדרך", "ארבעה מספרים, ותוכנית לשבוע הראשון"),
    ],
    "bonuses": [
        ("דף העבודה", "כל הכלים מהקורס בעמוד אחד להדפסה: רצף ארבעת המסכים, ששת הפתיחים, התסריט לשיחה, וארבעת המספרים."),
        ("גאנט תוכן לחודש", "20 ימים, 60 סטטוסים, מחולקים מראש לפי 60/40. לכל משבצת כתוב מה עולה בה."),
        ("מפלצת הסטטוס", "סוכן AI שמדביקים ב-ChatGPT, ב-Gemini או ב-Claude. הוא לומד את העסק שלכם ומגיש כל בוקר חבילת תוכן מלאה: טקסט, רעיון לסרטון, גרפיקה, רצף של ארבעה מסכים ותגובות מוכנות."),
    ],
    "testimonials": [
        ("[[שם]]", "[[סוג העסק]]", "[[משפט אחד מהעדות]]"),
        ("[[שם]]", "[[סוג העסק]]", "[[משפט אחד מהעדות]]"),
        ("[[שם]]", "[[סוג העסק]]", "[[משפט אחד מהעדות]]"),
    ],
    "faq": [
        ("לכמה זמן יש גישה לקורס?", "[[משך הגישה]]"),
        ("איך מקבלים את הקורס?", "מיד אחרי התשלום נשלח אליכם קישור כניסה במייל ובוואטסאפ. [[לאשר את אופן המסירה]]"),
        ("כמה זמן זה לוקח?", "11 שיעורים קצרים, פחות משעה בסך הכול. אפשר לצפות בישיבה אחת, או שיעור ביום."),
        ("אני לא טכני. זה יתאים לי?", "כן. הקורס מתחיל מהבסיס: מה זה הלשוניות, איפה הסטטוס, ואיך מעלים. כל מה שצריך זה טלפון עם וואטסאפ."),
        ("צריך וואטסאפ ביזנס?", "לא חובה. הסטטוס עובד גם בוואטסאפ רגיל. בקורס מוסבר ההבדל."),
        ("אין לי הרבה אנשי קשר. יש טעם?", "כן. שיעור שלם עוסק בהגדלת צפיות בלי לשלם על פרסום, ושיעור נוסף בפרסום ממומן."),
        ("אני לא יודע מה להעלות.", "בדיוק בשביל זה יש את הגאנט ואת מפלצת הסטטוס. הם נותנים לכם מה להעלות, יום אחרי יום."),
        ("אפשר לבטל?", "כן, לפי מדיניות הביטולים שבתקנון. הקישור בתחתית הדף."),
    ],
}

CSS = r"""
.pain{list-style:none;padding:0;margin:0 0 8px}.pain li{position:relative;padding:10px 30px 10px 0;border-bottom:1px solid rgba(0,0,0,.08);font-size:18px}.pain li:before{content:"✕";position:absolute;right:0;top:10px;color:#a3201a;font-weight:900}
.bon{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;margin-top:22px}
.bon>div{border:1px solid var(--line);border-top:3px solid var(--gold);border-radius:14px;padding:20px;background:var(--ink2)}
.bon span{font-size:13px;font-weight:800;color:var(--gold);letter-spacing:.04em}
.bon b{display:block;font-family:var(--display);font-size:22px;margin:4px 0 6px}
.bon p{margin:0;color:#d8d2c4;font-size:16px}
@media (max-width:860px){.bon{grid-template-columns:minmax(0,1fr)}}
/* LAYOUT: split hero (photo half / promise half), then a story told down the page: problem, turn, method, proof, offer. */
:root{color-scheme:dark;--ink:#0b0b0a;--ink2:#151513;--paper:#f7f3ea;--paperInk:#171614;--line:#2d2b26;--gold:#d4af37;--gold2:#f3dc8a;--text:#f3efe5;--mute:#a9a395;--wa:#25d366;
--display:"Rubik","Heebo",Arial,sans-serif;--body:"Heebo",Arial,sans-serif}
*{box-sizing:border-box;min-width:0}
body{margin:0;background:var(--ink);color:var(--text);font:17.5px/1.7 var(--body);overflow-x:clip}
a{color:inherit}img{max-width:100%;display:block}
.wrap{max-width:1120px;margin:0 auto;padding-left:max(18px,env(safe-area-inset-left,0px));padding-right:max(18px,env(safe-area-inset-right,0px))}
.narrow{max-width:760px}
h2{font-family:var(--display);font-weight:900;font-size:clamp(30px,4.2vw,46px);line-height:1.08;margin:0 0 14px;text-wrap:balance}
h2 em{font-style:normal;color:var(--gold)}
.eyebrow{display:inline-block;font-weight:800;font-size:13.5px;letter-spacing:.06em;color:var(--gold);margin:0 0 10px}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;background:var(--gold);color:#111;font-weight:900;font-size:19px;border:0;border-radius:12px;padding:16px 28px;min-height:58px;text-decoration:none;cursor:pointer}
.btn:hover{background:var(--gold2)}
.btn:focus-visible,input:focus-visible,summary:focus-visible,a:focus-visible{outline:3px solid #fff;outline-offset:2px}
.micro{font-size:13.5px;color:var(--mute);margin:10px 0 0}
mark.todo{background:#ffe066;color:#111;border-radius:4px;padding:0 4px;font-weight:700}

/* split hero */
.split{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);min-height:min(92vh,760px)}
.split .pic{position:relative;background:#1a1a18}
.split .pic img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center 15%}
.split .pic:after{content:"";position:absolute;inset:0;background:linear-gradient(270deg,rgba(11,11,10,0) 55%,var(--ink) 100%)}
.split .pic .cap{position:absolute;bottom:18px;left:20px;right:20px;z-index:1;font-size:14px;color:#e9e3d6}
.split .pic .cap b{display:block;font-size:19px;color:#fff}
.split .txt{display:flex;flex-direction:column;justify-content:center;padding:40px max(28px,5vw)}
.split .logo{height:44px;width:auto;margin-bottom:34px}
.split h1{font-family:var(--display);font-weight:900;font-size:clamp(40px,5.6vw,72px);line-height:1;margin:0 0 18px;letter-spacing:-.01em;text-wrap:balance}
.split h1 b{color:var(--gold)}
.split .lead{font-size:20px;color:#ddd6c6;margin:0 0 22px;max-width:30em}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 26px;padding:0;list-style:none}
.chips li{border:1px solid var(--line);border-radius:999px;padding:6px 14px;font-size:14.5px;font-weight:700;background:var(--ink2)}

/* sections */
section.s{padding-block:76px}
section.light{background:var(--paper);color:var(--paperInk)}
section.light .mute{color:#5f5b52}
.story p{font-size:19px;margin:0 0 16px}
.story .big{font-family:var(--display);font-weight:800;font-size:clamp(24px,3vw,32px);line-height:1.25;color:var(--gold);margin:28px 0}
section.light .story .big{color:#8a6a1c}
.phone{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px;margin-top:30px}
.phone div{background:#fff;border:1px solid #e5dccb;border-radius:16px;padding:18px}
.phone b{display:block;font-family:var(--display);font-size:34px;line-height:1;color:#8a6a1c}
.phone span{font-size:15px;color:#5f5b52}
.who{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:44px;align-items:center}
.who img{border-radius:18px;width:100%;aspect-ratio:1/1;object-fit:cover}
.who ul{list-style:none;margin:18px 0 0;padding:0}
.who li{padding:10px 30px 10px 0;border-bottom:1px solid var(--line);position:relative}
.who li:before{content:"";position:absolute;right:4px;top:19px;width:10px;height:10px;border-radius:50%;background:var(--gold)}
.vids{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}
.vid{border-radius:16px;overflow:hidden;background:var(--ink2);border:1px solid var(--line)}
.vid .frame{position:relative;aspect-ratio:9/12;background:radial-gradient(circle at 50% 40%,#2a2720,#121210);display:grid;place-items:center}
.vid .play{width:64px;height:64px;border-radius:50%;background:var(--gold);display:grid;place-items:center}
.vid .play:after{content:"";border-style:solid;border-width:12px 0 12px 20px;border-color:transparent transparent transparent #111;margin-left:5px}
.vid .frame small{position:absolute;bottom:12px;left:0;right:0;text-align:center;font-size:13px;color:var(--mute)}
.vid .q{padding:16px}
.vid .q p{margin:0 0 8px;font-weight:700}
.vid .q span{font-size:14px;color:var(--mute)}
.more{margin-top:20px;font-weight:700}.more a{color:var(--gold2)}
.syll{list-style:none;margin:0;padding:0;counter-reset:l;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}
.syll li{counter-increment:l;background:#fff;border:1px solid #e5dccb;border-radius:16px;padding:20px 20px 20px 20px;display:grid;grid-template-columns:52px minmax(0,1fr);gap:14px;align-items:start}
.syll li:before{content:counter(l,decimal-leading-zero);font-family:var(--display);font-weight:900;font-size:30px;color:#c9a44b;line-height:1}
.syll h3{margin:0 0 4px;font-size:19px;line-height:1.3}
.syll p{margin:0;font-size:15.5px;color:#5f5b52}
.how{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:14px;counter-reset:h}
.how div{counter-increment:h;border-top:3px solid var(--gold);padding-top:14px}
.how div:before{content:"שלב " counter(h);display:block;font-size:13px;font-weight:800;color:var(--gold);letter-spacing:.04em}
.how b{display:block;font-size:19px;margin:4px 0}
.how p{margin:0;font-size:15.5px;color:var(--mute)}
.fit{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:40px}
ul.chk{list-style:none;margin:0;padding:0}
ul.chk li{padding:10px 30px 10px 0;border-bottom:1px solid var(--line);position:relative}
ul.chk li:before{content:"✓";position:absolute;right:4px;top:10px;color:var(--gold);font-weight:900}
ul.chk.no li:before{content:"✕";color:#8d887c}
.offer{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);gap:40px;align-items:start}
.card{border:2px solid var(--gold);border-radius:20px;padding:28px;background:var(--ink2)}
.card .p{font-family:var(--display);font-size:72px;font-weight:900;line-height:1;color:var(--gold2);margin:8px 0 4px}
.card .p small{font-size:28px}
.card .pn{color:var(--mute);font-size:14px;margin:0 0 18px}
.card .btn{width:100%}
.card a:not(.btn){color:var(--gold2)}
label.c{display:flex;gap:10px;align-items:flex-start;font-size:14px;color:#cfc8b8;margin:0 0 14px}
label.c input{width:20px;height:20px;accent-color:var(--gold);flex:none;margin-top:2px}
.err{color:#ff9a9a;font-size:14px;min-height:20px;margin-top:8px}
details{border:1px solid var(--line);border-radius:12px;padding:14px 18px;margin:0 0 10px;background:var(--ink2)}
summary{cursor:pointer;font-weight:800;font-size:18px}
details p{margin:10px 0 0;color:#d8d2c4}
footer.legal{border-top:1px solid var(--line);padding-block:28px 96px;color:#8d887c;font-size:13.5px}
footer.legal p{margin:0 0 6px}footer.legal a{color:#cfc9bb}footer.legal .pay{font-size:12.5px;color:#7d786d}
.dock{position:fixed;bottom:0;left:0;right:0;z-index:9;display:none;gap:12px;align-items:center;justify-content:space-between;background:rgba(11,11,10,.95);border-top:1px solid var(--line);
padding:10px max(16px,env(safe-area-inset-right,0px)) calc(10px + env(safe-area-inset-bottom,0px)) max(16px,env(safe-area-inset-left,0px))}
.dock b{font-family:var(--display);font-size:18px}.dock .btn{min-height:46px;padding:10px 18px;font-size:16px}
@media(max-width:860px){
.split{grid-template-columns:minmax(0,1fr);min-height:0}.split .pic{aspect-ratio:4/4.2}.split .pic:after{background:linear-gradient(180deg,rgba(11,11,10,0) 55%,var(--ink) 100%)}
.split .txt{padding:8px 18px 40px}.split .logo{position:absolute;top:16px;right:16px;margin:0;height:38px}.split{position:relative}
.who,.fit,.offer,.syll{grid-template-columns:minmax(0,1fr)}.vids{grid-template-columns:minmax(0,1fr) minmax(0,1fr)}.vids .vid:nth-child(3){display:none}
.how{grid-template-columns:minmax(0,1fr) minmax(0,1fr)}.phone{grid-template-columns:minmax(0,1fr)}.dock{display:flex}section.s{padding-block:56px}}
"""


def status_page(t, footer, biz):
    s = S
    li = lambda xs, cls="chk": f'<ul class="{cls}">' + "".join(f"<li>{t(x)}</li>" for x in xs) + "</ul>"
    syll = "".join(f"<li><div><h3>{t(h)}</h3><p>{t(p)}</p></div></li>" for h, p in s["lessons"])
    vids = "".join(f'<div class="vid"><div class="frame"><span class="play" aria-hidden="true"></span><small>{t("[[סרטון עדות]]")}</small></div><div class="q"><p>"{t(q)}"</p><span>{t(n)} · {t(b)}</span></div></div>' for n, b, q in s["testimonials"])
    bons = "".join(f'<div><span>בונוס {i}</span><b>{t(h)}</b><p>{t(p)}</p></div>' for i, (h, p) in enumerate(s["bonuses"], 1))
    faq = "".join(f"<details><summary>{t(q)}</summary><p>{t(a)}</p></details>" for q, a in s["faq"])
    return f"""<!DOCTYPE html><html lang="he" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{s['name']}</title><meta name="description" content="מכפיל הסטטוס, הקורס של איתמר שולם: השיטה שהופכת צופים בוואטסאפ ללקוחות. 11 שיעורים קצרים, 3 בונוסים, 300 ₪.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Heebo:wght@400;700;800;900&family=Rubik:wght@700;800;900&display=swap" rel="stylesheet">
<!-- Meta Pixel / Google tag: להדביק כאן את הקודים מיצחק. בלחיצה על התשלום הדף קורא ל-fbq('track','InitiateCheckout') אם הפיקסל מותקן. -->
<style>{CSS}{CO_CSS}</style></head><body>

<header class="split">
<div class="pic"><img src="../hachshara-itamar.webp" alt="{biz['owner']}"><p class="cap"><b>{biz['owner']}</b>מייסד {biz['brand']} · 13 שנים במכירות</p></div>
<div class="txt"><img class="logo" src="../hachshara-logo.webp" alt="{biz['brand']}">
<p class="eyebrow">קורס דיגיטלי · {s['name']}</p>
<h1>{s['name']}<br><b>השיטה שהופכת צופים בוואטסאפ ללקוחות.</b></h1>
<p class="lead">הלקוחות שלכם פותחים וואטסאפ עשרות פעמים ביום. הגיע הזמן שיראו אתכם שם, ויקנו. 11 שיעורים קצרים, משימה בכל שיעור, ושלושה בונוסים.</p>
<ul class="chips"><li>11 שיעורים קצרים</li><li>משימה בכל שיעור</li><li>3 בונוסים</li><li>300 ₪, תשלום אחד</li></ul>
<div><a class="btn" href="#buy">אני רוצה את הקורס · 300 ₪ &#8592;</a><p class="micro">תשלום מאובטח · ביטול לפי התקנון</p></div>
</div>
</header>

<section class="s light"><div class="wrap narrow story">
<p class="eyebrow" style="color:#8a6a1c">מוכר לכם?</p>
<h2>אתם טובים במה שאתם עושים. <em style="color:#8a6a1c">רק שאף אחד לא יודע.</em></h2>
<ul class="pain"><li>אתם מעלים פוסטים לאינסטגרם, ומקבלים לייקים מחברים. לקוחות לא מגיעים.</li><li>יש לכם מאות אנשי קשר בוואטסאפ, ורובם שכחו מה אתם מוכרים.</li><li>אתם מעלים סטטוס פעם בשבוע, ורואים שצפו בו עשרים אנשים.</li><li>לא נעים לכם למכור. אז אתם נותנים, ונותנים, ומחכים שמישהו יבקש.</li><li>אין לכם מושג מה להעלות מחר בבוקר.</li></ul>
<p class="big">אם לא תספרו, אף אחד לא ידע.</p>
<p>לא שיתפתם את המוצר? אף אחד לא יכול לבקש אותו. לא שיווקתם? אף אחד לא יודע להעריך אתכם. לא מכרתם? לא עזרתם לאף אחד.</p>
<p>כמעט חמש שנים אני מעלה סטטוס כל יום. כל יום. היום צופים בסטטוס שלי אלפי אנשים, ויותר ממאה בעלי עסקים נכנסו אצלנו לליווי פרימיום מהסטטוס בלבד. בלי מודעה, בלי דף נחיתה.</p>
<p>ולמה זה עובד? כי מי שרואה את הסטטוס שלכם הוא לא עוקב אקראי. יש ביניכם מספר טלפון. הוא פוגש אתכם כל יום, בלי אלגוריתם שמחליט אם להראות אתכם. וכשהוא מגיב, אתם כבר בשיחה פרטית איתו.</p>
<p class="big">רשת פתוחה מביאה חשיפה. סטטוס מביא שיחות.</p>
<p>הקורס הזה הוא השיטה שלי, צעד אחרי צעד: קודם מבינים את המגרש, אחר כך יוצרים ומוכרים, ורק אז מגדילים צפיות. כי מי שמגדיל צפיות לפני שיש לו מסר, מגדיל רעש.</p>
<div class="phone"><div><b>5</b><span>שנים כמעט, סטטוס כל יום</span></div><div><b>+100</b><span>בעלי עסקים נכנסו לליווי, מהסטטוס בלבד</span></div><div><b>60/40</b><span>תוכן מול מכירה. הנוסחה שבקורס</span></div></div>
</div></section>

<section class="s"><div class="wrap who">
<img src="../hachshara-event.jpg" alt="איתמר שולם על הבמה מול קהל בעלי עסקים">
<div><p class="eyebrow">מי אני</p><h2>איתמר <em>שולם</em></h2>
<p style="margin:0;color:#ddd6c6">אני מלווה בעלי עסקים להכפיל את העסק שלהם. את מה שעובד בשטח אני מלמד בקורסים, בהרצאות ובפודקאסט.</p>
<ul><li>מייסד הכפלה עסקית. מלווה בעלי עסקים בשיטה של חמש תחנות: שיקוף, תשתית, מוצר והצעה, מכירות, שיווק</li><li>13 שנים בעולם המכירות</li><li>כמעט 5 שנים סטטוס כל יום, ואלפי צופים</li><li>מגיש את הפודקאסט "הכפלה עסקית" ומרצה בפני בעלי עסקים</li></ul>
<p style="margin:14px 0 0;color:var(--gold2);font-weight:700">כל מה שיש בקורס, אני עושה בעצמי כל בוקר.</p></div>
</div></section>

<section class="s" style="padding-top:0"><div class="wrap">
<p class="eyebrow">מה אומרים</p><h2>בעלי עסקים <em>מספרים</em></h2>
<div class="vids">{vids}</div>
<p class="more">עוד עדויות של בעלי עסקים <a href="https://www.youtube.com/@%D7%90%D7%99%D7%AA%D7%9E%D7%A8%D7%A9%D7%95%D7%9C%D7%9D" target="_blank" rel="noopener">בערוץ היוטיוב של איתמר &#8592;</a></p>
</div></section>

<section class="s light"><div class="wrap">
<p class="eyebrow" style="color:#8a6a1c">מה לומדים</p><h2>{t(s['lessons_count'])} שיעורים. <em style="color:#8a6a1c">שיטה אחת.</em></h2>
<p class="mute" style="margin:0 0 28px">פחות משעה של צפייה. כל שיעור עונה על שאלה אחת, ונגמר במשימה אחת.</p>
<ol class="syll">{syll}</ol>
<div class="cta" style="margin-top:28px"><a class="btn" href="#buy">אני רוצה את הקורס · 300 ₪ &#8592;</a></div>
</div></section>

<section class="s"><div class="wrap">
<p class="eyebrow">הבונוסים</p><h2>שלושה בונוסים <em>שעושים את העבודה</em></h2>
<div class="bon">{bons}</div>
</div></section>

<section class="s light"><div class="wrap narrow story">
<p class="eyebrow" style="color:#8a6a1c">הנוסחה</p><h2>60% תוכן. <em style="color:#8a6a1c">40% מכירה.</em></h2>
<p>רוב העסקים נותנים, נותנים, נותנים, ומפחדים להציע. בקורס תלמדו למכור על המקום: אנשים קונים ממי שנותן, אבל רק אם הוא גם מציע. וגם מי שלא קונה היום מבין שיש לכם מה לתת, ולכן הוא נשאר.</p>
<p class="big">מכירה היא לא טובה שעושים לכם. מכירה היא הטוב שאתם עושים לאחרים.</p>
</div></section>

<section class="s"><div class="wrap">
<p class="eyebrow">איך זה עובד</p><h2>מהתשלום לסטטוס <em>הראשון</em></h2>
<div class="how" style="margin-top:26px">
<div><b>נרשמים</b><p>תשלום מאובטח של 300 ₪. הקבלה מגיעה למייל.</p></div>
<div><b>מקבלים גישה</b><p>קישור כניסה נשלח מיד במייל ובוואטסאפ.</p></div>
<div><b>צופים</b><p>מהטלפון או מהמחשב, בקצב שלך. גישה ל{t(s['access'])}.</p></div>
<div><b>מעלים</b><p>משימה בסוף כל שיעור, וגאנט תוכן לחודש שלם.</p></div>
</div></div></section>

<section class="s" style="padding-top:0"><div class="wrap fit">
<div><h2 style="font-size:32px">למי זה <em>מתאים</em></h2>{li(["יש לכם עסק, ואתם מוכרים שירות או מוצר", "יש לכם וואטסאפ, ואנשים שכבר דיברו איתכם", "אתם מוכנים להעלות סטטוס כל יום, לפחות חודש"])}</div>
<div><h2 style="font-size:32px">למי <em>פחות</em></h2>{li(["אתם מחפשים קסם בלי לעבוד", "אין לכם עדיין מה למכור", "אתם לא מוכנים להציע את המוצר שלכם בקול"], "chk no")}</div>
</div></section>

<section class="s" id="buy" style="border-top:1px solid var(--line)"><div class="wrap offer">
<div><p class="eyebrow">ההצעה</p><h2>{s['name']}<br><em>במחיר של ארוחה אחת בחוץ</em></h2>
<ul class="chk"><li>11 שיעורים מוקלטים, קצרים וממוקדים</li><li>משימה מעשית בסוף כל שיעור</li><li>בונוס 1: דף העבודה</li><li>בונוס 2: גאנט תוכן לחודש שלם</li><li>בונוס 3: מפלצת הסטטוס, סוכן AI שמגיש לכם חבילת תוכן כל בוקר</li><li>גישה מיידית ל{t(s['access'])}</li></ul>
<p class="micro" style="font-size:15px">שאלה לפני שקונים? <a href="https://wa.me/{biz['wa']}" style="color:var(--gold2);font-weight:700">כתבו לאיתמר בוואטסאפ</a></p></div>
<div class="card"><p style="margin:0;color:#cfc8b8;font-weight:700">{s['name']} · קורס דיגיטלי</p>
<p class="p">300 <small>₪</small></p><p class="pn">תשלום אחד, כולל מע"מ</p>
{fields()}
<p class="micro">אחרי התשלום תקבלו קבלה וקישור כניסה לקורס במייל ובוואטסאפ.</p></div>
</div></section>

<section class="s" style="padding-top:0"><div class="wrap narrow"><p class="eyebrow">שאלות</p><h2>שאלות <em>נפוצות</em></h2>{faq}</div></section>
{footer(1)}
<div class="dock"><b>{s['name']} · 300 ₪</b><a class="btn" href="#buy">לרכישה</a></div>
{script('%%PAY_URL_STATUS%%','status-course-checkout',s['name'],'300',biz['wa'])}</body></html>
"""
