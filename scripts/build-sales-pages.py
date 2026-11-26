# Builds the paid-course landing pages and the legal pages under public/hachshara/.
# Edit the CONTENT dicts below, then run:  python3 scripts/build-sales-pages.py
# Anything wrapped in [[...]] is a missing detail; it renders as a yellow mark so it can't ship unnoticed.
import re, pathlib, html

ROOT = pathlib.Path(__file__).resolve().parent.parent / "public" / "hachshara"

BIZ = {
    "brand": "הכפלה עסקית",
    "owner": "איתמר שולם",
    "legal_name": "[[שם העסק הרשמי]]",
    "biz_id": "[[מספר עוסק / ח.פ]]",
    "address": "ריש לקיש 4, בית שמש",
    "phone": "053-3315315",
    "wa": "972533315315",
    "email": "[[מייל לשירות לקוחות]]",
    "provider": "[[UPay]]",
}

COURSES = {
    "status": {
        "src": "course-status",
        "title": "הכפלה בסטטוס: קורס הסטטוס בוואטסאפ",
        "tag": "הכפלה בסטטוס · קורס דיגיטלי · 300 ₪",
        "h1": "הסטטוס בוואטסאפ<br>הוא חלון ראווה.<br><b>בואו נגרום לו למכור.</b>",
        "lead": "קורס קצר ומעשי של איתמר שולם: איך הופכים את הסטטוס בוואטסאפ לערוץ מכירה קבוע, שמביא פניות מאנשים שכבר מכירים אתכם. [[משפט ההבטחה המדויק של הקורס]]",
        "price": "300",
        "price_note": "תשלום אחד, כולל מע\"מ",
        "facts": [("[[מספר]] שיעורים", "מוקלטים"), ("[[משך הגישה]]", "גישה לתכנים"), ("300 ₪", "תשלום אחד")],
        "cards_title": "מה לומדים בקורס",
        "cards": [
            ("[[שם שיעור 1]]", "[[מה לומדים בשיעור]]"),
            ("[[שם שיעור 2]]", "[[מה לומדים בשיעור]]"),
            ("[[שם שיעור 3]]", "[[מה לומדים בשיעור]]"),
        ],
        "for": ["בעלי עסקים קטנים שמוכרים בוואטסאפ", "נותני שירות שרוצים יותר פניות בלי עוד פרסום", "[[קהל נוסף]]"],
        "not_for": ["מי שמחפש פתרון בלי לעבוד עליו", "[[למי זה לא מתאים]]"],
        "includes": ["[[מספר]] שיעורים מוקלטים", "[[חומרים נלווים: תבניות / דוגמאות]]", "[[קבוצה / ליווי, אם יש]]", "גישה מיידית אחרי התשלום"],
        "faq": [
            ("איך מקבלים את הקורס?", "מיד אחרי התשלום נשלח אליכם קישור כניסה במייל ובוואטסאפ. [[לאשר את אופן המסירה]]"),
            ("לכמה זמן יש גישה?", "[[משך הגישה]]"),
            ("אפשר לבטל?", "כן, לפי מדיניות הביטולים שבתקנון. הפרטים המלאים בקישור למטה."),
        ],
    },
    "sales": {
        "src": "workshop-extreme-sales",
        "cta": "שמרו לי מקום בסדנה",
        "micro": "תשלום מאובטח · מספר המקומות מוגבל · ביטול לפי התקנון",
        "after": "אחרי התשלום תקבלו קבלה ואת כל פרטי הסדנה במייל ובוואטסאפ.",
        "title": "סדנת אקסטרים במכירות",
        "tag": "סדנת אקסטרים במכירות · [[מחיר]] ₪",
        "h1": "סדנה אחת.<br>לחץ אמיתי.<br><b>יוצאים ממנה סוגרים.</b>",
        "lead": "סדנת אקסטרים במכירות עם איתמר שולם, 13 שנים במכירות. לא עוד הרצאה על מכירות: מתרגלים שיחות אמיתיות, בלחץ אמיתי, עד שזה יושב. [[משפט ההבטחה המדויק של הסדנה]]",
        "price": "[[מחיר]]",
        "price_note": "כולל מע\"מ · [[תשלומים?]]",
        "facts": [("[[תאריך]]", "מועד הסדנה"), ("[[מקום / זום]]", "איפה"), ("[[משך]]", "משך"), ("[[מספר משתתפים]]", "מקומות")],
        "cards_title": "מה קורה בסדנה",
        "cards": [
            ("[[חלק 1]]", "[[מה עושים]]"),
            ("[[חלק 2]]", "[[מה עושים]]"),
            ("[[חלק 3]]", "[[מה עושים]]"),
        ],
        "for": ["בעלי עסקים שסוגרים לבד את העסקאות שלהם", "אנשי מכירות שרוצים שיטה ולא תחושות", "[[קהל נוסף]]"],
        "not_for": ["מי שמחפש הרצאה פסיבית", "[[למי זה לא מתאים]]"],
        "includes": ["[[משך]] של תרגול מעשי עם איתמר", "[[חומרים / תסריטי שיחה]]", "[[ליווי אחרי הסדנה, אם יש]]"],
        "faq": [
            ("מתי ואיפה הסדנה?", "[[תאריך, שעה ומקום / זום]]"),
            ("מה צריך להביא?", "[[מה להביא]]"),
            ("אפשר לבטל?", "כן, לפי מדיניות הביטולים שבתקנון. הפרטים המלאים בקישור למטה."),
        ],
    },
}


