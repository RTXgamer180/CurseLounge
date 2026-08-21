from flask import Flask, request, redirect, url_for, render_template_string
from pathlib import Path
import os

app = Flask("CurseLounge")
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>CurseLounge — Mods & Addons</title>
<style>
*{box-sizing:border-box}body{margin:0;font-family:Inter,Arial,sans-serif;background:#17181c;color:#f4f4f5}
a{color:inherit;text-decoration:none}.top{height:64px;background:#24252a;display:flex;align-items:center;padding:0 5%;gap:28px;border-bottom:1px solid #35363d}
.logo{font-size:25px;font-weight:900;color:#f16436}.nav{display:flex;gap:22px;font-weight:700}.nav a:hover{color:#f16436}
.actions{margin-left:auto;display:flex;gap:10px}.btn{border:1px solid #4a4b52;border-radius:7px;padding:10px 16px;background:#2d2e34}.premium{background:#f16436;border-color:#f16436}
.hero{min-height:500px;padding:80px 6%;text-align:center;background:radial-gradient(circle at 50% 20%,#30323a,#17181c 65%)}
.hero h1{font-size:52px;margin:10px auto 15px;max-width:850px}.hero p{font-size:19px;color:#bfc0c7;max-width:720px;margin:0 auto 35px}
.search{display:flex;max-width:700px;margin:auto;background:#fff;border-radius:8px;overflow:hidden}.search input{flex:1;padding:18px;border:0;font-size:17px;outline:0}.search button{border:0;background:#f16436;color:#fff;padding:0 25px;font-weight:800}
.stats{display:flex;justify-content:center;gap:55px;margin-top:45px;flex-wrap:wrap}.stat b{display:block;font-size:27px}.stat span{color:#aaa;font-size:12px}
section{padding:55px 6%;max-width:1250px;margin:auto}.section-title{display:flex;justify-content:space-between;align-items:center}.section-title h2{font-size:30px}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:18px}
.card{background:#24252a;border:1px solid #34353b;border-radius:10px;padding:20px;transition:.2s}.card:hover{transform:translateY(-3px);border-color:#f16436}.icon{height:80px;border-radius:8px;background:linear-gradient(135deg,#34363e,#1d1e23);display:grid;place-items:center;font-size:32px;margin-bottom:15px}.card h3{margin:8px 0}.muted{color:#999;font-size:14px}
.news{display:grid;grid-template-columns:repeat(auto-fit,minmax(270px,1fr));gap:18px}.news .card{min-height:170px}.tag{color:#f16436;font-size:12px;font-weight:800;text-transform:uppercase}
.feature{background:#23242a;border-radius:12px;padding:45px;margin-top:30px;display:grid;grid-template-columns:1fr 1fr;gap:35px;align-items:center}.feature h2{font-size:35px}.feature p{color:#b8b9c0;line-height:1.6}.feature-art{height:270px;border-radius:12px;background:linear-gradient(135deg,#f16436,#702d20 55%,#292a30);display:grid;place-items:center;font-size:70px}
footer{background:#111216;border-top:1px solid #303137;padding:45px 6%;color:#aaa}.footgrid{max-width:1200px;margin:auto;display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:30px}.footgrid h4{color:#fff}.footgrid a{display:block;margin:10px 0}.copyright{margin-top:35px;border-top:1px solid #292a2f;padding-top:20px}
@media(max-width:700px){.nav{display:none}.hero h1{font-size:38px}.feature{grid-template-columns:1fr}.stats{gap:25px}.top{padding:0 18px}}
.upload-box{margin-top:20px;padding:18px;background:#24252a;border:1px solid #34353b;border-radius:10px}
.upload-box input{max-width:100%}.upload-box button{border:1px solid #f16436;background:#f16436;color:#fff;border-radius:7px;padding:10px 16px;font-weight:800}
</style>
</head>
<body>
<header class="top">
  <div class="logo">CurseLounge</div>
  <nav class="nav"><a href="#games">Browse</a><a href="#create">Create</a><a href="#news">News</a><a href="#app">App</a></nav>
  <div class="actions"><a class="btn" href="#login">Log in</a><a class="btn premium" href="#premium">Go Premium</a></div>
</header>

<main>
<section class="hero">
  <div class="tag">MODS • ADDONS • COMMUNITY</div>
  <h1>Explore Thousands of Legendary Mods</h1>
  <p>Discover mods for your favorite games, or forge your own and share them with a huge gaming community.</p>
  <form class="search" method="get" action="/search">
    <input id="searchBox" placeholder="Search for a game..." aria-label="Search">
    <button>Search</button>
  </form>
  <div class="stats">
    <div class="stat"><b>500K+</b><span>MODS</span></div>
    <div class="stat"><b>100B+</b><span>DOWNLOADS</span></div>
    <div class="stat"><b>134K</b><span>MOD AUTHORS</span></div>
    <div class="stat"><b>$20M+</b><span>PAID TO CREATORS</span></div>
  </div>
</section>

<section id="games">
<div class="section-title"><h2>Popular Games</h2><a class="tag" href="#">View all games →</a></div>
<div class="grid">
  <a class="card" href="#"><div class="icon">⛏️</div><h3>Minecraft</h3><div class="muted">308.3K projects • 122.5B downloads</div></a>
  <a class="card" href="#"><div class="icon">⚔️</div><h3>World of Warcraft</h3><div class="muted">25.3K projects • 9.9B downloads</div></a>
  <a class="card" href="#"><div class="icon">🦖</div><h3>ARK: Survival Ascended</h3><div class="muted">6.9K projects • 1.3B downloads</div></a>
  <a class="card" href="#"><div class="icon">🏡</div><h3>The Sims 4</h3><div class="muted">131.2K projects • 4.1B downloads</div></a>
  <a class="card" href="#"><div class="icon">🚀</div><h3>Hytale</h3><div class="muted">6.3K projects • 29.5M downloads</div></a>
  <a class="card" href="#"><div class="icon">🌍</div><h3>Minecraft Bedrock</h3><div class="muted">20.6K projects • 680.5M downloads</div></a>
</div>
</section>

<section id="news">
<div class="section-title"><h2>Latest News</h2><a class="tag" href="#">View all →</a></div>
<div class="news">
  <article class="card"><div class="tag">News</div><h3>Submissions Are Now Open</h3><p class="muted">Build combat, survival, or creative modes and compete for prizes.</p></article>
  <article class="card"><div class="tag">News</div><h3>Echoes of the Past: ModJam 2026</h3><p class="muted">The contest is open for submissions. Enter your project today.</p></article>
  <article class="card"><div class="tag">Creator</div><h3>Creator of the Month</h3><p class="muted">Celebrating creators whose projects bring new adventures to players.</p></article>
  <article class="card"><div class="tag">Update</div><h3>Platform Release Notes</h3><p class="muted">Check out the latest platform features and improvements.</p></article>
</div>
</section>

<section id="app">
<div class="feature">
  <div><div class="tag">CURSEFORGE APP</div><h2>The Easiest Way to Manage Your Mods</h2><p>Install, update, and manage mods with one click. Keep your favorite games organized and ready to play.</p><a class="btn premium" href="#">Download App</a></div>
  <div class="feature-art">⚒️</div>
</div>
</section>

<section id="create">
<div class="feature">
  <div class="feature-art">✨</div>
  <div><div class="tag">CREATORS</div><h2>Create, Share, and Earn</h2><p>Publish your creations, reach players, and build a community around your projects.</p><a class="btn" href="#">Start Creating</a></div>
</div>
</section>

<section id="premium">
<div class="feature">
  <div><div class="tag">PREMIUM</div><h2>Support Creators with CurseLounge Premium</h2><p>Enjoy an ad-free browsing experience and extra features while supporting the creators you love.</p><a class="btn premium" href="#">Go Premium</a></div>
  <div class="feature-art">👑</div>
</div>
</section>
</main>


<section id="upload">
<div class="feature">
  <div>
    <div class="tag">UPLOAD</div>
    <h2>Upload a Project</h2>
    <p>Choose a file and upload it to this CurseLounge instance.</p>
    <form class="upload-box" action="/upload" method="post" enctype="multipart/form-data">
      <input type="file" name="file" required>
      <button type="submit">Upload</button>
    </form>
  </div>
  <div class="feature-art">⬆️</div>
</div>
</section>
<footer>
<div class="footgrid">
  <div><h4>Games</h4><a href="#games">All games</a><a href="#games">Minecraft</a><a href="#games">World of Warcraft</a><a href="#games">The Sims 4</a></div>
  <div><h4>Create</h4><a href="#create">Start a project</a><a href="#create">Submission guide</a><a href="#create">Author rewards</a></div>
  <div><h4>Community</h4><a href="#news">Blog</a><a href="#">Discord</a><a href="#">Ideas Portal</a></div>
  <div><h4>Support</h4><a href="#">Knowledge base</a><a href="#">Troubleshooting</a><a href="#">Contact us</a></div>
</div>
<div class="copyright">© 2026 CurseLounge-style demo • Built from scratch, not copied from CurseLounge source.</div>
</footer>


</body>
</html>"""

@app.route("/")
def index():
    return render_template_string(PAGE)

@app.route("/search")
def search():
    q = request.args.get("q", "").strip()
    return redirect(url_for("index"))

@app.route("/upload", methods=["POST"])
def upload():
    f = request.files.get("file")
    if not f or not f.filename:
        return redirect(url_for("index"))
    f.save(UPLOAD_DIR / Path(f.filename).name)
    return redirect(url_for("index"))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "10000"))
    app.run(host="0.0.0.0", port=port)
