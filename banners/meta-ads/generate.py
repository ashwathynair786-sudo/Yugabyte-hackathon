"""Generate ContextCon Meta ad HTML files: one set per hook, four sizes each.

Run from the repo root:  python3 banners/meta-ads/generate.py
Then render PNGs with:    node banners/meta-ads/render.js
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
BANNERS = os.path.dirname(HERE)

# Each set: id, highlighted lead (lime), rest of the hook (white), style.
#   style "robot": robot image + Claim your spot button
#   style "swirl": brand fluid texture, ContextCon logo on top, no button
#   style "photo": builder cutout image bottom-right, ContextCon logo on top, no button
SETS = [
    ("set1", "$10,000", "prize money for a project you would build anyway.", "robot"),
    ("set2", "$10,000", 'is split among builders. <span class="tail"><mark>Your name</mark> could be on it.</span>', "swirl"),
    ("set3", 'Go from <span class="from">“I use AI”</span>', '<span class="line2">to <span class="goal">“I build AI agents.”</span></span>', "photo"),
]

SIZES = {
    "1080x1080": (1080, 1080, "square"),
    "1200x1200": (1200, 1200, "square"),
    "1920x1080": (1920, 1080, "landscape"),
    "1080x1920": (1080, 1920, "story"),
}

src = open(os.path.join(BANNERS, "contextcon-banner-1504x380.html")).read()
MEKO = re.search(r'<div class="logo">(.*?)</div>', src, re.S).group(1)
HE = '<img src="../assets/hackerearth-logo-light.svg" alt="HackerEarth">'
CC = '<img src="../assets/contextcon-logo-white.png" alt="ContextCon: Remember everything">'
CLAIM = 'Claim your spot <span aria-hidden="true">&rarr;</span>'

BASE_CSS = """
@font-face{font-family:'Bloka';src:url('../../Bloka-Bold.otf') format('opentype');font-weight:700;font-display:block}
/* Meko brand tokens — from meko-brand-guidelines v0.2 */
:root{--ground:#000;--panel:#121017;--purple:#7859fe;--purple-mid:#5f46cd;--white:#fff;--text:#e8e6ee;--muted:#9a97a8;
  --line-2:rgba(255,255,255,.18);--lime:#c7f252;
  --sans:'Inter',system-ui,-apple-system,sans-serif;--mono:'Roboto Mono',ui-monospace,monospace}
*{box-sizing:border-box}
html,body{margin:0;background:var(--ground)}
body{min-height:100vh;display:grid;place-items:center;-webkit-font-smoothing:antialiased}
.ad{position:relative;overflow:hidden;background:var(--ground);font-family:var(--sans);color:var(--text)}
.stage{position:absolute;left:0;top:0;transform-origin:0 0}
.photo{position:absolute;background:url(../assets/linkedin-robot.jpg) center/cover no-repeat}
.photo::after{content:'';position:absolute;inset:0}
.meko svg{display:block;width:100%;height:auto}
.hook{margin:0;font-family:'Bloka',var(--sans);font-weight:700;text-transform:uppercase;letter-spacing:-.0225em;color:var(--white)}
.hook .lead{display:block;color:var(--lime);line-height:.86}
.hook .rest{display:block;line-height:1.02;text-wrap:balance}
.hook .tail{display:block;margin-top:.3em;color:var(--purple)}
.hook mark{background:var(--purple-mid);color:var(--white);padding:0 .14em;margin:0 -.04em;border-radius:.08em;
  -webkit-box-decoration-break:clone;box-decoration-break:clone}
.cc img{display:block;width:100%;height:auto}
.kicker{margin:0;font-family:var(--mono);font-weight:500;letter-spacing:.14em;text-transform:uppercase;color:var(--muted)}
.cta{display:inline-flex;align-items:center;gap:.5em;background:var(--purple-mid);color:var(--white);font-weight:600;
  letter-spacing:-.01em;text-decoration:none;border-radius:.55em;white-space:nowrap}
.powered{margin:0;display:flex;align-items:center;gap:.7em;background:rgba(0,0,0,.6);border:1px solid var(--line-2);border-radius:999px}
.powered .k{font-family:var(--mono);font-weight:500;letter-spacing:.14em;text-transform:uppercase;color:var(--muted)}
.powered img{display:block;width:auto}
"""

LAYOUT_CSS = {
    # designed at 1080x1080; the 1200 version is the same stage scaled up
    "square": """