def t(s):
    """escape nothing (content is ours) but turn [[x]] into a visible mark"""
    return re.sub(r"\[\[(.+?)\]\]", r'<mark class="todo">\1</mark>', s)


CSS = (pathlib.Path(__file__).with_name("sales-pages.css")).read_text(encoding="utf-8")

HEAD = """<!DOCTYPE html><html lang="he" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Heebo:wght@400;700;800;900&display=swap" rel="stylesheet">
<!-- Meta Pixel / Google tag: להדביק כאן את הקודים מיצחק. בלחיצה על כפתור הקנייה הדף קורא ל-fbq('track','InitiateCheckout') אם הפיקסל מותקן. -->
<style>{css}</style></head><body>"""


def footer(depth):
    up = "../" * depth
    return f"""<footer class="legal"><div class="wrap">
<p><b>{BIZ['brand']}</b> · {t(BIZ['legal_name'])} · {t(BIZ['biz_id'])}</p>
<p>{BIZ['address']} · <a href="tel:+{BIZ['wa']}">{BIZ['phone']}</a> · {t(BIZ['email'])} · <a href="https://wa.me/{BIZ['wa']}">וואטסאפ</a></p>
<p><a href="{up}legal/terms/">תקנון ותנאי רכישה</a> · <a href="{up}legal/terms/#refund">מדיניות ביטולים והחזרים</a> · <a href="{up}legal/privacy/">מדיניות פרטיות</a> · <a href="{up}legal/accessibility/">הצהרת נגישות</a></p>
<p class="pay">התשלום מאובטח ומתבצע אצל {t(BIZ['provider'])}. פרטי האשראי לא עוברים דרכנו ולא נשמרים אצלנו.</p>
</div></footer>"""


