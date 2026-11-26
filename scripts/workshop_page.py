from checkout import fields, script, CSS as CO_CSS
# The extreme-sales workshop page (live on Zoom). Its own layout, same brand.
# Imported by build-sales-pages.py, which passes in t() and footer().
import re

W = {
    "name": "סדנת אקסטרים במכירות",
    "price": "[[מחיר]]",
    "price_note": "כולל מע\"מ · [[תשלומים?]]",
    "date": "[[יום ותאריך]]",
    "time": "[[שעה]]",
    "length": "[[משך]] שעות",
    "seats": "[[מספר מקומות]]",
    "promise": "[[משפט ההבטחה המדויק של הסדנה]]",
    # Proposed run of the day. Times and topics are a draft for Itamar to confirm.
    "agenda": [
        ("[[שעה]]", "פתיחה: איפה העסקאות שלך נופלות", "כל משתתף מביא עסקה אמיתית שנתקעה. מאבחנים ביחד באיזה שלב היא נפלה."),
        ("[[שעה]]", "סבב 1: פתיחת שיחה", "הדקות הראשונות שקובעות אם מקשיבים לך. מתרגלים בזוגות בחדרים בזום, ואיתמר עובר בין החדרים."),
        ("[[שעה]]", "סבב 2: \"יקר לי\" ו\"אחשוב על זה\"", "ההתנגדויות שעוצרות הכי הרבה עסקאות. כל אחד עונה עליהן בקול, מול כולם, עד שזה יושב."),
        ("[[שעה]]", "סבב 3: הסגירה", "איך מבקשים את ההחלטה בלי להתנצל ובלי ללחוץ. סגירות חיות על עסקאות של משתתפים."),
        ("[[שעה]]", "סיכום: התוכנית לשבוע הבא", "כל משתתף יוצא עם 3 שיחות שהוא מתקשר אליהן השבוע, ועם התסריט שבנה בסדנה."),
    ],
    "steps": [
        ("נרשמים ומשלמים", "בעמוד תשלום מאובטח. הקבלה מגיעה למייל."),
        ("מקבלים את קישור הזום", "במייל ובוואטסאפ, [[כמה זמן]] לפני הסדנה."),
        ("מגיעים עם עסקה אמיתית", "לקוח שנתקע, הצעה שלא נסגרה. עליה עובדים."),
        ("יוצאים עם תסריט", "שלך, בשפה שלך, מוכן לשיחה של מחר בבוקר."),
    ],
    "leave_with": [
        "תסריט שיחה אישי לעסק שלך",
        "תשובות מוכנות ל-[[מספר]] ההתנגדויות הנפוצות",
        "רשימת 3 שיחות לשבוע הקרוב",
        "[[הקלטה / חומרים, אם יש]]",
    ],
    "for": ["בעלי עסקים שסוגרים לבד את העסקאות שלהם", "אנשי מכירות שרוצים שיטה ולא תחושות", "מי שמוכן לדבר בקול מול אחרים, גם אם זה לא נוח"],
    "not_for": ["מי שמחפש הרצאה להאזין לה ברקע", "מי שלא מוכן לפתוח מצלמה"],
    "faq": [
        ("חייבים לפתוח מצלמה?", "כן. זו סדנה של תרגול, לא הרצאה. בלי מצלמה ובלי מיקרופון אי אפשר לתרגל."),
        ("תהיה הקלטה?", "[[כן / לא]]"),
        ("מה אם אני לא מצליח להגיע?", "[[מה קורה: מועד חלופי / הקלטה / החזר לפי התקנון]]"),
        ("אני לא איש מכירות. זה מתאים לי?", "אם אתה סוגר עסקאות בעצמך, אתה איש מכירות. הסדנה בנויה בדיוק בשבילך."),
        ("אפשר לבטל?", "כן, לפי מדיניות הביטולים שבתקנון. הקישור בתחתית הדף."),
    ],
}

