from flask import Flask, render_template_string
import random

app = Flask(__name__)

QUOTES = [
    "Build. Break. Repeat.",
    "Every great project started with one file.",
    "CurseLounge is online ⚡",
    "Code today. Flex tomorrow.",
    "Welcome to the neon side of the internet."
]

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>CurseLounge</title>

<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700&family=Inter:wght@300;400;600&display=swap');

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
}

body{
    font-family:Inter,sans-serif;
    background:#050510;
    overflow:hidden;
    color:white;
}

/* Animated Background */
.bg{
    position:fixed;
    inset:0;
    background:
        radial-gradient(circle at 20% 30%,#7b2cff33,transparent 25%),
        radial-gradient(circle at 80% 70%,#00d4ff33,transparent 25%),
        radial-gradient(circle at 50% 50%,#ffffff11,transparent 45%);
    animation:bgMove 12s ease-in-out infinite alternate;
}

@keyframes bgMove{
    from{transform:scale(1) rotate(0deg);}
    to{transform:scale(1.15) rotate(3deg);}
}

/* Floating Particles */
.particle{
    position:absolute;
    width:4px;
    height:4px;
    border-radius:50%;
    background:#66f0ff;
    box-shadow:0 0 10px #66f0ff;
    animation:float linear infinite;
}

@keyframes float{
    from{transform:translateY(110vh);}
    to{transform:translateY(-10vh);}
}

.container{
    position:relative;
    z-index:2;
    height:100vh;
    display:flex;
    align-items:center;
    justify-content:center;
    flex-direction:column;
    text-align:center;
    padding:20px;
}

.logo{
    font-family:Orbitron,sans-serif;
    font-size:clamp(48px,10vw,90px);
    color:#8b5cf6;
    text-shadow:
        0 0 12px #8b5cf6,
        0 0 28px #7c3aed;
    margin-bottom:10px;
}

.subtitle{
    font-size:18px;
    opacity:.85;
    margin-bottom:35px;
}

.card{
    width:min(800px,90%);
    padding:30px;
    border-radius:24px;
    backdrop-filter:blur(18px);
    background:rgba(255,255,255,.06);
    border:1px solid rgba(255,255,255,.12);
    box-shadow:0 0 35px rgba(139,92,246,.25);
}

.quote{
    font-size:26px;
    font-weight:600;
    color:#ffffff;
    min-height:60px;
}

.stats{
    display:flex;
    justify-content:space-around;
    margin-top:30px;
    flex-wrap:wrap;
    gap:20px;
}

.stat h2{
    color:#66f0ff;
    font-size:32px;
}

.stat p{
    opacity:.7;
}

.btn{
    margin-top:35px;
    padding:15px 30px;
    border:none;
    border-radius:999px;
    background:linear-gradient(90deg,#7c3aed,#06b6d4);
    color:white;
    font-weight:bold;
    font-size:16px;
    cursor:pointer;
    transition:.25s;
    box-shadow:0 0 20px #7c3aed66;
}

.btn:hover{
    transform:translateY(-3px) scale(1.04);
    box-shadow:0 0 30px #06b6d4aa;
}

footer{
    position:absolute;
    bottom:20px;
    opacity:.45;
    font-size:13px;
}
</style>
</head>
<body>

<div class="bg"></div>

<div id="particles"></div>

<div class="container">
    <div class="logo">CurseLounge</div>
    <div class="subtitle">Neon Flask Website • Running on Render</div>

    <div class="card">
        <div class="quote">“{{ quote }}”</div>

        <div class="stats">
            <div class="stat">
                <h2 id="visits">1337</h2>
                <p>Visitors</p>
            </div>
            <div class="stat">
                <h2 id="uptime">99.9%</h2>
                <p>Uptime</p>
            </div>
            <div class="stat">
                <h2>Flask</h2>
                <p>Backend</p>
            </div>
        </div>

        <button class="btn" onclick="surprise()">
            ⚡ Surprise Me
        </button>
    </div>

    <footer>Made with Python + Flask</footer>
</div>

<script>
// Particles
for(let i=0;i<70;i++){
    const p=document.createElement("div");
    p.className="particle";
    p.style.left=Math.random()*100+"vw";
    p.style.animationDuration=(6+Math.random()*8)+"s";
    p.style.animationDelay=(-Math.random()*10)+"s";
    p.style.opacity=Math.random();
    document.getElementById("particles").appendChild(p);
}

const msgs=[
"✨ Keep building cool stuff.",
"⚡ Flask is serving pixels.",
"🌌 Neon mode activated.",
"🚀 Deploy > Debug > Repeat.",
"💜 CurseLounge welcomes you."
];

function surprise(){
    document.querySelector(".quote").innerText=
        msgs[Math.floor(Math.random()*msgs.length)];
}

setInterval(()=>{
    const n=document.getElementById("visits");
    n.innerText=(parseInt(n.innerText)+Math.floor(Math.random()*4)).toLocaleString();
},2500);
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML, quote=random.choice(QUOTES))


@app.route("/api")
def api():
    return {
        "status": "online",
        "website": "CurseLounge",
        "framework": "Flask"
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