def course_page(key, c):
    li = lambda xs: "".join(f"<li>{t(x)}</li>" for x in xs)
    facts = "".join(f"<li>{t(a)}<span>{t(b)}</span></li>" for a, b in c["facts"])
    cards = "".join(f'<div class="card"><b>{i}</b><h3>{t(h)}</h3><p>{t(p)}</p></div>' for i, (h, p) in enumerate(c["cards"], 1))
    faq = "".join(f"<details><summary>{t(q)}</summary><p>{t(a)}</p></details>" for q, a in c["faq"])
    buy = 'class="btn buy" href="#buy"'
    desc = re.sub(r"<[^>]+>|\[\[.+?\]\]", "", c["lead"]).strip()
    return HEAD.format(title=re.sub(r"\[\[(.+?)\]\]", r"\1", c["title"]), desc=html.escape(desc), css=CSS) + f"""
<div class="wrap top"><img src="../hachshara-logo.webp" alt="{BIZ['brand']}"><a {buy.replace('class="btn buy"', 'class="buy"')}>לרכישה</a></div>
<section class="wrap hero">
<div><span class="tag">{t(c['tag'])}</span>
<h1>{t(c['h1'])}</h1>
<p class="lead">{t(c['lead'])}</p>
<ul class="facts">{facts}</ul>
<a {buy}>{c.get('cta','אני רוצה את הקורס')} · {t(c['price'])} ₪ &#8592;</a>
<p class="micro">{c.get('micro','תשלום מאובטח · גישה מיידית · ביטול לפי התקנון')}</p></div>
<div class="photo"><img src="../hachshara-itamar.webp" alt="{BIZ['owner']}"><p><b>{BIZ['owner']}</b>מייסד {BIZ['brand']} · 13 שנים במכירות</p></div>
</section>
<section class="band"><div class="wrap"><h2>{t(c['cards_title'])}</h2><p class="sub">מעשי, קצר, ומוכן ליישום כבר מחר בבוקר.</p>
<div class="cards">{cards}</div></div></section>
<section class="wrap split fit">
<div><h2>למי זה מתאים</h2><ul class="yes">{li(c['for'])}</ul></div>
<div><h2>למי פחות</h2><ul class="no">{li(c['not_for'])}</ul></div>
</section>
<section class="band" id="buy"><div class="wrap split">
<div><h2>מה מקבלים</h2><ul class="yes dark">{li(c['includes'])}</ul>
<div class="me"><img src="../hachshara-itamar.webp" alt=""><div><b>{BIZ['owner']}</b><br><span>שאלה לפני שקונים? <a href="https://wa.me/{BIZ['wa']}">כתבו לי בוואטסאפ</a></span></div></div></div>
<div class="pricebox"><p class="name">{t(c['title'])}</p><p class="price">{t(c['price'])} <small>₪</small></p><p class="pn">{t(c['price_note'])}</p>
<label class="c"><input type="checkbox" id="agree">קראתי ואני מסכים/ה ל<a href="../legal/terms/" target="_blank">תקנון ולמדיניות הביטולים</a></label>
<a class="btn buy" id="pay" href="#">למעבר לתשלום מאובטח &#8592;</a><div class="err" id="err" role="alert"></div>
<p class="micro">{c.get('after','אחרי התשלום תקבלו קבלה וקישור כניסה במייל.')}</p></div>
</div></section>
<section class="wrap faq"><h2>שאלות נפוצות</h2>{faq}</section>
{footer(1)}
<script>
{{
const P='%%PAY_URL_{key.upper()}%%';
const CONFIG={{payUrl:P.indexOf('%%')===0?'':P,wa:'{BIZ['wa']}',course:{repr(re.sub(r"\[\[(.+?)\]\]", r"\1", c['title']))},price:{repr(c['price'] if c['price'].isdigit() else '')}}};
const pay=document.getElementById('pay'),agree=document.getElementById('agree'),err=document.getElementById('err');
pay.addEventListener('click',e=>{{e.preventDefault();err.textContent='';
 if(!agree.checked){{err.textContent='צריך לאשר את התקנון לפני התשלום';agree.focus();return}}
 try{{window.fbq&&fbq('track','InitiateCheckout',{{value:+CONFIG.price||undefined,currency:'ILS',content_name:CONFIG.course}})}}catch(x){{}}
 let u=CONFIG.payUrl;
 if(u){{const q=new URLSearchParams(location.search),o=new URL(u,location.href);q.forEach((v,k)=>{{if(/^utm_/.test(k))o.searchParams.set(k,v)}});location.href=o.toString()}}
 else location.href='https://wa.me/'+CONFIG.wa+'?text='+encodeURIComponent('היי, אני רוצה לרכוש את '+CONFIG.course);
}});
}}
</script></body></html>
"""


def legal_page(title, body):
    return HEAD.format(title=title + " · " + BIZ["brand"], desc=title, css=CSS) + f"""
<div class="wrap top"><img src="../../hachshara-logo.webp" alt="{BIZ['brand']}"><a href="javascript:history.back()">חזרה</a></div>
<main class="wrap doc"><h1>{title}</h1><p class="upd">עודכן לאחרונה: [[תאריך]]</p>{t(body)}</main>
{footer(2)}</body></html>
"""


