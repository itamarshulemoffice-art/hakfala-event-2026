from checkout import fields, script, CSS as CO_CSS
from testimonials import grid as tv_grid, CSS as TV_CSS
# The extreme-sales workshop page (recorded live workshop, instant access). Its own layout, same brand.
# Imported by build-sales-pages.py, which passes in t() and footer().
import re

W = {
    "name": "סדנת אקסטרים במכירות",
    "price": "[[500]]",
    "price_note": "כולל מע\"מ · תשלום אחד · גישה מיידית",
    "length": "3 שעות",
    "access": "[[משך הגישה]]",
    "pains": [
        "\"אני אחשוב על זה\". ומאז שקט",
        "\"יקר לי\". ואתה כבר מוריד מחיר",
        "שלחת הצעת מחיר. וחיכית. ועוד חיכית",
        "מתקשר פעם שנייה ומרגיש נודניק",
        "המוצר שלך טוב יותר. והם סגרו עם המתחרה",
    ],
    "quotes": [
        ("רוב תהליכי המכירה הם שיחות טלפון. ואת חצי הדקה הראשונה אי אפשר לתקן.", "שלב 1"),
        ("איתור צרכים וכאבים. פה נמצא הקסם, פה הכל מתחיל ופה הכל נגמר.", "שלב 2"),
        ("התנגדות היא לא \"לא\". היא בקשה למידע.", "שלב 4"),
        ("הלקוח סוגר עם מי שמרחיק אותו הכי רחוק מהכאב. לא עם הזול.", "שלב 5"),
    ],
    "stack": [
        ("הסדנה המלאה, 3 שעות", "מצולמת באולם בשבע מצלמות"),
        ("חמשת שלבי שיחת המכירה", "מהפתיחה ועד הסגירה"),
        ("ארבעת סגנונות התקשורת", "מקדם, מניע, תומך ומנתח"),
        ("התשובות להתנגדויות הנפוצות", "\"יקר לי\", \"אחשוב על זה\", \"צריך לשאול את אשתי\""),
    ],
    # Itamar's real workshop: recorded live in the hall (7 cameras), hosted on Schooler. 5 stages of a sale.
    "agenda": [
        ("שלב 1", "פתיחה ויצירת כימיה", "חצי הדקה הראשונה, שבה הלקוח מחליט אם אתה מוכר או יועץ. ארבעת סגנונות התקשורת: מקדם, מניע, תומך ומנתח, ואיך מדברים עם כל אחד מהם."),
        ("שלב 2", "איתור צרכים וכאבים", "פה נמצא הקסם. איך שואלים את השאלות שמגיעות לסיבה האמיתית שבגללה הלקוח התקשר, ולמה \"שירות ואמינות\" זו לא תשובה."),
        ("שלב 3", "הצגת המוצר כפתרון", "לא רשימת תכונות. מחברים את מה שאתה מוכר בדיוק לכאב שהלקוח סיפר לך עליו, במילים שלו."),
        ("שלב 4", "טיפול בהתנגדויות", "\"יקר לי\" כמעט אף פעם לא באמת על המחיר. התנגדות היא בקשה למידע, לא \"לא\". מה עונים ל\"אני אחשוב על זה\" ול\"צריך לשאול את אשתי\"."),
        ("שלב 5", "הסגירה", "לקוח סוגר עם מי שהוא הכי סומך עליו, לא עם הזול. איך מבקשים את ההחלטה בלי להתנצל ובלי להישמע לוחץ."),
    ],
    "steps": [
        ("נרשמים ומשלמים", "בעמוד תשלום מאובטח. הקבלה מגיעה למייל."),
        ("מקבלים גישה מיד", "קישור אישי לסדנה במייל ובוואטסאפ, בלי שם משתמש וסיסמה."),
        ("צופים עם דף ועט", "שלוש שעות, מחולקות לפי השלבים. עוצרים, רושמים, חוזרים."),
        ("מיישמים בשיחה הבאה", "מבנה השיחה מוכן להעתקה כבר מחר בבוקר."),
    ],
    "leave_with": [
        "מבנה שיחת מכירה בחמישה שלבים, להעתיק כבר מחר בבוקר",
        "מה עונים ל\"אני אחשוב על זה\" ול\"יקר לי\", בלי לשבור מחיר",
        "איך מזהים תוך דקה את סגנון התקשורת של הלקוח",
        "איך מבקשים את הסגירה בלי להתחנן",
    ],
    "for": ["בעלי עסקים שסוגרים לבד את העסקאות שלהם", "מי שמקבל פניות ושומע הרבה \"אחזור אליך\"", "אנשי מכירות שרוצים שיטה ולא תחושות"],
    "not_for": ["מי שמחפש טריקים ולחץ על לקוחות", "מי שלא מתכוון להרים טלפון אחרי הצפייה"],
    "faq": [
        ("זה בלייב או מוקלט?", "הסדנה צולמה בלייב באולם, מול בעלי עסקים, בשבע מצלמות. אתם צופים בהקלטה המלאה מתי שנוח לכם, מהמחשב או מהטלפון."),
        ("כמה זמן יש לי גישה?", "[[משך הגישה]]"),
        ("אני לא איש מכירות. זה מתאים לי?", "אם אתה סוגר עסקאות בעצמך, אתה איש מכירות. כל מי שמוכר מוצר, שירות או את עצמו, מוכר. הסדנה בנויה בדיוק בשבילך."),
        ("מה ההבדל בין זה לליווי של הכפלה עסקית?", "הסדנה נותנת את שיטת המכירה. בליווי עובדים איתך על העסק כולו, כולל הקלטות של השיחות שלך ותיקון שלהן."),
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
.pain{list-style:none;padding:0;margin:0 0 8px}.pain li{position:relative;padding:12px 32px 12px 0;border-bottom:1px solid rgba(0,0,0,.1);font-size:19px;font-weight:700}.pain li:before{content:"✕";position:absolute;right:0;top:12px;color:#a3201a;font-weight:900}
.qs{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}
.qs figure{margin:0;background:var(--ink2);border:1px solid var(--line);border-right:4px solid var(--hot);border-radius:14px;padding:22px}
.qs blockquote{margin:0;font-family:var(--display);font-weight:800;font-size:clamp(20px,2.2vw,25px);line-height:1.3}
.qs figcaption{margin-top:10px;font-size:13px;color:var(--gold2);font-weight:700}
.stack{list-style:none;margin:0 0 16px;padding:0}.stack li{display:flex;justify-content:space-between;gap:10px;padding:9px 0;border-bottom:1px dashed var(--line);font-size:15px}.stack b{color:var(--text)}.stack span{color:var(--mute);font-size:13.5px;text-align:left}
.was{color:var(--mute);font-size:15px;margin:0}
@media (max-width:860px){.qs{grid-template-columns:minmax(0,1fr)}.stack li{flex-direction:column;gap:0}.stack span{text-align:right}}
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
.punch{font-family:var(--display);font-weight:900;font-size:clamp(28px,4.4vw,46px);line-height:1.1;margin:22px 0 0;color:#fff;text-wrap:balance}.punch em{font-style:normal;color:var(--hot)}
.story .tl{list-style:none;padding:0;margin:18px 0 0;border-inline-start:3px solid #a3201a}.story .tl li{padding:10px 18px;font-size:19px;font-weight:600}.story .tl b{display:block;font-family:var(--display);font-size:24px;color:#a3201a;line-height:1.1}
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
    vids = tv_grid(["MwQCIENZgNY", "a7MfGVZ2jOo", "V9oCiN17GRw", "HXH6TiDErKE", "IdDaDOZIY0Y", "iUQNNYWroYg"])
    pains = '<ul class="pain">' + "".join(f"<li>{t(x)}</li>" for x in w["pains"]) + "</ul>"
    quotes = "".join(f'<figure><blockquote>"{t(q)}"</blockquote><figcaption>{c} · איתמר שולם</figcaption></figure>' for q, c in w["quotes"])
    stack = "".join(f"<li><b>{t(a)}</b><span>{t(b)}</span></li>" for a, b in w["stack"])
    faq = "".join(f"<details><summary>{t(q)}</summary><p>{t(a)}</p></details>" for q, a in w["faq"])
    plain = lambda s: re.sub(r"\[\[(.+?)\]\]", r"\1", s)
    return f"""<!DOCTYPE html><html lang="he" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{w['name']}</title><meta name="description" content="סדנת אקסטרים במכירות של איתמר שולם: 3 שעות על סגירת עסקאות, בלי להתחנן ובלי להוריד מחיר. חמשת שלבי המכירה, גישה מיידית.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Heebo:wght@400;700;800;900&family=Rubik:wght@700;800;900&display=swap" rel="stylesheet">
<!-- Meta Pixel / Google tag: להדביק כאן את הקודים מיצחק. בלחיצה על התשלום הדף קורא ל-fbq('track','InitiateCheckout') אם הפיקסל מותקן. -->
<style>{CSS}{CO_CSS}{TV_CSS}</style></head><body>
<div class="bar"><div class="wrap"><img src="../hachshara-logo.webp" alt="{biz['brand']}"><span class="when">3 שעות · 5 שלבים · גישה מיידית</span><a class="go" href="#buy">לצפייה בסדנה</a></div></div>
<header class="hero xs"><div class="ph"><img src="../hachshara-event.jpg" alt="איתמר שולם מול קהל בעלי עסקים"><span class="tag">איתמר שולם · 13 שנים במכירות</span></div><div class="wrap hx">
<p class="kicker"><i></i>הסדנה שבעלי עסקים שילמו 500 ₪ כדי לשבת בה</p>
<h1 class="name"><span class="o">סדנת</span> <span class="g">אקסטרים</span><br>במכירות</h1>
<p class="punch">תפסיק להוריד מחיר.<br><em>תתחיל לסגור.</em></p>
<p class="sub">3 שעות. 5 שלבים. מהשנייה הראשונה בשיחה ועד שהלקוח אומר כן. בלי להתחנן, בלי הנחות, בלי "אני אחשוב על זה". צולם בלייב באולם, ואתה צופה מהבית.</p>
<div class="ticket"><div><b>3 שעות</b><span>סדנה מלאה</span></div><div><b>5 שלבים</b><span>מפתיחה ועד סגירה</span></div><div><b>מיד</b><span>גישה אחרי התשלום</span></div><div><b>{t(w['price'])} ₪</b><span>מחיר</span></div></div>
<div class="cta"><a class="btn" href="#buy">אני רוצה לסגור יותר עסקאות &#8592;</a><p class="micro">תשלום מאובטח · קישור הצפייה נשלח מיד אחרי התשלום</p></div>
</div></header>

<section class="s story"><div class="wrap" style="max-width:780px">
<p class="kicker"><i></i>מכיר את זה?</p>
<h2>העסקה לא נפלה במחיר. <em>היא נפלה בדקה הראשונה.</em></h2>
{pains}
<p class="big" style="margin-top:26px">סימנת אחד? זו לא בעיה של מוצר. זו לא בעיה של מחיר. <span style="color:#a3201a">זו שיחת מכירה בלי שיטה.</span></p>
<p class="kicker" style="margin-top:44px"><i></i>הסיפור</p>
<h2>מחנות אופניים <em>למחלקות שמוכרות במיליונים</em></h2>
<ul class="tl"><li><b>גיל 12</b>חנות אופניים בבני ברק. 25 שקל לשעה</li><li><b>גיל 22</b>מנהל פרויקט בנייה עם 100 עובדים</li><li><b>נדל"ן</b>אין תקציב להכשרה? בונה סדנה בעצמו</li><li><b>היום</b>מחלקות מכירה שמוכרות במיליונים</li></ul>
<p class="big">אם אתה יודע למכור, מה יכול לעצור אותך?</p>
<p>יותר מעשר פעמים באולם. 500 ₪ לכיסא. <b>עכשיו היא מצולמת במלואה, ואתה צופה מהבית.</b></p>
<div class="cta" style="margin-top:26px"><a class="btn" href="#buy">אני רוצה לסגור יותר &#8592;</a></div>
</div></section>

<section class="s"><div class="wrap">
<h2>מכירה זה <em>לא לחץ</em></h2><p class="lede">כשאומרים "איש מכירות", רוב האנשים שומעים נודניק או שרלטן. העולם השתנה. מי שמוכר היום הכי טוב הוא מי שהכי מבין את הלקוח.</p>
<div class="contrast">
<div><s>משכנעים את הלקוח</s><p>מבינים מה כואב לו</p></div>
<div><s>מורידים מחיר</s><p>מראים למה זה שווה</p></div>
<div><s>מחכים שיחזור</s><p>מבקשים את ההחלטה</p></div>
</div></div></section>

<section class="s"><div class="wrap">
<h2>חמשת <em>השלבים</em></h2><p class="lede">כל שיחת מכירה עוברת את חמשת השלבים האלה. מי שמדלג על אחד מהם, משלם עליו בסגירה.</p>
<ol class="run">{run}</ol>
<div class="cta" style="margin-top:26px"><a class="btn" href="#buy">אני רוצה את הסדנה &#8592;</a></div>
</div></section>

<section class="s"><div class="wrap">
<h2>משפטים <em>מהסדנה</em></h2><p class="lede">ככה איתמר מדבר באולם. ככה תשמעו את זה גם בהקלטה.</p>
<div class="qs">{quotes}</div>
</div></section>

<section class="s"><div class="wrap">
<h2>איך <em>זה עובד</em></h2><p class="lede">מחשב או טלפון, ושלוש שעות שתקבעו לעצמכם ביומן.</p>
<div class="steps">{steps}</div>
</div></section>

<section class="s"><div class="wrap two">
<div><h2>יוצאים <em>עם</em></h2>{li(w['leave_with'])}</div>
<div><h2>למי <em>זה</em></h2>{li(w['for'])}<h2 style="margin-top:28px;font-size:26px">ולמי לא</h2>{li(w['not_for'], 'chk no')}</div>
</div></section>

<section class="s"><div class="wrap who">
<img src="../hachshara-itamar.webp" alt="{biz['owner']}">
<div><p class="kicker"><i></i>מי מעביר</p><h2>איתמר <em>שולם</em></h2>
<ul class="chk"><li>מייסד {biz['brand']}</li><li>13 שנים במכירות, מחנות אופניים ועד שיווק נדל"ן</li><li>הכשיר באופן אישי מוקדי מכירות שמכרו במאות מיליונים</li><li>מלווה בעלי עסקים בשיטת הכפלה עסקית, ומגיש את הפודקאסט "הכפלה עסקית"</li></ul>
<p>"מכירה היא לא לקחת מהלקוח. מכירה היא לקחת אותו מאיפה שהוא נמצא לצעד הבא שלו."</p></div>
</div></section>

<section class="s"><div class="wrap">
<h2>מה אומרים <em>בעלי העסקים</em></h2><p class="lede">לקוחות שעבדו עם איתמר בליווי העסקי של הכפלה עסקית.</p>
{vids}
<p class="more">עוד עדויות <a href="https://www.youtube.com/@%D7%90%D7%99%D7%AA%D7%9E%D7%A8%D7%A9%D7%95%D7%9C%D7%9D" target="_blank" rel="noopener">בערוץ היוטיוב של איתמר &#8592;</a></p>
<div class="cta" style="margin-top:22px"><a class="btn" href="#buy">אני רוצה את הסדנה &#8592;</a></div>
</div></section>

<section class="s" id="buy"><div class="wrap buy">
<div><h2>מתחילים <em>היום</em></h2><p class="lede">הגישה נפתחת מיד אחרי התשלום. מי שצופה בשלושת הימים הראשונים, הוא זה שבאמת משנה משהו בשיחה הבאה.</p>
<p class="seats">● גישה ל-{t(w['access'])}</p>
<p>שאלה לפני שנרשמים? <a href="https://wa.me/{biz['wa']}" style="color:var(--gold2);font-weight:700">כתבו לאיתמר בוואטסאפ</a></p></div>
<div class="card"><p style="margin:0;color:#cfc8b8;font-weight:700">{w['name']} · 3 שעות</p>
<ul class="stack">{stack}</ul>
<p class="was">בעלי עסקים שילמו 500 ₪ כדי לשבת באולם</p>
<p class="p">{t(w['price'])} <small>₪</small></p><p class="pn">{t(w['price_note'])}</p>
{fields()}
<p class="micro">אחרי התשלום תקבלו קבלה, ואת קישור הצפייה במייל ובוואטסאפ.</p></div>
</div></section>

<section class="s"><div class="wrap" style="max-width:820px"><h2>שאלות <em>נפוצות</em></h2>{faq}</div></section>
{footer(1)}
{script('%%PAY_URL_SALES%%','sales-workshop-checkout',w['name'],(w['price'] if w['price'].isdigit() else ''),biz['wa'])}</body></html>
"""