CSS = r"""

.hero.xs{padding:0}
.xs{display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr);padding:0;min-height:min(88vh,720px)}
.xs .ph{position:relative;background:#1a1a18}
.xs .ph img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.xs .ph:after{content:"";position:absolute;inset:0;background:linear-gradient(270deg,rgba(10,10,10,0) 50%,var(--ink) 100%)}
.xs .tag{position:absolute;bottom:16px;right:16px;z-index:1;background:rgba(10,10,10,.75);border:1px solid var(--line);border-radius:999px;padding:6px 14px;font-size:14px;font-weight:700}
.xs .hx{display:flex;flex-direction:column;justify-content:center;padding-block:48px;max-width:none;margin:0}
.xs .name{font-size:clamp(46px,6.4vw,96px)!important}
.story{background:#f7f3ea;color:#171614}.story h2 em{color:#a3201a}.story .kicker{color:#a3201a}
.story p{font-size:19px;margin:0 0 16px}.story .big{font-family:var(--display);font-weight:800;font-size:clamp(24px,3vw,32px);line-height:1.25;color:#8a6a1c;margin:26px 0}
.vids{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;margin-top:18px}
.vid{border-radius:16px;overflow:hidden;background:var(--ink2);border:1px solid var(--line)}
.vid .frame{position:relative;aspect-ratio:9/12;background:radial-gradient(circle at 50% 40%,#2a2720,#121210);display:grid;place-items:center}
.vid .play{width:60px;height:60px;border-radius:50%;background:var(--hot);display:grid;place-items:center}
.vid .play:after{content:"";border-style:solid;border-width:11px 0 11px 18px;border-color:transparent transparent transparent #fff;margin-left:5px}
.vid .frame small{position:absolute;bottom:12px;left:0;right:0;text-align:center;font-size:13px;color:var(--mute)}
.vid .q{padding:16px}.vid .q p{margin:0 0 8px;font-weight:700}.vid .q span{font-size:14px;color:var(--mute)}
.more{margin-top:14px;color:var(--mute)}.more a{color:var(--gold2);font-weight:700}
@media (max-width:860px){.xs{grid-template-columns:minmax(0,1fr);min-height:0}.xs .ph{aspect-ratio:4/3.4}.xs .ph:after{background:linear-gradient(180deg,rgba(10,10,10,0) 55%,var(--ink) 100%)}.xs .hx{padding-block:6px 40px}.vids{grid-template-columns:minmax(0,1fr) minmax(0,1fr)}.vids .vid:nth-child(3){display:none}}
/* LAYOUT: a ring-side poster. Huge outlined name, a ticket strip, then a vertical run-of-show. */
:root{color-scheme:dark;--ink:#0a0a0a;--ink2:#141413;--line:#2c2b27;--gold:#d4af37;--gold2:#f3dc8a;--text:#f2eee4;--mute:#a7a194;--hot:#ff5a36;
--display:"Rubik","Heebo",Arial,sans-serif;--body:"Heebo",Arial,sans-serif}
*{box-sizing:border-box;min-width:0}
body{margin:0;background:var(--ink);color:var(--text);font:17px/1.65 var(--body);overflow-x:clip}
a{color:inherit}
.wrap{max-width:1120px;margin:0 auto;padding-left:max(18px,env(safe-area-inset-left,0px));padding-right:max(18px,env(safe-area-inset-right,0px))}
.bar{position:sticky;top:0;z-index:5;background:rgba(10,10,10,.92);backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}
.bar .wrap{display:flex;align-items:center;gap:14px;padding-block:10px}
.bar img{height:38px}.bar .when{margin-inline-start:auto;font-size:14px;color:var(--mute)}
.bar .go{background:var(--gold);color:#111;font-weight:800;text-decoration:none;border-radius:999px;padding:8px 16px;font-size:15px;white-space:nowrap}
.hero{position:relative;padding-block:56px 40px;overflow:hidden}
.hero:before{content:"";position:absolute;inset:0;background:repeating-linear-gradient(-55deg,transparent 0 22px,rgba(212,175,55,.05) 22px 24px);pointer-events:none}
.kicker{display:inline-flex;gap:8px;align-items:center;font-weight:800;font-size:14px;letter-spacing:.04em;color:var(--hot);margin:0 0 14px}
.kicker i{width:9px;height:9px;border-radius:50%;background:var(--hot);box-shadow:0 0 0 4px rgba(255,90,54,.2)}
.name{font-family:var(--display);font-weight:900;line-height:.92;margin:0;font-size:clamp(52px,11vw,132px);letter-spacing:-.02em;text-wrap:balance}
.name .o{color:transparent;-webkit-text-stroke:2px var(--gold)}
.name .g{color:var(--gold)}
.sub{font-size:clamp(19px,2.2vw,24px);max-width:36em;margin:22px 0 0;color:#e2dccd}
.ticket{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));margin:34px 0 0;border:1px solid var(--line);border-radius:14px;overflow:hidden;background:var(--ink2)}
.ticket div{padding:14px 16px;border-inline-start:1px dashed var(--line)}
.ticket div:first-child{border:0}
.ticket b{display:block;font-family:var(--display);font-size:20px}
.ticket span{font-size:12.5px;color:var(--mute);letter-spacing:.03em}
.cta{display:flex;flex-wrap:wrap;gap:14px;align-items:center;margin-top:26px}
.btn{display:inline-flex;align-items:center;justify-content:center;background:var(--gold);color:#111;font-weight:900;font-size:19px;border:0;border-radius:12px;padding:16px 28px;min-height:56px;text-decoration:none;cursor:pointer}
.btn:hover{background:var(--gold2)}
.btn:focus-visible,input:focus-visible,summary:focus-visible{outline:3px solid #fff;outline-offset:2px}
.micro{font-size:13.5px;color:var(--mute);margin:0}
section.s{padding-block:64px;border-top:1px solid var(--line)}
h2{font-family:var(--display);font-weight:900;font-size:clamp(30px,4.4vw,48px);line-height:1.05;margin:0 0 10px;text-wrap:balance}
h2 em{font-style:normal;color:var(--gold)}
.lede{color:var(--mute);margin:0 0 30px;max-width:38em}
.contrast{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:2px;background:var(--line);border-radius:14px;overflow:hidden}
.contrast div{background:var(--ink2);padding:22px}
.contrast s{display:block;color:var(--mute);text-decoration-color:var(--hot);text-decoration-thickness:2px;font-size:16px}
.contrast p{margin:6px 0 0;font-family:var(--display);font-weight:800;font-size:22px;line-height:1.2}
.run{list-style:none;margin:0;padding:0;position:relative}
.run:before{content:"";position:absolute;top:8px;bottom:8px;right:84px;width:2px;background:linear-gradient(var(--gold),var(--hot))}
.run li{display:grid;grid-template-columns:70px 30px minmax(0,1fr);gap:0 14px;padding:0 0 26px}
.run .tm{font-variant-numeric:tabular-nums;color:var(--gold2);font-weight:700;padding-top:2px;text-align:left}
.run .dot{width:16px;height:16px;border-radius:50%;background:var(--ink);border:3px solid var(--gold);margin:6px auto 0;position:relative;z-index:1}
.run h3{margin:0;font-family:var(--display);font-size:22px;line-height:1.25}
.run p{margin:4px 0 0;color:#cfc8b8;max-width:40em}
.steps{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:14px;counter-reset:st}
.steps div{border:1px solid var(--line);border-radius:14px;padding:18px;counter-increment:st;background:var(--ink2)}
.steps div:before{content:counter(st);display:grid;place-items:center;width:34px;height:34px;border-radius:50%;background:var(--gold);color:#111;font-weight:900;margin-bottom:10px}
.steps b{display:block;font-size:18px}.steps p{margin:4px 0 0;font-size:15px;color:var(--mute)}
.two{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:40px}
ul.chk{list-style:none;margin:0;padding:0}
ul.chk li{padding:10px 32px 10px 0;border-bottom:1px solid var(--line);position:relative}
ul.chk li:before{content:"✓";position:absolute;right:4px;top:10px;color:var(--gold);font-weight:900}
ul.chk.no li:before{content:"✕";color:var(--hot)}
.who{display:grid;grid-template-columns:220px minmax(0,1fr);gap:32px;align-items:center}
.who img{width:100%;aspect-ratio:1;object-fit:cover;object-position:top;border-radius:50%;border:4px solid var(--gold)}
.who p{margin:0 0 10px;font-size:18px}
.buy{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);gap:36px;align-items:start}
.card{border:2px solid var(--gold);border-radius:18px;padding:28px;background:var(--ink2)}
.card .p{font-family:var(--display);font-size:64px;font-weight:900;line-height:1;color:var(--gold2);margin:6px 0}
.card .p small{font-size:26px}
.card .pn{color:var(--mute);font-size:14px;margin:0 0 18px}
.card .btn{width:100%}
.card a:not(.btn){color:var(--gold2)}
label.c{display:flex;gap:10px;align-items:flex-start;font-size:14px;color:#cfc8b8;margin:0 0 14px}
label.c input{width:20px;height:20px;accent-color:var(--gold);flex:none;margin-top:2px}
.err{color:#ff9a9a;font-size:14px;min-height:20px;margin-top:8px}
.seats{display:flex;gap:10px;align-items:center;font-weight:700;color:var(--hot);margin:0 0 6px}
details{border:1px solid var(--line);border-radius:12px;padding:14px 18px;margin:0 0 10px;background:var(--ink2)}
summary{cursor:pointer;font-weight:800;font-size:18px}
details p{margin:10px 0 0;color:#d8d2c4}
mark.todo{background:#ffe066;color:#111;border-radius:4px;padding:0 4px;font-weight:700;-webkit-text-stroke:0}
footer.legal{border-top:1px solid var(--line);padding-block:28px 40px;color:#8d887c;font-size:13.5px}
footer.legal p{margin:0 0 6px}footer.legal a{color:#cfc9bb}footer.legal .pay{font-size:12.5px;color:#7d786d}
@media(max-width:860px){.ticket{grid-template-columns:repeat(2,minmax(0,1fr))}.ticket div:nth-child(3){border:0}.ticket div:nth-child(n+3){border-top:1px dashed var(--line)}
.contrast,.steps,.two,.buy{grid-template-columns:minmax(0,1fr)}.who{grid-template-columns:minmax(0,1fr)}.who img{width:160px}
.run:before{right:64px}.run li{grid-template-columns:52px 26px minmax(0,1fr);gap:0 10px}.bar .when{display:none}}
@media(prefers-reduced-motion:no-preference){.kicker i{animation:pulse 1.6s infinite}@keyframes pulse{50%{box-shadow:0 0 0 8px rgba(255,90,54,0)}}}
"""


