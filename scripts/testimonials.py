"""Video testimonials from Itamar's YouTube channel (clients of הכפלה עסקית consulting).
Thumbnail + click-to-play: the YouTube player loads only after a click, so the page stays light."""

ALL = {
    "iUQNNYWroYg": "יעקב רובין",
    "YlC4c-9N164": "זלמן הולצברג",
    "eKyT13RRXqg": "אביגדור קבילי",
    "ML49iCHtz00": "יצחק וחנון",
    "FJMLzrPt_VA": "שמעון שמש",
    "e8v3e2sjWwI": "ורד נפרין",
    "MwQCIENZgNY": "דרור בש",
    "a7MfGVZ2jOo": "יחיאל זלוטניק",
    "V9oCiN17GRw": "ישראל ברלין",
    "HXH6TiDErKE": "חנה שרה הרטמן",
    "IdDaDOZIY0Y": "רפאל לייטנר וישראל סיימון",
}

CSS = """
.tv{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;margin-top:18px}
.tv button{all:unset;cursor:pointer;display:block;border-radius:14px;overflow:hidden;background:#151512;border:1px solid rgba(255,255,255,.1)}
.tv button:focus-visible{outline:3px solid #d4af37;outline-offset:2px}
.tv .f{position:relative;aspect-ratio:16/9;background:#111 center/cover no-repeat;display:grid;place-items:center}
.tv .f iframe{position:absolute;inset:0;width:100%;height:100%;border:0}
.tv .p{width:58px;height:58px;border-radius:50%;background:#d4af37;display:grid;place-items:center;box-shadow:0 6px 20px rgba(0,0,0,.45)}
.tv .p:after{content:"";border-style:solid;border-width:11px 0 11px 18px;border-color:transparent transparent transparent #111;margin-left:5px}
.tv .n{display:block;padding:12px 14px;font-weight:700;color:#f3efe5;font-size:16px}
.tv .n small{display:block;font-weight:400;color:#a9a395;font-size:13px}
@media (max-width:860px){.tv{grid-template-columns:minmax(0,1fr) minmax(0,1fr)}}
@media (max-width:520px){.tv{gap:10px}.tv .p{width:44px;height:44px}.tv .n{padding:8px 10px;font-size:14px}}
"""


def grid(ids):
    cards = "".join(
        f'<button type="button" data-v="{v}" aria-label="לצפייה בעדות של {ALL[v]}">'
        f'<span class="f" style="background-image:url(https://i.ytimg.com/vi/{v}/hqdefault.jpg)"><span class="p" aria-hidden="true"></span></span>'
        f'<span class="n">{ALL[v]}<small>לקוח/ה של הכפלה עסקית</small></span></button>'
        for v in ids)
    return f"""<div class="tv">{cards}</div>
<script>document.querySelectorAll('.tv button').forEach(function(b){{b.addEventListener('click',function(){{var f=b.querySelector('.f');if(f.querySelector('iframe'))return;f.innerHTML='<iframe src="https://www.youtube-nocookie.com/embed/'+b.dataset.v+'?autoplay=1&rel=0" allow="autoplay; encrypted-media; picture-in-picture" allowfullscreen title="עדות"></iframe>'}})}})</script>"""
