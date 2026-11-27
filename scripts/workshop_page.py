from checkout import fields, script, CSS as CO_CSS
from testimonials import grid as tv_grid, CSS as TV_CSS
# The extreme-sales workshop page (recorded live workshop, instant access). Its own layout, same brand.
# Imported by build-sales-pages.py, which passes in t() and footer().
import re

W = {
    "name": "סדנת אקסטרים במכירות",
    "price": "297",
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

from status_page import CSS as ST_CSS

# Same design and section flow as the status page (Itamar asked for it "כמו הסטטוס", 2026-11-26).
CSS = ST_CSS + r"""
.split h1 .nm{display:block;font-size:.62em;color:var(--text);margin-bottom:10px}
.tl{list-style:none;padding:0;margin:18px 0 0;border-inline-start:3px solid #8a6a1c}.tl li{padding:8px 18px;font-size:18px;font-weight:600}.tl b{display:block;font-family:var(--display);font-size:22px;color:#8a6a1c;line-height:1.1}
.qs{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px;margin-top:22px}
.qs figure{margin:0;border:1px solid var(--line);border-top:3px solid var(--gold);border-radius:14px;padding:20px;background:var(--ink2)}
.qs blockquote{margin:0;font-family:var(--display);font-weight:800;font-size:21px;line-height:1.35}
.qs figcaption{margin-top:10px;font-size:13px;font-weight:800;color:var(--gold);letter-spacing:.04em}
.card .was{margin:16px 0 0;color:var(--mute);font-size:14.5px}
@media (max-width:860px){.qs{grid-template-columns:minmax(0,1fr)}}
"""


def workshop_page(t, footer, biz):
    w = W
    li = lambda xs, cls="chk": f'<ul class="{cls}">' + "".join(f"<li>{t(x)}</li>" for x in xs) + "</ul>"
    syll = "".join(f"<li><div><h3>{t(h)}</h3><p>{t(p)}</p></div></li>" for a, h, p in w["agenda"])
    steps = "".join(f"<div><b>{t(a)}</b><p>{t(b)}</p></div>" for a, b in w["steps"])
    vids = tv_grid(["MwQCIENZgNY", "a7MfGVZ2jOo", "V9oCiN17GRw", "HXH6TiDErKE", "IdDaDOZIY0Y", "iUQNNYWroYg"])
    pains = '<ul class="pain">' + "".join(f"<li>{t(x)}</li>" for x in w["pains"]) + "</ul>"
    quotes = "".join(f'<figure><blockquote>"{t(q)}"</blockquote><figcaption>{c} · איתמר שולם</figcaption></figure>' for q, c in w["quotes"])
    stack = "".join(f"<li>{t(a)}: {t(b)}</li>" for a, b in w["stack"])
    faq = "".join(f"<details><summary>{t(q)}</summary><p>{t(a)}</p></details>" for q, a in w["faq"])
    price = t(w['price'])
    return f"""<!DOCTYPE html><html lang="he" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{w['name']}</title><meta name="description" content="סדנת אקסטרים במכירות של איתמר שולם: 3 שעות על סגירת עסקאות, בלי להתחנן ובלי להוריד מחיר. חמשת שלבי המכירה, גישה מיידית.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Heebo:wght@400;700;800;900&family=Rubik:wght@700;800;900&display=swap" rel="stylesheet">
<!-- Meta Pixel / Google tag: להדביק כאן את הקודים מיצחק. בלחיצה על התשלום הדף קורא ל-fbq('track','InitiateCheckout') אם הפיקסל מותקן. -->
<style>{CSS}{CO_CSS}{TV_CSS}</style></head><body>

<header class="split">
<div class="pic"><img src="../hachshara-itamar.webp" alt="{biz['owner']}"><p class="cap"><b>{biz['owner']}</b>מייסד {biz['brand']} · 13 שנים במכירות</p></div>
<div class="txt"><img class="logo" src="../hachshara-logo.webp" alt="{biz['brand']}">
<p class="eyebrow">סדנה מוקלטת · צולמה בלייב באולם</p>
<h1><span class="nm">{w['name']}</span>תפסיק להוריד מחיר.<br><b>תתחיל לסגור.</b></h1>
<p class="lead">3 שעות. 5 שלבים. מהשנייה הראשונה בשיחה ועד שהלקוח אומר כן. בלי להתחנן, בלי הנחות, בלי "אני אחשוב על זה".</p>
<ul class="chips"><li>3 שעות, סדנה מלאה</li><li>5 שלבי מכירה</li><li>גישה מיידית</li><li>{price} ₪, תשלום אחד</li></ul>
<div><a class="btn" href="#buy">אני רוצה לסגור יותר עסקאות &#8592;</a><p class="micro">תשלום מאובטח · קישור הצפייה נשלח מיד אחרי התשלום</p></div>
</div>
</header>

<section class="s light"><div class="wrap narrow story">
<p class="eyebrow" style="color:#8a6a1c">מכיר את זה?</p>
<h2>העסקה לא נפלה במחיר. <em style="color:#8a6a1c">היא נפלה בדקה הראשונה.</em></h2>
{pains}
<p class="big">זו לא בעיה של מוצר. זו לא בעיה של מחיר. זו שיחת מכירה בלי שיטה.</p>
<p>איתמר התחיל למכור בגיל 12, וכל מה שהוא למד מאז נכנס לסדנה אחת:</p>
<ul class="tl"><li><b>גיל 12</b>חנות אופניים בבני ברק. 25 שקל לשעה</li><li><b>גיל 22</b>מנהל פרויקט בנייה עם 100 עובדים</li><li><b>נדל"ן</b>אין תקציב להכשרה? בונה סדנה בעצמו</li><li><b>היום</b>מחלקות מכירה שמוכרות במיליונים</li></ul>
<p class="big">אם אתה יודע למכור, מה יכול לעצור אותך?</p>
<p>הסדנה הועברה באולם יותר מעשר פעמים, מול בעלי עסקים ששילמו 500 ₪ כדי לשבת בחדר. עכשיו היא מצולמת במלואה, בשבע מצלמות, ואתה צופה מהבית.</p>
<div class="phone"><div><b>3</b><span>שעות של סדנה מלאה</span></div><div><b>5</b><span>שלבים, מהפתיחה ועד הסגירה</span></div><div><b>13</b><span>שנים של איתמר במכירות</span></div></div>
</div></section>

<section class="s"><div class="wrap who">
<img src="../hachshara-event.jpg" alt="איתמר שולם על הבמה מול קהל בעלי עסקים">
<div><p class="eyebrow">מי מעביר</p><h2>איתמר <em>שולם</em></h2>
<p style="margin:0;color:#ddd6c6">מלווה בעלי עסקים להכפיל את העסק שלהם. את מה שעובד בשטח הוא מלמד בסדנאות, בהרצאות ובפודקאסט.</p>
<ul><li>מייסד {biz['brand']}</li><li>13 שנים במכירות, מחנות אופניים ועד שיווק נדל"ן</li><li>הכשיר באופן אישי מוקדי מכירות שמכרו במאות מיליונים</li><li>מגיש את הפודקאסט "הכפלה עסקית" ומרצה בפני בעלי עסקים</li></ul>
<p style="margin:14px 0 0;color:var(--gold2);font-weight:700">"מכירה היא לא לקחת מהלקוח. מכירה היא לקחת אותו מאיפה שהוא נמצא לצעד הבא שלו."</p></div>
</div></section>

<section class="s" style="padding-top:0"><div class="wrap">
<p class="eyebrow">מה אומרים</p><h2>בעלי עסקים <em>מספרים</em></h2>
<p class="lede">לקוחות שעבדו עם איתמר בליווי העסקי של הכפלה עסקית.</p>
{vids}
<p class="more">עוד עדויות של בעלי עסקים <a href="https://www.youtube.com/@%D7%90%D7%99%D7%AA%D7%9E%D7%A8%D7%A9%D7%95%D7%9C%D7%9D" target="_blank" rel="noopener">בערוץ היוטיוב של איתמר &#8592;</a></p>
</div></section>

<section class="s light"><div class="wrap">
<p class="eyebrow" style="color:#8a6a1c">מה לומדים</p><h2>5 שלבים. <em style="color:#8a6a1c">שיחת מכירה אחת.</em></h2>
<p class="mute" style="margin:0 0 28px">כל שיחת מכירה עוברת את חמשת השלבים האלה. מי שמדלג על אחד מהם, משלם עליו בסגירה.</p>
<ol class="syll">{syll}</ol>
<div class="cta" style="margin-top:28px"><a class="btn" href="#buy">אני רוצה את הסדנה · {price} ₪ &#8592;</a></div>
</div></section>

<section class="s"><div class="wrap">
<p class="eyebrow">מהסדנה</p><h2>ככה איתמר <em>מדבר באולם</em></h2>
<div class="qs">{quotes}</div>
</div></section>

<section class="s light"><div class="wrap narrow story">
<p class="eyebrow" style="color:#8a6a1c">הגישה</p><h2>מכירה זה <em style="color:#8a6a1c">לא לחץ.</em></h2>
<p>כשאומרים "איש מכירות", רוב האנשים שומעים נודניק. העולם השתנה. מי שמוכר היום הכי טוב הוא מי שהכי מבין את הלקוח: לא משכנע, מבין מה כואב. לא מוריד מחיר, מראה למה זה שווה. לא מחכה שיחזור, מבקש את ההחלטה.</p>
<p class="big">הלקוח סוגר עם מי שמרחיק אותו הכי רחוק מהכאב. לא עם הזול.</p>
</div></section>

<section class="s"><div class="wrap">
<p class="eyebrow">איך זה עובד</p><h2>מהתשלום לשיחה <em>הבאה</em></h2>
<div class="how" style="margin-top:26px">{steps}</div>
</div></section>

<section class="s" style="padding-top:0"><div class="wrap fit">
<div><h2 style="font-size:32px">למי זה <em>מתאים</em></h2>{li(w['for'])}</div>
<div><h2 style="font-size:32px">למי <em>פחות</em></h2>{li(w['not_for'], 'chk no')}</div>
</div></section>

<section class="s" id="buy" style="border-top:1px solid var(--line)"><div class="wrap offer">
<div><p class="eyebrow">ההצעה</p><h2>{w['name']}<br><em>3 שעות שישנו לך את השיחה הבאה</em></h2>
<ul class="chk">{stack}<li>גישה מיידית ל-{t(w['access'])}</li></ul>
<p class="micro" style="font-size:15px">שאלה לפני שקונים? <a href="https://wa.me/{biz['wa']}" style="color:var(--gold2);font-weight:700">כתבו לאיתמר בוואטסאפ</a></p></div>
<div class="card"><p style="margin:0;color:#cfc8b8;font-weight:700">{w['name']} · סדנה מוקלטת</p>
<p class="was">בעלי עסקים שילמו 500 ₪ כדי לשבת באולם</p>
<p class="p">{price} <small>₪</small></p><p class="pn">{t(w['price_note'])}</p>
{fields()}
<p class="micro">אחרי התשלום תקבלו קבלה, ואת קישור הצפייה במייל ובוואטסאפ.</p></div>
</div></section>

<section class="s" style="padding-top:0"><div class="wrap narrow"><p class="eyebrow">שאלות</p><h2>שאלות <em>נפוצות</em></h2>{faq}</div></section>
{footer(1)}
<div class="dock"><b>{w['name']} · {price} ₪</b><a class="btn" href="#buy">לרכישה</a></div>
{script('%%PAY_URL_SALES%%','sales-workshop-checkout',w['name'],(w['price'] if w['price'].isdigit() else ''),biz['wa'])}</body></html>
"""
