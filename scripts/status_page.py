from checkout import fields, script, CSS as CO_CSS
# Full paid-traffic sales page for "הכפלה בסטטוס" (300 NIS). Imported by build-sales-pages.py.
import re

S = {
    "name": "הכפלה בסטטוס",
    "price": "300",
    "lessons_count": "[[מספר]]",
    "access": "[[משך הגישה]]",
    # Proposed syllabus. Itamar to confirm titles, order and lengths.
    # Lesson list comes from Itamar (his own status course). Do not fill from other people's courses.
    "lessons": [(f"[[שם שיעור {i}]]", "[[משפט אחד: מה לומדים ומה יוצאים איתו]]") for i in range(1, 7)],
    "testimonials": [
        ("[[שם]]", "[[סוג העסק]]", "[[משפט אחד מהעדות]]"),
        ("[[שם]]", "[[סוג העסק]]", "[[משפט אחד מהעדות]]"),
        ("[[שם]]", "[[סוג העסק]]", "[[משפט אחד מהעדות]]"),
    ],
    "faq": [
        ("לכמה זמן יש גישה לקורס?", "[[משך הגישה]]"),
        ("איך מקבלים את הקורס?", "מיד אחרי התשלום נשלח אליכם קישור כניסה במייל ובוואטסאפ. [[לאשר את אופן המסירה]]"),
        ("כמה זמן לוקח כל שיעור?", "[[משך שיעור ממוצע]]. אפשר לראות בטלפון, בכל זמן."),
        ("זה מתאים גם לעסק קטן מאוד?", "כן. הסטטוס עובד בדיוק בגלל שאנשים מכירים אותך. ככל שהעסק אישי יותר, הוא עובד טוב יותר."),
        ("אני לא טוב בכתיבה. זה בשבילי?", "כן. הקורס נותן מבנים מוכנים, כך שלא צריך להמציא כל יום מאפס."),
        ("אפשר לבטל?", "כן, לפי מדיניות הביטולים שבתקנון. הקישור בתחתית הדף."),
    ],
}

CSS = r"""
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
    faq = "".join(f"<details><summary>{t(q)}</summary><p>{t(a)}</p></details>" for q, a in s["faq"])
    return f"""<!DOCTYPE html><html lang="he" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{s['name']}</title><meta name="description" content="הקורס של איתמר שולם: איך הופכים את הסטטוס בוואטסאפ לערוץ שמביא פניות ולקוחות. 300 ₪, גישה מיידית.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Heebo:wght@400;700;800;900&family=Rubik:wght@700;800;900&display=swap" rel="stylesheet">
<!-- Meta Pixel / Google tag: להדביק כאן את הקודים מיצחק. בלחיצה על התשלום הדף קורא ל-fbq('track','InitiateCheckout') אם הפיקסל מותקן. -->
<style>{CSS}{CO_CSS}</style></head><body>

<header class="split">
<div class="pic"><img src="../hachshara-itamar.webp" alt="{biz['owner']}"><p class="cap"><b>{biz['owner']}</b>מייסד {biz['brand']} · 13 שנים במכירות</p></div>
<div class="txt"><img class="logo" src="../hachshara-logo.webp" alt="{biz['brand']}">
<p class="eyebrow">קורס דיגיטלי · {s['name']}</p>
<h1>מאות אנשים רואים את הסטטוס שלך כל יום.<br><b>הגיע הזמן שהם גם יקנו.</b></h1>
<p class="lead">בקורס "{s['name']}" איתמר שולם מראה את השיטה שהופכת את הסטטוס בוואטסאפ לערוץ קבוע שמביא פניות, בלי לשלם שקל על פרסום. {t('[[משפט ההבטחה המדויק]]')}</p>
<ul class="chips"><li>{t(s['lessons_count'])} שיעורים מוקלטים</li><li>גישה מיידית</li><li>צופים מהטלפון</li><li>300 ₪, תשלום אחד</li></ul>
<div><a class="btn" href="#buy">אני רוצה את הקורס · 300 ₪ &#8592;</a><p class="micro">תשלום מאובטח · ביטול לפי התקנון</p></div>
</div>
</header>

