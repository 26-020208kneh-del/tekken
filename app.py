import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Iron Fighters",
    page_icon="🥊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown(
    """
    <style>
        html, body, [data-testid="stAppViewContainer"] {
            background: #080808;
        }

        [data-testid="stHeader"] {
            background: rgba(0,0,0,0);
        }

        .block-container {
            padding-top: 1rem;
            padding-bottom: 0;
            max-width: 1400px;
        }

        h1 {
            text-align: center;
            color: white;
            margin-bottom: 5px;
        }

        .subtitle {
            text-align: center;
            color: #999;
            margin-bottom: 15px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("# 🥊 IRON FIGHTERS")
st.markdown(
    '<div class="subtitle">2D Fighting Game · Player vs CPU</div>',
    unsafe_allow_html=True
)

game_html = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">

<style>
* {
    box-sizing: border-box;
}

body {
    margin: 0;
    background: #080808;
    color: white;
    font-family: Arial, sans-serif;
    overflow: hidden;
}

#game-wrapper {
    width: 100%;
    max-width: 1200px;
    margin: auto;
}

#game {
    position: relative;
    width: 100%;
    height: 680px;
    background:
        linear-gradient(
            to bottom,
            #171b35 0%,
            #28365b 55%,
            #70412e 56%,
            #161616 57%,
            #111 100%
        );
    overflow: hidden;
    border: 3px solid #333;
    border-radius: 12px;
    box-shadow: 0 0 40px rgba(255, 40, 40, 0.15);
}

#arena-light {
    position: absolute;
    width: 300px;
    height: 300px;
    left: 50%;
    top: 0;
    transform: translateX(-50%);
    background: radial-gradient(
        ellipse,
        rgba(255,255,220,0.2),
        transparent 70%
    );
}

.floor-line {
    position: absolute;
    left: 0;
    right: 0;
    bottom: 115px;
    height: 5px;
    background: #e5b35a;
    box-shadow: 0 0 15px #e5b35a;
}

#hud {
    position: absolute;
    left: 25px;
    right: 25px;
    top: 20px;
    display: flex;
    align-items: center;
    gap: 18px;
    z-index: 10;
}

.name {
    font-weight: bold;
    font-size: 20px;
    width: 130px;
}

.enemy-name {
    text-align: right;
}

.health {
    height: 28px;
    background: #222;
    border: 2px solid #ddd;
    flex: 1;
    overflow: hidden;
    border-radius: 5px;
}

.health-inner {
    height: 100%;
    background: linear-gradient(90deg, #19e56d, #aaff44);
    width: 100%;
    transition: width .15s;
}

#enemy-health .health-inner {
    float: right;
    background: linear-gradient(90deg, #ff4949, #ffb347);
}

#timer {
    font-size: 34px;
    font-weight: bold;
    min-width: 60px;
    text-align: center;
}

.fighter {
    position: absolute;
    width: 70px;
    height: 160px;
    bottom: 118px;
    z-index: 5;
}

.body {
    position: absolute;
    width: 45px;
    height: 70px;
    left: 13px;
    top: 42px;
    border-radius: 15px 15px 8px 8px;
}

.head {
    position: absolute;
    width: 48px;
    height: 48px;
    left: 11px;
    top: 0;
    border-radius: 50%;
}

.arm {
    position: absolute;
    width: 16px;
    height: 70px;
    top: 45px;
    border-radius: 10px;
    transform-origin: top center;
}

.arm1 {
    left: 5px;
    transform: rotate(18deg);
}

.arm2 {
    right: 5px;
    transform: rotate(-18deg);
}

.leg {
    position: absolute;
    width: 18px;
    height: 65px;
    top: 105px;
    border-radius: 10px;
}

.leg1 {
    left: 13px;
    transform: rotate(7deg);
}

.leg2 {
    right: 13px;
    transform: rotate(-7deg);
}

#player {
    left: 160px;
}

#player .head {
    background: #f1bd91;
    border: 4px solid #111;
}

#player .body {
    background: #2878ff;
}

#player .arm,
#player .leg {
    background: #2878ff;
}

#player .leg {
    background: #173e99;
}

#cpu {
    left: calc(100% - 230px);
}

#cpu .head {
    background: #9f6746;
    border: 4px solid #111;
}

#cpu .body {
    background: #d52727;
}

#cpu .arm,
#cpu .leg {
    background: #d52727;
}

#cpu .leg {
    background: #8d1717;
}

.fighter.attack .arm2 {
    transform: rotate(-75deg) translateY(-10px);
}

.fighter.kick .leg2 {
    transform: rotate(75deg);
}

.fighter.hit {
    animation: hit .15s linear;
}

@keyframes hit {
    50% {
        transform: translateX(-12px);
        filter: brightness(2);
    }
}

#message {
    position: absolute;
    left: 50%;
    top: 44%;
    transform: translate(-50%, -50%);
    font-size: 54px;
    font-weight: 900;
    text-shadow: 0 4px 20px black;
    display: none;
    z-index: 20;
    text-align: center;
}

#controls {
    position: absolute;
    bottom: 15px;
    left: 50%;
    transform: translateX(-50%);
    color: #ddd;
    font-size: 15px;
    background: rgba(0,0,0,.65);
    padding: 9px 18px;
    border-radius: 20px;
    z-index: 20;
}

#start-screen {
    position: absolute;
    inset: 0;
    background: rgba(0,0,0,.82);
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    z-index: 30;
}

#start-screen h2 {
    font-size: 52px;
    margin: 0 0 20px;
}

button {
    border: none;
    padding: 15px 38px;
    font-size: 20px;
    font-weight: bold;
    border-radius: 8px;
    background: #e52d2d;
    color: white;
    cursor: pointer;
}

button:hover {
    background: #ff4444;
}

#mobile-controls {
    display: none;
}

@media (max-width: 700px) {
    #game {
        height: 560px;
    }

    #mobile-controls {
        display: flex;
        position: absolute;
        bottom: 15px;
        left: 15px;
        right: 15px;
        justify-content: space-between;
        z-index: 25;
    }

    .mobile-group {
        display: flex;
        gap: 8px;
    }

    .mobile-btn {
        width: 55px;
        height: 55px;
        padding: 0;
        font-size: 15px;
        background: rgba(0,0,0,.7);
        border: 1px solid #777;
    }

    #controls {
        display: none;
    }

    .name {
        font-size: 13px;
        width: 70px;
    }

    #timer {
        font-size: 25px;
        min-width: 40px;
    }
}
</style>
</head>

<body>

<div id="game-wrapper">

<div id="game">

<div id="arena-light"></div>
<div class="floor-line"></div>

<div id="hud">

    <div class="name">PLAYER</div>

    <div class="health">
        <div id="player-hp" class="health-inner"></div>
    </div>

    <div id="timer">60</div>

    <div class="health" id="enemy-health">
        <div id="cpu-hp" class="health-inner"></div>
    </div>

    <div class="name enemy-name">CPU</div>

</div>

<div id="player" class="fighter">

    <div class="head"></div>
    <div class="body"></div>

    <div class="arm arm1"></div>
    <div class="arm arm2"></div>

    <div class="leg leg1"></div>
    <div class="leg leg2"></div>

</div>

<div id="cpu" class="fighter">

    <div class="head"></div>
    <div class="body"></div>

    <div class="arm arm1"></div>
    <div class="arm arm2"></div>

    <div class="leg leg1"></div>
    <div class="leg leg2"></div>

</div>

<div id="message"></div>

<div id="controls">
    ← → 이동 &nbsp; | &nbsp;
    ↑ 점프 &nbsp; | &nbsp;
    A 펀치 &nbsp; | &nbsp;
    S 킥 &nbsp; | &nbsp;
    D 필살기
</div>

<div id="mobile-controls">

    <div class="mobile-group">
        <button class="mobile-btn" id="leftBtn">←</button>
        <button class="mobile-btn" id="rightBtn">→</button>
        <button class="mobile-btn" id="jumpBtn">↑</button>
    </div>

    <div class="mobile-group">
        <button class="mobile-btn" id="punchBtn">A</button>
        <button class="mobile-btn" id="kickBtn">S</button>
        <button class="mobile-btn" id="specialBtn">D</button>
    </div>

</div>

<div id="start-screen">

    <h2>IRON FIGHTERS</h2>

    <p>
        Player vs CPU
    </p>

    <button id="startBtn">
        FIGHT!
    </button>

</div>

</div>

</div>

<script>

const game = document.getElementById("game");

const player = document.getElementById("player");
const cpu = document.getElementById("cpu");

const playerHPBar = document.getElementById("player-hp");
const cpuHPBar = document.getElementById("cpu-hp");

const timerElement = document.getElementById("timer");
const message = document.getElementById("message");

const startScreen = document.getElementById("start-screen");
const startBtn = document.getElementById("startBtn");

let running = false;

let playerX = 160;
let cpuX = 800;

let playerY = 0;
let cpuY = 0;

let playerHP = 100;
let cpuHP = 100;

let playerVelocityY = 0;
let cpuVelocityY = 0;

let keys = {};

let timer = 60;

let playerCooldown = 0;
let cpuCooldown = 0;

let cpuDirectionTimer = 0;

let animationFrame;

document.addEventListener("keydown", function(e) {

    keys[e.key.toLowerCase()] = true;

    if (
        ["arrowleft", "arrowright", "arrowup", " "]
        .includes(e.key.toLowerCase())
    ) {
        e.preventDefault();
    }

});

document.addEventListener("keyup", function(e) {
    keys[e.key.toLowerCase()] = false;
});


function clamp(value, min, max) {
    return Math.max(min, Math.min(max, value));
}


function distance() {
    return Math.abs(
        (playerX + 35) - (cpuX + 35)
    );
}


function startGame() {

    running = true;

    playerX = 160;
    cpuX = game.clientWidth - 230;

    playerY = 0;
    cpuY = 0;

    playerHP = 100;
    cpuHP = 100;

    playerVelocityY = 0;
    cpuVelocityY = 0;

    timer = 60;

    playerCooldown = 0;
    cpuCooldown = 0;

    message.style.display = "none";

    startScreen.style.display = "none";

    updateBars();

    cancelAnimationFrame(animationFrame);

    gameLoop();

}


function updateBars() {

    playerHPBar.style.width = playerHP + "%";
    cpuHPBar.style.width = cpuHP + "%";

}


function jump(character) {

    if (character === "player") {

        if (playerY === 0) {
            playerVelocityY = 15;
        }

    } else {

        if (cpuY === 0) {
            cpuVelocityY = 15;
        }

    }

}


function attack(attacker, type) {

    if (!running) return;

    if (attacker === "player") {

        if (playerCooldown > 0) return;

        playerCooldown =
            type === "special" ? 50 : 25;

        player.classList.remove("attack");
        player.classList.remove("kick");

        if (type === "punch") {

            player.classList.add("attack");

        } else {

            player.classList.add("kick");

        }

        setTimeout(() => {

            player.classList.remove("attack");
            player.classList.remove("kick");

        }, 180);

        let range =
            type === "special" ? 145 : 100;

        if (distance() < range) {

            let damage;

            if (type === "punch") {
                damage = 7;
            }

            else if (type === "kick") {
                damage = 10;
            }

            else {
                damage = 20;
            }

            cpuHP -= damage;

            cpu.classList.add("hit");

            setTimeout(() => {
                cpu.classList.remove("hit");
            }, 150);

            updateBars();

        }

    }

    else {

        if (cpuCooldown > 0) return;

        cpuCooldown =
            type === "special" ? 65 : 35;

        cpu.classList.remove("attack");
        cpu.classList.remove("kick");

        if (type === "punch") {

            cpu.classList.add("attack");

        } else {

            cpu.classList.add("kick");

        }

        setTimeout(() => {

            cpu.classList.remove("attack");
            cpu.classList.remove("kick");

        }, 180);

        let range =
            type === "special" ? 140 : 95;

        if (distance() < range) {

            let damage;

            if (type === "punch") {
                damage = 6;
            }

            else if (type === "kick") {
                damage = 9;
            }

            else {
                damage = 16;
            }

            playerHP -= damage;

            player.classList.add("hit");

            setTimeout(() => {
                player.classList.remove("hit");
            }, 150);

            updateBars();

        }

    }

}


function updatePlayer() {

    if (keys["arrowleft"]) {
        playerX -= 5;
    }

    if (keys["arrowright"]) {
        playerX += 5;
    }

    if (keys["arrowup"]) {

        if (playerY === 0) {
            playerVelocityY = 15;
        }

    }

    if (keys["a"]) {
        attack("player", "punch");
    }

    if (keys["s"]) {
        attack("player", "kick");
    }

    if (keys["d"]) {
        attack("player", "special");
    }

    playerVelocityY -= 0.8;

    playerY += playerVelocityY;

    if (playerY < 0) {

        playerY = 0;
        playerVelocityY = 0;

    }

    playerX =
        clamp(
            playerX,
            20,
            game.clientWidth - 100
        );

}


function updateCPU() {

    let d = distance();

    if (d > 115) {

        if (playerX < cpuX) {
            cpuX -= 2.4;
        } else {
            cpuX += 2.4;
        }

    } else {

        cpuDirectionTimer++;

        if (cpuDirectionTimer % 55 === 0) {

            let r = Math.random();

            if (r < 0.5) {

                attack("cpu", "punch");

            } else if (r < 0.85) {

                attack("cpu", "kick");

            } else {

                attack("cpu", "special");

            }

        }

    }

    if (
        Math.random() < 0.002 &&
        cpuY === 0
    ) {

        cpuVelocityY = 15;

    }

    cpuVelocityY -= 0.8;

    cpuY += cpuVelocityY;

    if (cpuY < 0) {

        cpuY = 0;
        cpuVelocityY = 0;

    }

    cpuX =
        clamp(
            cpuX,
            20,
            game.clientWidth - 100
        );

}


function render() {

    player.style.left = playerX + "px";
    player.style.bottom =
        (118 + playerY) + "px";

    cpu.style.left = cpuX + "px";
    cpu.style.bottom =
        (118 + cpuY) + "px";

}


function gameOver(text) {

    running = false;

    message.innerHTML = text;

    message.style.display = "block";

    startScreen.style.display = "flex";

    startBtn.innerText = "REMATCH";

}


let lastSecond = Date.now();


function gameLoop() {

    if (!running) return;

    if (playerCooldown > 0) {
        playerCooldown--;
    }

    if (cpuCooldown > 0) {
        cpuCooldown--;
    }

    updatePlayer();
    updateCPU();

    render();

    if (playerHP <= 0) {

        gameOver("CPU WINS!");

        return;

    }

    if (cpuHP <= 0) {

        gameOver("PLAYER WINS!");

        return;

    }

    if (Date.now() - lastSecond >= 1000) {

        timer--;

        timerElement.innerText = timer;

        lastSecond = Date.now();

        if (timer <= 0) {

            if (playerHP > cpuHP) {
                gameOver("PLAYER WINS!");
            }

            else if (cpuHP > playerHP) {
                gameOver("CPU WINS!");
            }

            else {
                gameOver("DRAW!");
            }

            return;

        }

    }

    animationFrame =
        requestAnimationFrame(gameLoop);

}


startBtn.addEventListener(
    "click",
    startGame
);


function mobileHold(button, key) {

    button.addEventListener(
        "touchstart",
        function(e) {

            e.preventDefault();
            keys[key] = true;

        }
    );

    button.addEventListener(
        "touchend",
        function(e) {

            e.preventDefault();
            keys[key] = false;

        }
    );

}


mobileHold(
    document.getElementById("leftBtn"),
    "arrowleft"
);

mobileHold(
    document.getElementById("rightBtn"),
    "arrowright"
);

mobileHold(
    document.getElementById("jumpBtn"),
    "arrowup"
);

mobileHold(
    document.getElementById("punchBtn"),
    "a"
);

mobileHold(
    document.getElementById("kickBtn"),
    "s"
);

mobileHold(
    document.getElementById("specialBtn"),
    "d"
);

</script>

</body>
</html>
"""

components.html(
    game_html,
    height=720,
    scrolling=False
)