B = BIZ
TERMS = f"""
<p>ברוכים הבאים לאתר {B['brand']}. האתר והקורסים המוצעים בו מופעלים על ידי {B['legal_name']}, {B['biz_id']}, {B['address']} (להלן: "העסק"). רכישה באתר מהווה הסכמה לתנאים אלה. התקנון כתוב בלשון זכר מטעמי נוחות ומיועד לכל המגדרים.</p>
<h2>1. המוצרים</h2>
<p>העסק מוכר קורסים וסדנאות בתחום העסקים והמכירות, ובהם "הכפלה בסטטוס" ו"סדנת אקסטרים במכירות". תיאור כל קורס, תכולתו ומחירו מופיעים בדף הקורס. המחירים בשקלים וכוללים מע"מ.</p>
<h2>2. הרכישה והתשלום</h2>
<p>התשלום מתבצע בכרטיס אשראי דרך ספק הסליקה {B['provider']}, בעמוד תשלום מאובטח. פרטי האשראי לא נשמרים אצל העסק. אישור רכישה וקבלה יישלחו למייל שהוזן בעת התשלום. רשאי לרכוש מי שמלאו לו 18 ומחזיק בכרטיס אשראי בתוקף שהונפק בישראל או בחו"ל.</p>
<h2>3. אספקת הקורס</h2>
<p>הגישה לקורס נמסרת [[תוך כמה זמן: מיד / תוך 24 שעות]] מהתשלום, באמצעות קישור כניסה שנשלח במייל ובוואטסאפ. משך הגישה לתכנים: [[משך הגישה]]. אם הקישור לא הגיע, פנו אלינו ב-{B['phone']} או ב-{B['email']}.</p>
<h2>4. שימוש בתכנים</h2>
<p>כל התכנים בקורס הם קניין רוחני של העסק. הגישה אישית למשתמש שרכש אותה. אין להעביר, להעתיק, להקליט, להפיץ או למכור את התכנים או את פרטי הגישה לאחר.</p>
<h2 id="refund">5. ביטול עסקה והחזרים</h2>
<p>ביטול עסקה יתאפשר בהתאם לחוק הגנת הצרכן, התשמ"א-1981, ולתקנותיו:</p>
<ul>
<li>אפשר לבטל את העסקה בתוך 14 יום מיום הרכישה, בהודעה בכתב במייל {B['email']} או בוואטסאפ {B['phone']}, עם שם מלא, טלפון ומספר העסקה.</li>
<li>[[לבחור: (א) אם עוד לא נצפה תוכן מהקורס, יוחזר מלוא הסכום בניכוי דמי ביטול של 5% או 100 ₪, הנמוך מביניהם. / (ב) נוסח אחר שאיתמר מעדיף.]]</li>
<li>[[לאשר: מידע שהופק או נמסר באופן דיגיטלי ונצפה כבר, אינו ניתן לביטול לפי סעיף 14ג(ד) לחוק, למעט כשהחוק מחייב אחרת.]]</li>
<li>ההחזר יבוצע לאמצעי התשלום המקורי בתוך 14 יום מקבלת הודעת הביטול, והגישה לקורס תיחסם.</li>
</ul>
<h2>6. אחריות</h2>
<p>הקורסים מעניקים ידע, כלים ושיטות עבודה. התוצאות תלויות ביישום של כל משתתף, והעסק לא מתחייב לתוצאה עסקית או כספית מסוימת.</p>
<h2>7. פרטיות</h2>
<p>הפרטים שנמסרים בעת הרכישה נשמרים לפי <a href="../privacy/">מדיניות הפרטיות</a>.</p>
<h2>8. שינויים ושיפוט</h2>
<p>העסק רשאי לעדכן את התקנון מעת לעת. על רכישה חל התקנון שהיה בתוקף ביום הרכישה. על התקנון חלים דיני מדינת ישראל, וסמכות השיפוט נתונה לבתי המשפט המוסמכים במחוז ירושלים.</p>
<h2>9. יצירת קשר</h2>
<p>{B['legal_name']} · {B['address']} · טלפון ווואטסאפ {B['phone']} · מייל {B['email']}</p>
"""

