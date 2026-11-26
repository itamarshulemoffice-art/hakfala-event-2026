"""Shared checkout step for the paid pages: capture the lead (name, phone, email) into the CRM,
then send the buyer to the payment page. Whoever stops before paying is still a lead to call back.

Funnel: ad -> sales page -> this form -> CRM lead (src=<product>-checkout) -> payment page
-> payment provider returns to <page>/thanks/ -> Purchase pixel + next step.
"""

CRM_ENDPOINT = "https://hakfala-leads.vercel.app/api/lead"

CSS = r"""
.co .fld{margin:0 0 12px}
.co .fld label{display:block;font-size:14px;font-weight:700;color:#cfc8b8;margin:0 0 5px}
.co .fld input{width:100%;font:inherit;font-size:17px;padding:12px 14px;border-radius:10px;border:1px solid #4a463d;background:#0f0f0e;color:#f3efe5;min-height:50px}
.co .fld.bad input{border-color:#ff9a9a}
.co .fld .m{color:#ff9a9a;font-size:13px;min-height:0;margin:4px 0 0}
.co label.c{display:flex;gap:10px;align-items:flex-start;font-size:14px;color:#cfc8b8;margin:0 0 12px}
.co label.c input{width:20px;height:20px;accent-color:#d4af37;flex:none;margin-top:2px}
.co label.c.bad{color:#ff9a9a}
.co .hp{position:absolute;width:1px;height:1px;overflow:hidden;clip-path:inset(50%);white-space:nowrap}
.co button.btn{width:100%;font-family:inherit}
.co button.btn[disabled]{opacity:.7;cursor:wait}
"""


def fields():
    """Form fields + terms + pay button. Drop inside the price card."""
    return """<form class="co" id="co" novalidate>
<div class="fld"><label for="co-name">שם מלא</label><input id="co-name" autocomplete="name" required><p class="m" id="co-name-m"></p></div>
<div class="fld"><label for="co-phone">טלפון נייד</label><input id="co-phone" type="tel" inputmode="tel" autocomplete="tel" dir="ltr" required><p class="m" id="co-phone-m"></p></div>
<div class="fld"><label for="co-email">אימייל (לשם נשלחים הקבלה והגישה)</label><input id="co-email" type="email" autocomplete="email" dir="ltr" required><p class="m" id="co-email-m"></p></div>
<div class="hp" aria-hidden="true"><label>אתר<input id="co-site" tabindex="-1" autocomplete="off"></label></div>
<label class="c" id="co-agree-w"><input type="checkbox" id="co-agree"><span>קראתי ואני מסכים/ה ל<a href="../legal/terms/" target="_blank">תקנון ולמדיניות הביטולים</a></span></label>
<label class="c"><input type="checkbox" id="co-mkt"><span>אשמח לקבל תוכן ועדכונים במייל ובוואטסאפ (לא חובה)</span></label>
<button class="btn" id="co-btn" type="submit">למעבר לתשלום מאובטח &#8592;</button>
<p class="m" id="co-err" role="alert" style="color:#ff9a9a;font-size:14px;margin:8px 0 0"></p>
</form>"""


