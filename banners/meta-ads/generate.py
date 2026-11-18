"""Generate ContextCon Meta ad HTML files: one set per hook, four sizes each.

Run from the repo root:  python3 banners/meta-ads/generate.py
Then render PNGs with:    node banners/meta-ads/render.js
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
BANNERS = os.path.dirname(HERE)

# Each set: id, highlighted lead (lime), rest of the hook (white).
SETS = [
    ("set1", "$10,000", "prize money for a project you would build anyway."),
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

for set_id, lead, rest in SETS:
    for size, (w, h, kind) in SIZES.items():
        design_w = {"square": 1080, "landscape": 1920, "story": 1080}[kind]
        body = BODY[kind].format(meko=MEKO, he=HE, cc=CC, claim=CLAIM, lead=lead, rest=rest)
        html = PAGE.format(base=BASE_CSS, layout=LAYOUT_CSS[kind], w=w, h=h, scale=w / design_w,
                           label=f"{lead} {rest}", body=body)
        out = os.path.join(HERE, f"contextcon-meta-{set_id}-{size}.html")
        open(out, "w").write(html)
        print("wrote", os.path.relpath(out))