def workshop_page(t, footer, biz):
    w = W
    li = lambda xs, cls="chk": f'<ul class="{cls}">' + "".join(f"<li>{t(x)}</li>" for x in xs) + "</ul>"
    run = "".join(f'<li><span class="tm">{t(a)}</span><span class="dot"></span><div><h3>{t(h)}</h3><p>{t(p)}</p></div></li>' for a, h, p in w["agenda"])
    steps = "".join(f"<div><b>{t(a)}</b><p>{t(b)}</p></div>" for a, b in w["steps"])
    vids = "".join(f'<div class="vid"><div class="frame"><span class="play" aria-hidden="true"></span><small>{t("[[סרטון עדות]]")}</small></div><div class="q"><p>"{t("[[משפט אחד מהעדות]]")}"</p><span>{t("[[שם]]")} · {t("[[סוג העסק]]")}</span></div></div>' for _ in range(3))
    faq = "".join(f"<details><summary>{t(q)}</summary><p>{t(a)}</p></details>" for q, a in w["faq"])
    plain = lambda s: re.sub(r"\[\[(.+?)\]\]", r"\1", s)
    return f"""<!DOCTYPE html><html lang="he" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{w['name']}</title><meta name="description" content="סדנה חיה בזום עם איתמר שולם: מתרגלים שיחות מכירה אמיתיות, התנגדויות וסגירה, ויוצאים עם תסריט אישי.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Heebo:wght@400;700;800;900&family=Rubik:wght@700;800;900&display=swap" rel="stylesheet">
<!-- Meta Pixel / Google tag: להדביק כאן את הקודים מיצחק. בלחיצה על התשלום הדף קורא ל-fbq('track','InitiateCheckout') אם הפיקסל מותקן. -->
<style>{CSS}{CO_CSS}</style></head><body>
<div class="bar"><div class="wrap"><img src="../hachshara-logo.webp" alt="{biz['brand']}"><span class="when">{t(w['date'])} · {t(w['time'])} · בזום</span><a class="go" href="#buy">שמרו לי מקום</a></div></div>
<header class="hero xs"><div class="ph"><img src="../hachshara-event.jpg" alt="איתמר שולם מול קהל בעלי עסקים"><span class="tag">איתמר שולם · 13 שנים במכירות</span></div><div class="wrap hx">
<p class="kicker"><i></i>סדנה חיה בזום · מספר המקומות מוגבל</p>
<h1 class="name"><span class="o">סדנת</span> <span class="g">אקסטרים</span><br>במכירות</h1>
<p class="sub">{t(w['length'])} בזום עם איתמר שולם. בלי שקפים ובלי הרצאות: שיחות מכירה אמיתיות, התנגדויות אמיתיות, וסגירות בלייב, עד שזה יושב לך בגוף. {t(w['promise'])}</p>
<div class="ticket"><div><b>{t(w['date'])}</b><span>מתי</span></div><div><b>{t(w['time'])}</b><span>שעה</span></div><div><b>בזום</b><span>מכל מקום, מצלמה פתוחה</span></div><div><b>{t(w['price'])} ₪</b><span>מחיר</span></div></div>
<div class="cta"><a class="btn" href="#buy">שמרו לי מקום בסדנה &#8592;</a><p class="micro">תשלום מאובטח · קישור הזום נשלח אחרי ההרשמה</p></div>
</div></header>

<section class="s story"><div class="wrap" style="max-width:780px">
<p class="kicker"><i></i>הסיפור</p>
<h2>הלקוח אמר "אני אחשוב על זה". <em>ואתה הסכמת.</em></h2>
<p>זה קרה לכל בעל עסק. שיחה טובה, הלקוח מתעניין, המחיר עולה על השולחן, ואז השקט. "אני אחזור אליך". הוא לא חוזר.</p>
<p>לא חסר לך ידע. קראת, שמעת פודקאסטים, אולי אפילו עשית קורס. אבל ברגע האמת, מול לקוח אמיתי, הגוף קופא והמילים נעלמות.</p>
<p class="big">מכירה זה לא משהו שיודעים. זה משהו שעושים, עד שזה יושב בגוף.</p>
<p>{t('[[הסיפור של איתמר: רגע אמיתי שבו הבין שתרגול מנצח ידע, ומה ראה אצל בעלי העסקים שליווה. 3-4 משפטים בשפה שלו]]')}</p>
<p>בשביל זה בנינו את הסדנה הזו: כמה שעות של תרגול חי, בלי שקפים, על עסקאות אמיתיות שלך.</p>
<div class="cta" style="margin-top:26px"><a class="btn" href="#buy">אני רוצה לתרגל את זה &#8592;</a></div>
</div></section>

<section class="s"><div class="wrap">
<h2>למה <em>אקסטרים</em></h2><p class="lede">כי לשמוע על מכירות זה קל. לעשות את זה בקול, מול אנשים, כשמישהו אומר לך "יקר לי", זה מה שמשנה את החודש הבא שלך.</p>
<div class="contrast">
<div><s>שומעים על התנגדויות</s><p>עונים עליהן בקול, מול כולם</p></div>
<div><s>רושמים טיפים</s><p>בונים תסריט לעסקה שלך</p></div>
<div><s>מחכים לרגע הנכון</s><p>סוגרים בלייב, בסדנה</p></div>
</div></div></section>

<section class="s"><div class="wrap">
<h2>מה קורה <em>בסדנה</em></h2><p class="lede">חמישה סבבים. כל סבב: הסבר קצר, תרגול בזוגות בחדרים בזום, ותיקון מול כולם.</p>
<ol class="run">{run}</ol>
<div class="cta" style="margin-top:26px"><a class="btn" href="#buy">אני בפנים &#8592;</a><p class="micro">{t(w['seats'])} מקומות בלבד</p></div>
</div></section>

<section class="s"><div class="wrap">
<h2>איך זה עובד <em>בזום</em></h2><p class="lede">אין צורך בשום דבר מלבד מחשב או טלפון עם מצלמה ומיקרופון.</p>
<div class="steps">{steps}</div>
</div></section>

<section class="s"><div class="wrap two">
<div><h2>יוצאים <em>עם</em></h2>{li(w['leave_with'])}</div>
<div><h2>למי <em>זה</em></h2>{li(w['for'])}<h2 style="margin-top:28px;font-size:26px">ולמי לא</h2>{li(w['not_for'], 'chk no')}</div>
</div></section>

<section class="s"><div class="wrap who">
<img src="../hachshara-itamar.webp" alt="{biz['owner']}">
<div><p class="kicker"><i></i>מי מעביר</p><h2>איתמר <em>שולם</em></h2>
<ul class="chk"><li>מייסד {biz['brand']}</li><li>13 שנים במכירות, בשטח ולא מהצד</li><li>ליווה למעלה מ-100 בעלי עסקים בשנה האחרונה</li><li>מגיש הפודקאסט "הכפלה עסקית", מרצה ומוביל צוות מנטורים</li></ul>
<p>{t('[[משפט אחד של איתמר: למה הוא מעביר את הסדנה הזו]]')}</p></div>
</div></section>

<section class="s"><div class="wrap">
<h2>מה אומרים <em>בעלי העסקים</em></h2><p class="lede">{t('[[לבחור 3 סרטוני עדות מהערוץ, עדיף על מכירות וסגירות]]')}</p>
<div class="vids">{vids}</div>
<p class="more">עוד עדויות <a href="https://www.youtube.com/@%D7%90%D7%99%D7%AA%D7%9E%D7%A8%D7%A9%D7%95%D7%9C%D7%9D" target="_blank" rel="noopener">בערוץ היוטיוב של איתמר &#8592;</a></p>
<div class="cta" style="margin-top:22px"><a class="btn" href="#buy">שמרו לי מקום בסדנה &#8592;</a></div>
</div></section>

<section class="s" id="buy"><div class="wrap buy">
<div><h2>שמרו לי <em>מקום</em></h2><p class="lede">המקומות מוגבלים כדי שכל אחד יתרגל ולא רק יצפה.</p>
<p class="seats">● {t(w['seats'])} מקומות בסדנה</p>
<p>שאלה לפני שנרשמים? <a href="https://wa.me/{biz['wa']}" style="color:var(--gold2);font-weight:700">כתבו לאיתמר בוואטסאפ</a></p></div>
<div class="card"><p style="margin:0;color:#cfc8b8;font-weight:700">{w['name']} · {t(w['date'])}</p>
<p class="p">{t(w['price'])} <small>₪</small></p><p class="pn">{t(w['price_note'])}</p>
{fields()}
<p class="micro">אחרי התשלום תקבלו קבלה, ואת קישור הזום במייל ובוואטסאפ.</p></div>
</div></section>

<section class="s"><div class="wrap" style="max-width:820px"><h2>שאלות <em>נפוצות</em></h2>{faq}</div></section>
{footer(1)}
{script('%%PAY_URL_SALES%%','sales-workshop-checkout',w['name'],(w['price'] if w['price'].isdigit() else ''),biz['wa'])}</body></html>
"""