def script(pay_placeholder, src, product, price, wa):
    """JS: validate, post lead to CRM, fire InitiateCheckout, go to payment (or WhatsApp if no link yet)."""
    return f"""<script>
(function(){{
var P='{pay_placeholder}',K='%%CRM_KEY%%';
var C={{payUrl:P.indexOf('%%')===0?'':P,crmKey:K.indexOf('%%')===0?'':K,crm:'{CRM_ENDPOINT}',src:'{src}',product:'{product}',price:'{price}',wa:'{wa}'}};
function g(i){{return document.getElementById(i)}}
var f=g('co'),btn=g('co-btn');
function v(i){{return (g(i).value||'').trim()}}
function mark(i,msg){{g(i+'-m').textContent=msg;g(i).closest('.fld').classList.toggle('bad',!!msg);g(i).setAttribute('aria-invalid',msg?'true':'false');return !msg}}
function phoneOk(p){{var n=p.replace(/[^\\d]/g,'').replace(/^972/,'0');return /^0\\d{{8,9}}$/.test(n)}}
function emailOk(m){{return /^[^\\s@]+@[^\\s@]+\\.[^\\s@]{{2,}}$/.test(m)}}
var utm={{}};try{{new URLSearchParams(location.search).forEach(function(val,k){{if(/^utm_|^fbclid$/.test(k))utm[k]=val}})}}catch(e){{}}
function toPay(name,phone,email){{
  try{{window.fbq&&fbq('track','InitiateCheckout',{{value:+C.price||undefined,currency:'ILS',content_name:C.product}})}}catch(e){{}}
  try{{sessionStorage.setItem('co',JSON.stringify({{n:name,p:C.product,v:C.price}}))}}catch(e){{}}
  if(C.payUrl){{var o=new URL(C.payUrl,location.href);for(var k in utm)o.searchParams.set(k,utm[k]);location.href=o.toString();return}}
  location.href='https://wa.me/'+C.wa+'?text='+encodeURIComponent('היי, אני רוצה לרכוש: '+C.product+'\\nשם: '+name+'\\nטלפון: '+phone+'\\nאימייל: '+email);
}}
f.addEventListener('submit',function(e){{
  e.preventDefault();g('co-err').textContent='';
  if(v('co-site'))return;
  var name=v('co-name'),phone=v('co-phone'),email=v('co-email');
  var a=mark('co-name',name.length<2?'נשמח לדעת איך קוראים לך':'');
  var b=mark('co-phone',phoneOk(phone)?'':'צריך מספר נייד תקין, לדוגמה 0501234567');
  var c=mark('co-email',emailOk(email)?'':'צריך כתובת אימייל תקינה');
  var ok=g('co-agree').checked;g('co-agree-w').classList.toggle('bad',!ok);
  if(!(a&&b&&c&&ok)){{(!a?g('co-name'):!b?g('co-phone'):!c?g('co-email'):g('co-agree')).focus();if(!ok)g('co-err').textContent='צריך לאשר את התקנון לפני התשלום';return}}
  try{{window.fbq&&fbq('track','Lead',{{content_name:C.product}})}}catch(e){{}}
  if(!C.crmKey){{toPay(name,phone,email);return}}
  btn.disabled=true;btn.textContent='רגע, מעבירים לתשלום...';
  var mkt=g('co-mkt').checked;
  var body=new URLSearchParams({{name:name,phone:phone,email:email,consent:mkt?'1':'0',
    note:['התחיל רכישה: '+C.product+' ('+C.price+' ₪)','מקור: דף מכירה ממומן',mkt?'אישור דיוור: כן':'אישור דיוור: לא'].join(' | ')}});
  for(var k in utm)body.set(k,utm[k]);
  var done=false,go=function(){{if(done)return;done=true;toPay(name,phone,email)}};
  setTimeout(go,2500);
  fetch(C.crm+'?k='+encodeURIComponent(C.crmKey)+'&src='+encodeURIComponent(C.src),{{method:'POST',mode:'no-cors',keepalive:true,headers:{{'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8'}},body:body.toString()}}).then(go,go);
}});
var dk=document.querySelector('.dock'),by=g('buy');if(dk&&by&&window.IntersectionObserver)new IntersectionObserver(function(es){{dk.style.display=es[0].isIntersecting?'none':''}}).observe(by);
['co-name','co-phone','co-email'].forEach(function(i){{g(i).addEventListener('input',function(){{if(g(i).closest('.fld').classList.contains('bad'))mark(i,'')}})}});
}})();
</script>"""


def thanks_page(biz, product, price, next_steps, back):
    """Return page after payment. Set it as the provider's success URL: <page>/thanks/"""
    steps = "".join(f"<li>{s}</li>" for s in next_steps)
    return f"""<!DOCTYPE html><html lang="he" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>תודה, נרשמת · {product}</title><meta name="robots" content="noindex">
<link href="https://fonts.googleapis.com/css2?family=Heebo:wght@400;700;900&display=swap" rel="stylesheet">
<!-- Meta Pixel: אותו קוד כמו בדף המכירה. הדף שולח Purchase פעם אחת בכל רכישה. -->
<style>:root{{color-scheme:dark}}body{{margin:0;background:#0b0b0a;color:#f3efe5;font:18px/1.7 Heebo,Arial,sans-serif}}
main{{max-width:640px;margin:0 auto;padding:56px 18px}}img{{width:120px}}h1{{font-size:clamp(30px,6vw,44px);line-height:1.15;margin:18px 0 8px}}
h1 b{{color:#d4af37}}ol{{padding-inline-start:22px}}li{{margin:0 0 10px}}.btn{{display:inline-flex;background:#25d366;color:#08210f;font-weight:900;border-radius:12px;padding:15px 24px;text-decoration:none;margin-top:10px}}
.m{{color:#a9a395;font-size:14px;margin-top:28px}}a{{color:#f3dc8a}}</style></head><body><main>
<img src="../../hachshara-logo.webp" alt="{biz['brand']}">
<h1>תודה! <b>{product}</b> שלך.</h1>
<p>התשלום התקבל. מה קורה עכשיו:</p><ol>{steps}</ol>
<a class="btn" href="https://wa.me/{biz['wa']}?text={'%D7%94%D7%99%D7%99%2C%20%D7%A0%D7%A8%D7%A9%D7%9E%D7%AA%D7%99'}">כתבו לנו בוואטסאפ &#8592;</a>
<p class="m">לא קיבלתם מייל תוך 10 דקות? בדקו בספאם או כתבו לנו: {biz['phone']}. <a href="{back}">חזרה לדף</a></p>
</main>
<script>try{{var k='paid:'+location.pathname;if(!sessionStorage.getItem(k)){{sessionStorage.setItem(k,'1');window.fbq&&fbq('track','Purchase',{{value:{price or 0},currency:'ILS',content_name:'{product}'}})}}}}catch(e){{}}</script>
</body></html>"""