<section class="s light"><div class="wrap narrow story">
<p class="eyebrow" style="color:#8a6a1c">הסיפור</p>
<h2>יש לך ערוץ פרסום שכבר עובד. <em style="color:#8a6a1c">פשוט אף אחד לא לימד אותך להשתמש בו.</em></h2>
<p>כל בוקר, מאות אנשים פותחים את הוואטסאפ ורואים מה העלית. לקוחות קודמים, שכנים, חברים, אנשים ששמרו את המספר שלך פעם. הם כבר מכירים אותך, ורובם כבר סומכים עליך.</p>
<p>ומה הם רואים שם? תמונה של מוצר עם "מבצע!". ברכה לשבת. או כלום.</p>
<p class="big">הם צופים. הם לא כותבים. והכסף נשאר על השולחן.</p>
<p>{t('[[הסיפור של איתמר: איך הגיע לשיטת הסטטוס, מה ראה אצל בעלי העסקים שליווה, ומה השתנה כשהתחילו לעבוד נכון. 3-4 משפטים בשפה שלו]]')}</p>
<p>הקורס הזה הוא השיטה עצמה: מה מעלים, מתי, ואיך גורמים לאדם שצפה לשלוח לך הודעה. ואז, מה עונים לו כדי שזה ייגמר בעסקה.</p>
<div class="phone"><div><b>{t('[[מספר]]')}</b><span>{t('[[נתון אמיתי, למשל: צפיות ממוצעות בסטטוס של בעל עסק]]')}</span></div><div><b>0 ₪</b><span>עלות הפרסום בסטטוס</span></div><div><b>24</b><span>שעות שכל סטטוס נשאר מול העיניים שלהם</span></div></div>
</div></section>

<section class="s"><div class="wrap who">
<img src="../hachshara-event.jpg" alt="איתמר שולם על הבמה מול קהל בעלי עסקים">
<div><p class="eyebrow">מי אני</p><h2>איתמר <em>שולם</em></h2>
<p style="margin:0;color:#ddd6c6">אני מלווה בעלי עסקים להכפיל את העסק שלהם. את מה שעובד בשטח אני מלמד בקורסים, בהרצאות ובפודקאסט.</p>
<ul><li>מייסד הכפלה עסקית, חברה לליווי וייעוץ לבעלי עסקים</li><li>13 שנים בעולם המכירות</li><li>ליווה למעלה מ-100 בעלי עסקים בשנה האחרונה</li><li>מגיש את הפודקאסט "הכפלה עסקית" ומרצה בפני בעלי עסקים</li></ul></div>
</div></section>

<section class="s" style="padding-top:0"><div class="wrap">
<p class="eyebrow">מה אומרים</p><h2>בעלי עסקים <em>מספרים</em></h2>
<div class="vids">{vids}</div>
<p class="more">עוד עדויות של בעלי עסקים <a href="https://www.youtube.com/@%D7%90%D7%99%D7%AA%D7%9E%D7%A8%D7%A9%D7%95%D7%9C%D7%9D" target="_blank" rel="noopener">בערוץ היוטיוב של איתמר &#8592;</a></p>
</div></section>

<section class="s light"><div class="wrap">
<p class="eyebrow" style="color:#8a6a1c">מה לומדים</p><h2>{t(s['lessons_count'])} שיעורים. <em style="color:#8a6a1c">שיטה אחת.</em></h2>
<p class="mute" style="margin:0 0 28px">כל שיעור קצר ומעשי. רואים, ומעלים את הסטטוס הראשון כבר באותו יום.</p>
<ol class="syll">{syll}</ol>
</div></section>

<section class="s"><div class="wrap">
<p class="eyebrow">איך זה עובד</p><h2>מהתשלום לסטטוס <em>הראשון</em></h2>
<div class="how" style="margin-top:26px">
<div><b>נרשמים</b><p>תשלום מאובטח של 300 ₪. הקבלה מגיעה למייל.</p></div>
<div><b>מקבלים גישה</b><p>קישור כניסה נשלח מיד במייל ובוואטסאפ.</p></div>
<div><b>צופים</b><p>מהטלפון או מהמחשב, בקצב שלך. גישה ל{t(s['access'])}.</p></div>
<div><b>מעלים</b><p>לפי התוכנית ל-30 יום, סטטוס אחרי סטטוס.</p></div>
</div></div></section>

<section class="s" style="padding-top:0"><div class="wrap fit">
<div><h2 style="font-size:32px">למי זה <em>מתאים</em></h2>{li(["בעלי עסקים קטנים שמוכרים בוואטסאפ", "נותני שירות שרוצים יותר פניות בלי עוד פרסום", "מי שיש לו מאות אנשי קשר ולא מנצל אותם"])}</div>
<div><h2 style="font-size:32px">למי <em>פחות</em></h2>{li(["מי שמחפש פתרון בלי לעבוד עליו", "עסקים שלא מוכרים דרך וואטסאפ בכלל"], "chk no")}</div>
</div></section>

<section class="s" id="buy" style="border-top:1px solid var(--line)"><div class="wrap offer">
<div><p class="eyebrow">ההצעה</p><h2>{s['name']}<br><em>במחיר של ארוחה אחת בחוץ</em></h2>
<ul class="chk"><li>{t(s['lessons_count'])} שיעורים מוקלטים, קצרים ומעשיים</li><li>התוכנית ל-30 יום: מה מעלים בכל יום</li><li>{t('[[תבניות ודוגמאות לסטטוסים]]')}</li><li>גישה מיידית ל{t(s['access'])}</li></ul>
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