PRIVACY = f"""
<p>{B['legal_name']} ({B['brand']}) מכבד את פרטיות המשתמשים באתר. מסמך זה מסביר איזה מידע נאסף ומה נעשה בו.</p>
<h2>איזה מידע נאסף</h2>
<ul><li>פרטים שאתם מוסרים: שם, טלפון ומייל, בטפסים ובעת רכישה.</li>
<li>פרטי התשלום נמסרים ישירות לספק הסליקה {B['provider']}, ולא נשמרים אצלנו.</li>
<li>מידע טכני על הגלישה, באמצעות עוגיות וכלי מדידה כמו פיקסל של מטא ו-Google Analytics, כדי למדוד את הפרסום ולשפר אותו.</li></ul>
<h2>למה משתמשים במידע</h2>
<ul><li>כדי לספק את הקורס שרכשתם, לשלוח קבלה וקישורי גישה, ולתת שירות.</li>
<li>כדי לשלוח עדכונים, תוכן והצעות, רק אם אישרתם זאת. אפשר להסיר את עצמכם בכל רגע דרך הקישור שבכל הודעה או בפנייה אלינו.</li>
<li>כדי לנתח את השימוש באתר ואת ביצועי הפרסום.</li></ul>
<h2>עם מי משתפים</h2>
<p>עם ספקים שעוזרים לנו לתת את השירות: ספק הסליקה, מערכת ניהול הלקוחות, מערכת הדיוור (רב מסר), ופלטפורמות הפרסום. לא נמכור את המידע שלכם לאף אחד.</p>
<h2>הזכויות שלכם</h2>
<p>אפשר לבקש לעיין במידע שנשמר עליכם, לתקן אותו או למחוק אותו, בפנייה ל-{B['email']} או ב-{B['phone']}.</p>
<h2>אבטחה</h2>
<p>האתר מוגש בחיבור מאובטח (HTTPS), והתשלום מתבצע בעמוד הסליקה המאובטח של {B['provider']}.</p>
"""

ACCESS = f"""
<p>{B['brand']} רואה חשיבות בהנגשת האתר לאנשים עם מוגבלות. האתר נבנה כך שיהיה קריא בהגדלת טקסט, ניתן לניווט במקלדת, כולל טקסט חלופי לתמונות, בניגודיות צבעים גבוהה ובכיוון עברית תקין.</p>
<p>אם נתקלתם בבעיית נגישות, נשמח שתספרו לנו ונטפל בה: רכז/ת הנגישות: [[שם]] · טלפון {B['phone']} · מייל {B['email']}.</p>
"""

def write(rel, s):
    p = ROOT / rel / "index.html"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(s, encoding="utf-8")
    print("wrote", p.relative_to(ROOT.parent.parent), "todo marks:", s.count('class="todo"'))

import sys; sys.path.insert(0, str(pathlib.Path(__file__).parent))
from workshop_page import workshop_page
from status_page import status_page
from checkout import thanks_page
write("status", status_page(t, footer, BIZ))
write("sales", workshop_page(t, footer, BIZ))
write("status/thanks", thanks_page(BIZ, "הכפלה בסטטוס", 300, [
    "תוך כמה דקות יגיעו אליך במייל הקבלה וקישור הכניסה לקורס.",
    "שלחנו לך הודעה בוואטסאפ עם הקישור ועם הדרך הכי טובה להתחיל.",
    "מתחילים מהשיעור הראשון: אסטרטגיה לפני הכל.",
], "../"))
write("sales/thanks", thanks_page(BIZ, "סדנת אקסטרים במכירות", 0, [
    "תוך כמה דקות יגיעו אליך במייל הקבלה ופרטי הסדנה.",
    "קישור הזום יישלח במייל ובוואטסאפ, וגם תזכורת יום לפני ושעה לפני.",
    "מגיעים עם מצלמה פתוחה ועם עסקה אמיתית שתרצו לעבוד עליה.",
], "../"))
write("legal/terms", legal_page("תקנון ותנאי רכישה", TERMS))
write("legal/privacy", legal_page("מדיניות פרטיות", PRIVACY))
write("legal/accessibility", legal_page("הצהרת נגישות", ACCESS))
