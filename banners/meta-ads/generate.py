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
#   style "board": swirl + a winners-board card with an empty "your name" slot
SETS = [
    ("set1", "$10,000", "prize money for a project you would build anyway.", "robot"),
    ("set2", "$10,000", 'is split among builders. <span class="tail">Your name could be on it.</span>', "board"),
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
.hook{position:absolute;left:72px;top:340px;width:640px}
.hook .lead{font-size:200px}
.hook .rest{margin-top:22px;font-size:60px}
.meko{position:absolute;left:72px;bottom:64px;width:180px}
.powered{position:absolute;right:64px;bottom:80px;font-size:15px;padding:10px 20px 10px 18px}
.powered .k{font-size:13px}.powered img{height:22px}
""",
    "landscape": """
.stage{width:1920px;height:1080px}
.tex{position:absolute;inset:0;width:1920px;height:1080px;display:block}
.cc{position:absolute;left:110px;top:96px;width:500px}
.kicker{position:absolute;left:112px;top:252px;font-size:18px}
.hook{position:absolute;left:110px;top:370px;width:980px}
.hook .lead{font-size:240px}
.hook .rest{margin-top:24px;font-size:72px}
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
.hook{position:absolute;left:80px;top:600px;width:920px}
.hook .lead{font-size:230px}
.hook .rest{margin-top:26px;font-size:72px}
.meko{position:absolute;left:80px;top:1440px;width:200px}
.powered{position:absolute;right:80px;top:1466px;font-size:15px;padding:10px 20px 10px 18px}
.powered .k{font-size:13px}.powered img{height:22px}
""",
}


BOARD_CARD = """
    <div class="board" aria-hidden="true">
      <div class="bh"><span>Winners board</span><span>Submissions close 17 Jan</span></div>
      <div class="row you"><span class="rk">01</span><span class="nm">Your name<i class="cur"></i></span><span class="tag">You?</span></div>
      <div class="row"><span class="rk">02</span><span class="bar" style="width:58%"></span></div>
      <div class="row"><span class="rk">03</span><span class="bar" style="width:44%"></span></div>
    </div>"""

BOARD_BASE = """
.hook .rest{line-height:1}
.board{position:absolute;background:rgba(18,16,23,.94);border:1px solid var(--line-2);border-radius:.9em;padding:.9em 1em 1em;
  box-shadow:0 1.5em 4em rgba(0,0,0,.55)}
.bh{display:flex;justify-content:space-between;gap:1em;font-family:var(--mono);font-weight:500;font-size:.5em;letter-spacing:.16em;
  text-transform:uppercase;color:var(--muted);padding:0 .4em .9em}
.row{display:flex;align-items:center;gap:.8em;height:1.9em;padding:0 .8em;border-radius:.55em;border:1px solid transparent}
.row + .row{margin-top:.2em}
.rk{flex:none;width:1.6em;font-family:var(--mono);font-weight:500;font-size:.62em;color:var(--dim,#6a6778)}
.bar{display:block;height:.42em;border-radius:99px;background:rgba(255,255,255,.12)}
.row.you{background:rgba(199,242,82,.08);border-color:rgba(199,242,82,.7)}
.row.you .rk{color:var(--lime)}
.nm{font-family:'Bloka',var(--sans);font-weight:700;text-transform:uppercase;letter-spacing:-.0225em;font-size:.95em;color:var(--white);
  display:flex;align-items:center}
.cur{display:inline-block;width:.09em;height:1.05em;margin-left:.12em;background:var(--lime)}
.tag{margin-left:auto;font-family:var(--mono);font-weight:500;font-size:.5em;letter-spacing:.16em;text-transform:uppercase;
  color:#000;background:var(--lime);border-radius:99px;padding:.45em .9em}
"""

BOARD_CSS = {
    "square": """
.stage{width:1080px;height:1080px}
.tex{position:absolute;inset:0;width:1080px;height:1080px;display:block}
.cc{position:absolute;left:72px;top:64px;width:360px}
.kicker{position:absolute;left:74px;top:178px;font-size:15px}
.hook{position:absolute;left:72px;top:240px;width:940px}
.hook .lead{font-size:168px}
.hook .rest{margin-top:14px;font-size:54px}
.hook .tail{margin-top:18px;font-size:30px;letter-spacing:.02em}
.board{left:72px;top:570px;width:620px;font-size:32px}
.meko{position:absolute;left:72px;bottom:60px;width:180px}
.powered{position:absolute;right:64px;bottom:76px;font-size:15px;padding:10px 20px 10px 18px}
.powered .k{font-size:13px}.powered img{height:22px}
""",
    "landscape": """
.stage{width:1920px;height:1080px}
.tex{position:absolute;inset:0;width:1920px;height:1080px;display:block}
.cc{position:absolute;left:110px;top:96px;width:460px}
.kicker{position:absolute;left:112px;top:240px;font-size:17px}
.hook{position:absolute;left:110px;top:340px;width:900px}
.hook .lead{font-size:230px}
.hook .rest{margin-top:20px;font-size:66px;text-wrap:wrap}
.hook .tail{margin-top:26px;font-size:40px;letter-spacing:.02em}
.board{left:1120px;top:360px;width:680px;font-size:38px}
.meko{position:absolute;left:110px;bottom:84px;width:220px}
.powered{position:absolute;right:72px;bottom:96px;font-size:16px;padding:12px 24px 12px 20px}
.powered .k{font-size:14px}.powered img{height:26px}
""",
    "story": """
.stage{width:1080px;height:1920px}
.tex{position:absolute;left:0;bottom:0;width:1080px;height:1120px;display:block}
.cc{position:absolute;left:80px;top:280px;width:480px}
.kicker{position:absolute;left:82px;top:432px;font-size:18px}
.hook{position:absolute;left:80px;top:520px;width:920px}
.hook .lead{font-size:220px}
.hook .rest{margin-top:20px;font-size:64px}
.hook .tail{margin-top:26px;font-size:40px;letter-spacing:.02em}
.board{left:80px;top:960px;width:920px;font-size:40px}
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

for set_id, lead, rest, style in SETS:
    for size, (w, h, kind) in SIZES.items():
        design_w = {"square": 1080, "landscape": 1920, "story": 1080}[kind]
        if style == "swirl":
            body = SWIRL_BODY.format(tex=texture(kind), meko=MEKO, he=HE, cc=CC, lead=lead, rest=rest)
            layout = SWIRL_CSS[kind]
        elif style == "board":
            body = SWIRL_BODY.format(tex=texture(kind), meko=MEKO, he=HE, cc=CC, lead=lead, rest=rest) + BOARD_CARD
            layout = BOARD_BASE + BOARD_CSS[kind]
        else:
            body = BODY[kind].format(meko=MEKO, he=HE, cc=CC, claim=CLAIM, lead=lead, rest=rest)
            layout = LAYOUT_CSS[kind]
        html = PAGE.format(base=BASE_CSS, layout=layout, w=w, h=h, scale=w / design_w,
                           label=re.sub(r"<[^>]+>", "", f"{lead} {rest}"), body=body)
        out = os.path.join(HERE, f"contextcon-meta-{set_id}-{size}.html")
        open(out, "w").write(html)
        print("wrote", os.path.relpath(out))