.stage{width:1080px;height:1080px}
.photo{left:430px;top:300px;width:760px;height:760px}
.photo::after{background:linear-gradient(90deg,#000 0%,rgba(0,0,0,.55) 18%,rgba(0,0,0,0) 38%),linear-gradient(180deg,#000 0%,rgba(0,0,0,0) 22%)}
.meko{position:absolute;left:72px;top:64px;width:180px}
.powered{position:absolute;right:64px;top:84px;font-size:15px;padding:10px 20px 10px 18px}
.powered .k{font-size:13px}.powered img{height:22px}
.hook{position:absolute;left:72px;top:216px;width:620px}
.hook .lead{font-size:200px}
.hook .rest{margin-top:22px;font-size:58px}
.bottom{position:absolute;left:72px;bottom:72px;display:flex;flex-direction:column;align-items:flex-start;gap:24px}
.cc{width:380px}
.kicker{font-size:17px}
.cta{font-size:28px;padding:20px 34px}
""",
    "landscape": """
.stage{width:1920px;height:1080px}
.photo{left:880px;top:-40px;width:1140px;height:1140px}
.photo::after{background:linear-gradient(90deg,#000 0%,rgba(0,0,0,.6) 16%,rgba(0,0,0,0) 34%)}
.meko{position:absolute;left:110px;top:90px;width:220px}
.powered{position:absolute;right:72px;bottom:64px;font-size:16px;padding:12px 24px 12px 20px}
.powered .k{font-size:14px}.powered img{height:26px}
.hook{position:absolute;left:110px;top:250px;width:960px}
.hook .lead{font-size:250px}
.hook .rest{margin-top:26px;font-size:76px}
.bottom{position:absolute;left:110px;bottom:96px;display:flex;align-items:center;gap:44px}
.bottom .left{display:flex;flex-direction:column;gap:16px}
.cc{width:440px}
.kicker{font-size:18px}
.cta{font-size:32px;padding:24px 40px}
""",
    # Meta story/reels safe zone: keep content clear of top ~14% and bottom ~20%
    "story": """
.stage{width:1080px;height:1920px}
.photo{left:120px;top:860px;width:1060px;height:1060px}
.photo::after{background:linear-gradient(180deg,#000 0%,rgba(0,0,0,.5) 12%,rgba(0,0,0,0) 28%,rgba(0,0,0,0) 62%,rgba(0,0,0,.85) 86%),linear-gradient(90deg,#000 0%,rgba(0,0,0,0) 22%)}
.meko{position:absolute;left:80px;top:280px;width:200px}
.powered{position:absolute;right:80px;top:306px;font-size:15px;padding:10px 20px 10px 18px}
.powered .k{font-size:13px}.powered img{height:22px}
.hook{position:absolute;left:80px;top:440px;width:920px}
.hook .lead{font-size:230px}
.hook .rest{margin-top:26px;font-size:72px}
.bottom{position:absolute;left:80px;right:80px;top:1250px;display:flex;flex-direction:column;align-items:flex-start;gap:28px}
.cc{width:440px}
.kicker{font-size:19px}
.cta{font-size:34px;padding:24px 42px}
""",
}

BODY = {
    "square": """
    <div class="photo" aria-hidden="true"></div>
    <div class="meko">{meko}</div>
    <p class="powered"><span class="k">Powered by</span>{he}</p>
    <h1 class="hook"><span class="lead">{lead}</span><span class="rest">{rest}</span></h1>
    <div class="bottom"><div class="cc">{cc}</div><p class="kicker">Worldwide virtual hackathon</p><a class="cta" href="#">{claim}</a></div>""",
    "landscape": """
    <div class="photo" aria-hidden="true"></div>
    <div class="meko">{meko}</div>
    <p class="powered"><span class="k">Powered by</span>{he}</p>
    <h1 class="hook"><span class="lead">{lead}</span><span class="rest">{rest}</span></h1>
    <div class="bottom"><div class="left"><div class="cc">{cc}</div><p class="kicker">Worldwide virtual hackathon</p></div><a class="cta" href="#">{claim}</a></div>""",
    "story": """
    <div class="photo" aria-hidden="true"></div>
    <div class="meko">{meko}</div>
    <p class="powered"><span class="k">Powered by</span>{he}</p>
    <h1 class="hook"><span class="lead">{lead}</span><span class="rest">{rest}</span></h1>
    <div class="bottom"><div class="cc">{cc}</div><p class="kicker">Worldwide virtual hackathon</p><a class="cta" href="#">{claim}</a></div>""",
}

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>ContextCon Meta ad</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&family=Roboto+Mono:wght@500&display=swap" rel="stylesheet">
<style>{base}{layout}
.ad{{width:{w}px;height:{h}px}}
.stage{{transform:scale({scale})}}
</style>
</head>
<body>
<main class="ad" aria-label="ContextCon: {label}">
  <div class="stage">{body}
  </div>
</main>
</body>
</html>
"""

# ---- swirl style: brand fluid texture (same construction as the key visual) ----
kv = open(os.path.join(BANNERS, "contextcon-key-visual-2000x1200.html")).read()
TEX_DEFS = re.search(r'<linearGradient id="g135".*?</linearGradient>', kv, re.S).group(0) + \
    re.search(r'<filter id="marble".*?</filter>', kv, re.S).group(0)
TEX_FLOWS = re.search(r'<g filter="url\(#marble\)">(.*?)</g>\s*</g>', kv, re.S).group(1)
# start each flow further left so only the mask decides where the texture fades
TEX_FLOWS = re.sub(r'd="M7([68])0 (-?\d+) C(\d+) ',
                   lambda m: f'd="M{240 if m.group(1) == "6" else 260} {m.group(2)} C{int(m.group(3)) - 300} ', TEX_FLOWS)

def texture(kind):
    if kind == "story":   # texture along the bottom, fading upward
        vb, x2, y2, stops = "700 -640 1300 1348", 0, 1, [(.38, 0), (.55, .35), (.75, .9), (1, 1)]
    elif kind == "square":  # texture on the right, fading left
        vb, x2, y2, stops = "860 -60 1260 1260", 1, 0, [(.44, 0), (.58, .3), (.78, .9), (1, 1)]
    else:                   # landscape
        vb, x2, y2, stops = "0 0 2000 1200", 1, 0, [(.48, 0), (.6, .3), (.8, .9), (1, 1)]
    x, y, w, h = vb.split()
    st = "".join(f'<stop offset="{o}" stop-color="#fff" stop-opacity="{a}"/>' for o, a in stops)
    return (f'<svg class="tex" viewBox="{vb}" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><defs>{TEX_DEFS}'
            f'<linearGradient id="fade" x1="0" y1="0" x2="{x2}" y2="{y2}">{st}</linearGradient>'
            f'<mask id="m"><rect x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#fade)"/></mask></defs>'
            f'<g mask="url(#m)"><rect x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#g135)" opacity=".18"/>'
            f'<g filter="url(#marble)">{TEX_FLOWS}</g></g></svg>')

SWIRL_CSS = {
    "square": """
.stage{width:1080px;height:1080px}
.tex{position:absolute;inset:0;width:1080px;height:1080px;display:block}
.cc{position:absolute;left:72px;top:72px;width:440px}
.kicker{position:absolute;left:74px;top:208px;font-size:17px}
.hook{position:absolute;left:72px;top:316px;width:700px}
.hook .lead{font-size:216px}
.hook .rest{margin-top:20px;font-size:58px}
.hook .tail{margin-top:30px;color:var(--white)}
.meko{position:absolute;left:72px;bottom:64px;width:180px}
.powered{position:absolute;right:64px;bottom:80px;font-size:15px;padding:10px 20px 10px 18px}
.powered .k{font-size:13px}.powered img{height:22px}
""",
    "landscape": """
.stage{width:1920px;height:1080px}
.tex{position:absolute;inset:0;width:1920px;height:1080px;display:block}
.cc{position:absolute;left:110px;top:96px;width:500px}
.kicker{position:absolute;left:112px;top:252px;font-size:18px}
.hook{position:absolute;left:110px;top:330px;width:1000px}
.hook .lead{font-size:260px}
.hook .rest{margin-top:22px;font-size:70px}
.hook .tail{margin-top:30px;color:var(--white)}
.meko{position:absolute;left:110px;bottom:84px;width:220px}
.powered{position:absolute;right:72px;bottom:96px;font-size:16px;padding:12px 24px 12px 20px}
.powered .k{font-size:14px}.powered img{height:26px}
""",
    # Meta story/reels safe zone: content clear of top ~14% and bottom ~20%
    "story": """
.stage{width:1080px;height:1920px}
.tex{position:absolute;left:0;bottom:0;width:1080px;height:1120px;display:block}
.cc{position:absolute;left:80px;top:280px;width:600px}
.kicker{position:absolute;left:82px;top:470px;font-size:20px}
.hook{position:absolute;left:80px;top:580px;width:920px}
.hook .lead{font-size:250px}
.hook .rest{margin-top:24px;font-size:72px}
.hook .tail{margin-top:34px;color:var(--white)}
.meko{position:absolute;left:80px;top:1440px;width:200px}
.powered{position:absolute;right:80px;top:1466px;font-size:15px;padding:10px 20px 10px 18px}
.powered .k{font-size:13px}.powered img{height:22px}
""",
}



SWIRL_BODY = """
    {tex}
    <div class="cc">{cc}</div>
    <p class="kicker">Worldwide virtual hackathon</p>
    <h1 class="hook"><span class="lead">{lead}</span><span class="rest">{rest}</span></h1>
    <div class="meko">{meko}</div>
    <p class="powered"><span class="k">Powered by</span>{he}</p>"""


# ---- photo style: transparent builder cutout anchored bottom-right ----
PHOTO_BASE = """
.glow{position:absolute;border-radius:50%;background:radial-gradient(closest-side,rgba(120,89,254,.42),rgba(74,53,162,.18) 55%,rgba(0,0,0,0))}
.person{position:absolute;right:0;bottom:0;display:block;height:auto}
.hook{color:var(--white);text-transform:none;letter-spacing:-.03em}
.hook .lead{display:block;color:var(--white);line-height:1.04}
.hook .from{position:relative;color:var(--muted);white-space:nowrap}
.hook .from::after{content:'';position:absolute;left:-.02em;right:-.02em;top:47%;height:.055em;background:var(--purple);border-radius:99px}
.hook .line2{display:block;line-height:1.04;text-wrap:balance}
.hook .goal{color:var(--lime)}
"""

PHOTO_CSS = {
    "square": """
.stage{width:1080px;height:1080px}
.glow{right:-120px;bottom:-140px;width:900px;height:900px}
.person{width:520px}
.cc{position:absolute;left:72px;top:64px;width:400px}
.kicker{position:absolute;left:74px;top:190px;font-size:16px}
.powered{position:absolute;right:64px;top:82px;font-size:15px;padding:10px 20px 10px 18px}
.powered .k{font-size:13px}.powered img{height:22px}
.hook{position:absolute;left:72px;top:300px;width:660px}
.hook .lead{font-size:72px}
.hook .line2{margin-top:10px;font-size:72px}
.meko{position:absolute;left:72px;bottom:64px;width:180px}
""",
    "landscape": """
.stage{width:1920px;height:1080px}
.glow{right:-80px;bottom:-200px;width:1200px;height:1200px}
.person{width:780px}
.cc{position:absolute;left:110px;top:96px;width:460px}
.kicker{position:absolute;left:112px;top:240px;font-size:17px}
.powered{position:absolute;right:72px;top:96px;font-size:16px;padding:12px 24px 12px 20px}
.powered .k{font-size:14px}.powered img{height:26px}
.hook{position:absolute;left:110px;top:440px;width:1010px}
.hook .lead{font-size:106px}
.hook .line2{margin-top:14px;font-size:106px}
.meko{position:absolute;left:110px;bottom:84px;width:220px}
""",
    # Meta story/reels safe zone: text clear of top ~14% and bottom ~20%
    "story": """
.stage{width:1080px;height:1920px}
.glow{right:-200px;bottom:-200px;width:1100px;height:1100px}
.person{width:720px}
.cc{position:absolute;left:80px;top:280px;width:480px}
.kicker{position:absolute;left:82px;top:432px;font-size:18px}
.powered{position:absolute;right:80px;top:300px;font-size:15px;padding:10px 20px 10px 18px}
.powered .k{font-size:13px}.powered img{height:22px}
.hook{position:absolute;left:80px;top:620px;width:940px}
.hook .lead{font-size:100px}
.hook .line2{margin-top:16px;font-size:100px}
.meko{position:absolute;left:80px;top:1440px;width:200px}
""",
}

PHOTO_BODY = """
    <div class="glow" aria-hidden="true"></div>
    <img class="person" src="../assets/neon-laptop-builder.png" alt="">
    <div class="cc">{cc}</div>
    <p class="kicker">Worldwide virtual hackathon</p>
    <p class="powered"><span class="k">Powered by</span>{he}</p>
    <h1 class="hook"><span class="lead">{lead}</span>{rest}</h1>
    <div class="meko">{meko}</div>"""

for set_id, lead, rest, style in SETS:
    for size, (w, h, kind) in SIZES.items():
        design_w = {"square": 1080, "landscape": 1920, "story": 1080}[kind]
        if style == "swirl":
            body = SWIRL_BODY.format(tex=texture(kind), meko=MEKO, he=HE, cc=CC, lead=lead, rest=rest)
            layout = SWIRL_CSS[kind]
        elif style == "photo":
            body = PHOTO_BODY.format(meko=MEKO, he=HE, cc=CC, lead=lead, rest=rest)
            layout = PHOTO_BASE + PHOTO_CSS[kind]
        else:
            body = BODY[kind].format(meko=MEKO, he=HE, cc=CC, claim=CLAIM, lead=lead, rest=rest)
            layout = LAYOUT_CSS[kind]
        html = PAGE.format(base=BASE_CSS, layout=layout, w=w, h=h, scale=w / design_w,
                           label=re.sub(r"<[^>]+>", "", f"{lead} {rest}"), body=body)
        out = os.path.join(HERE, f"contextcon-meta-{set_id}-{size}.html")
        open(out, "w").write(html)
        print("wrote", os.path.relpath(out))
