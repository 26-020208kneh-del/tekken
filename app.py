import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="IRON FIGHTERS",
    page_icon="🥊",
    layout="wide",
)

st.markdown(
    """
    <style>
    .block-container {
        padding: 0.5rem 1rem 0;
        max-width: 1400px;
    }
    [data-testid="stHeader"] {
        background: transparent;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

GAME = r"""
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
    background: #08090d;
    color: white;
    font-family: Arial, sans-serif;
}

#game {
    position: relative;
    width: 100%;
    max-width: 1250px;
    height: 720px;
    margin: auto;
    overflow: hidden;
    border: 3px solid #343843;
    border-radius: 14px;
    background:
        radial-gradient(
            ellipse at 50% 25%,
            rgba(255,255,255,.15),
            transparent 30%
        ),
        linear-gradient(
            #182442 0%,
            #283d68 55%,
            #633c32 56%,
            #151515 57%,
            #090909 100%
        );
    box-shadow: 0 20px 70px rgba(0,0,0,.7);
}

#lights {
    position: absolute;
    top: -100px;
    left: 50%;
    width: 500px;
    height: 500px;
    transform: translateX(-50%);
    background: radial-gradient(
        ellipse,
        rgba(255,240,190,.22),
        transparent 68%
    );
}

.floor {
    position: absolute;
    left: 0;
    right: 0;
    bottom: 122px;
    height: 6px;
    background: #d9a64b;
    box-shadow: 0 0 20px rgba(255,190,80,.5);
}

.floor2 {
    position: absolute;
    left: 0;
    right: 0;
    bottom: 40px;
    height: 1px;
    background: rgba(255,255,255,.08);
}

#hud {
    position: absolute;
    z-index: 30;
    top: 18px;
    left: 22px;
    right: 22px;
    display: grid;
    grid-template-columns: 115px 1fr 70px 1fr 115px;
    gap: 12px;
    align-items: center;
}

.name {
    font-weight: 900;
    font-size: 19px;
}

.enemy-name {
    text-align: right;
}

.health {
    height: 28px;
    background: #101114;
    border: 2px solid #ddd;
    border-radius: 5px;
    overflow: hidden;
}

.hp {
    height: 100%;
    width: 100%;
    background: linear-gradient(
        #72ff9c,
        #19b85a
    );
    transition: width .12s;
}

#cpuHp {
    float: right;
    background: linear-gradient(
        #ff7575,
        #d21f35
    );
}

#timer {
    font-size: 36px;
    font-weight: 900;
    text-align: center;
}

#combo {
    position: absolute;
    z-index: 40;
    left: 50%;
    top: 150px;
    transform: translateX(-50%);
    font-size: 36px;
    font-weight: 900;
    color: #ffe66d;
    text-shadow: 0 4px 15px #000;
    opacity: 0;
    transition: .12s;
}

#combo.show {
    opacity: 1;
}

#stateText {
    position: absolute;
    z-index: 40;
    left: 50%;
    top: 205px;
    transform: translateX(-50%);
    font-size: 20px;
    font-weight: 800;
    color: white;
    opacity: 0;
}

.fighter {
    position: absolute;
    width: 82px;
    height: 185px;
    bottom: 125px;
    z-index: 10;
    transition: filter .05s;
}

.fighter * {
    position: absolute;
}

.head {
    width: 52px;
    height: 52px;
    top: 0;
    left: 15px;
    border-radius: 50%;
    z-index: 4;
}

.body {
    width: 48px;
    height: 72px;
    left: 17px;
    top: 45px;
    border-radius: 15px 15px 8px 8px;
    z-index: 3;
}

.arm {
    width: 17px;
    height: 72px;
    top: 47px;
    border-radius: 12px;
    transform-origin: top center;
    z-index: 2;
}

.arm1 {
    left: 7px;
    transform: rotate(20deg);
}

.arm2 {
    right: 5px;
    transform: rotate(-20deg);
}

.leg {
    width: 19px;
    height: 72px;
    top: 108px;
    border-radius: 12px;
    transform-origin: top center;
    z-index: 1;
}

.leg1 {
    left: 18px;
    transform: rotate(6deg);
}

.leg2 {
    right: 17px;
    transform: rotate(-6deg);
}

#player {
    left: 160px;
}

#player .head {
    background: #e9ae83;
    border: 4px solid #111;
}

#player .body,
#player .arm {
    background: #327cff;
}

#player .leg {
    background: #1946a4;
}

#cpu {
    left: calc(100% - 245px);
}

#cpu .head {
    background: #9a6448;
    border: 4px solid #111;
}

#cpu .body,
#cpu .arm {
    background: #df3030;
}

#cpu .leg {
    background: #941c28;
}

/* idle */
.fighter.idle .body {
    animation: idleBody .8s infinite ease-in-out;
}

@keyframes idleBody {
    50% {
        transform: translateY(-3px);
    }
}

/* walk */
.fighter.walk .leg1 {
    animation: walk1 .22s infinite alternate;
}

.fighter.walk .leg2 {
    animation: walk2 .22s infinite alternate;
}

@keyframes walk1 {
    to { transform: rotate(-18deg); }
}

@keyframes walk2 {
    to { transform: rotate(18deg); }
}

/* punch */
.fighter.punch .arm2 {
    animation: punch .20s ease-out;
}

@keyframes punch {
    0% {
        transform: rotate(-20deg);
    }
    35% {
        transform: rotate(-90deg);
        height: 88px;
    }
    100% {
        transform: rotate(-25deg);
    }
}

/* kick */
.fighter.kick .leg2 {
    animation: kick .28s ease-out;
}

@keyframes kick {
    0% {
        transform: rotate(-6deg);
    }
    35% {
        transform: rotate(78deg);
        height: 85px;
    }
    100% {
        transform: rotate(-6deg);
    }
}

/* special */
.fighter.special {
    filter: drop-shadow(
        0 0 16px #ffe15b
    );
}

.fighter.special .arm2 {
    animation: special .45s ease-out;
}

@keyframes special {
    0% {
        transform: rotate(-20deg);
    }
    45% {
        transform: rotate(-105deg);
        height: 100px;
    }
    100% {
        transform: rotate(-20deg);
    }
}

/* jump */
.fighter.jump .body {
    transform: rotate(-5deg);
}

/* guard */
.fighter.guard {
    filter: brightness(1.3);
}

.fighter.guard .arm1 {
    transform: rotate(55deg);
}

.fighter.guard .arm2 {
    transform: rotate(-55deg);
}

/* hit */
.fighter.hit {
    animation: hurt .14s linear;
    filter: brightness(2.1);
}

@keyframes hurt {
    50% {
        transform: translateX(-15px) rotate(-5deg);
    }
}

/* stun */
.fighter.stun {
    filter: brightness(1.7);
}

/* down */
.fighter.down {
    transform: rotate(88deg) translateY(45px);
    transform-origin: bottom center;
    opacity: .8;
}

/* direction */
.fighter.flip {
    transform: scaleX(-1);
}

#message {
    position: absolute;
    z-index: 50;
    left: 50%;
    top: 43%;
    transform: translate(-50%,-50%);
    font-size: 62px;
    font-weight: 1000;
    text-align: center;
    text-shadow: 0 5px 25px #000;
    display: none;
}

#start {
    position: absolute;
    z-index: 100;
    inset: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    background: rgba(0,0,0,.84);
}

#start h1 {
    font-size: 56px;
    margin: 0 0 8px;
}

#start p {
    color: #bbb;
    margin-bottom: 25px;
}

button {
    border: 0;
    border-radius: 8px;
    padding: 14px 35px;
    background: #df3030;
    color: white;
    font-size: 20px;
    font-weight: 900;
    cursor: pointer;
}

button:hover {
    background: #ff4848;
}

#controls {
    position: absolute;
    z-index: 60;
    bottom: 17px;
    left: 50%;
    transform: translateX(-50%);
    padding: 9px 18px;
    border-radius: 20px;
    background: rgba(0,0,0,.72);
    color: #ddd;
    white-space: nowrap;
}

#flash {
    position: absolute;
    z-index: 45;
    pointer-events: none;
    inset: 0;
    opacity: 0;
    background: white;
}

#flash.on {
    animation: flash .12s;
}

@keyframes flash {
    0% { opacity: .7; }
    100% { opacity: 0; }
}

@media(max-width:700px) {

    #game {
        height: 600px;
    }

    #hud {
        grid-template-columns: 65px 1fr 45px 1fr 65px;
        gap: 5px;
    }

    .name {
        font-size: 11px;
    }

    #timer {
        font-size: 24px;
    }

    #controls {
        white-space: normal;
        text-align: center;
        font-size: 11px;
    }

}
</style>
</head>

<body>

<div id="game">

<div id="lights"></div>
<div class="floor"></div>
<div class="floor2"></div>

<div id="hud">

    <div class="name">PLAYER</div>

    <div class="health">
        <div id="playerHp" class="hp"></div>
    </div>

    <div id="timer">60</div>

    <div class="health">
        <div id="cpuHp" class="hp"></div>
    </div>

    <div class="name enemy-name">CPU</div>

</div>

<div id="combo">3 HIT COMBO</div>
<div id="stateText">COUNTER</div>

<div id="player" class="fighter idle">
    <div class="head"></div>
    <div class="body"></div>
    <div class="arm arm1"></div>
    <div class="arm arm2"></div>
    <div class="leg leg1"></div>
    <div class="leg leg2"></div>
</div>

<div id="cpu" class="fighter idle">
    <div class="head"></div>
    <div class="body"></div>
    <div class="arm arm1"></div>
    <div class="arm arm2"></div>
    <div class="leg leg1"></div>
    <div class="leg leg2"></div>
</div>

<div id="flash"></div>

<div id="message"></div>

<div id="controls">
    ← → 이동　↑ 점프　A 펀치　S 킥　D 필살기　　가만히 있으면 자동 가드
</div>

<div id="start">

    <h1>IRON FIGHTERS</h1>

    <p>
        2D Fighting Game
    </p>

    <button id="startButton">
        FIGHT!
    </button>

</div>

</div>

<script>

const game = document.getElementById("game");

const playerEl = document.getElementById("player");
const cpuEl = document.getElementById("cpu");

const playerHpEl = document.getElementById("playerHp");
const cpuHpEl = document.getElementById("cpuHp");

const timerEl = document.getElementById("timer");

const comboEl = document.getElementById("combo");
const stateText = document.getElementById("stateText");

const messageEl = document.getElementById("message");
const startEl = document.getElementById("start");
const startButton = document.getElementById("startButton");

const flashEl = document.getElementById("flash");

let running = false;

const keys = {};

let lastTime = performance.now();

let timer = 60;
let timerAccumulator = 0;

let player;
let cpu;

let particles = [];

const ATTACKS = {

    punch: {
        startup: 7,
        active: 5,
        recovery: 15,
        range: 105,
        damage: 6,
        hitstun: 16,
        knockback: 7,
        guardDamage: 1
    },

    kick: {
        startup: 11,
        active: 6,
        recovery: 20,
        range: 125,
        damage: 10,
        hitstun: 22,
        knockback: 12,
        guardDamage: 2
    },

    special: {
        startup: 18,
        active: 9,
        recovery: 32,
        range: 165,
        damage: 19,
        hitstun: 34,
        knockback: 24,
        guardDamage: 4
    }

};


function fighter(x, isCPU) {

    return {

        x: x,
        y: 0,

        vx: 0,
        vy: 0,

        hp: 100,

        facing: isCPU ? -1 : 1,

        state: "idle",

        stateTimer: 0,

        attack: null,

        attackFrame: 0,

        hitstun: 0,

        blockstun: 0,

        knockdown: 0,

        combo: 0,

        comboTimer: 0,

        isCPU: isCPU,

        aiTimer: 0,

        aiAttackTimer: 0,

        aiBlockTimer: 0

    };

}


function resetGame() {

    player = fighter(170, false);

    cpu = fighter(game.clientWidth - 250, true);

    timer = 60;
    timerAccumulator = 0;

    running = true;

    messageEl.style.display = "none";

    startEl.style.display = "none";

    lastTime = performance.now();

    requestAnimationFrame(loop);

}


function clamp(v, min, max) {

    return Math.max(
        min,
        Math.min(max, v)
    );

}


function dist(a,b) {

    return Math.abs(
        a.x - b.x
    );

}


function facingOpponent(f, opponent) {

    if (opponent.x > f.x) {
        f.facing = 1;
    } else {
        f.facing = -1;
    }

}


function isAttacking(f) {

    return f.attack !== null;

}


function isBusy(f) {

    return (
        f.hitstun > 0 ||
        f.blockstun > 0 ||
        f.knockdown > 0
    );

}


function autoGuard(f, opponent) {

    if (isBusy(f)) {
        return false;
    }

    if (f.attack) {
        return false;
    }

    if (f.isCPU) {

        return f.aiBlockTimer > 0;

    }

    const near = dist(f, opponent) < 185;

    const movement =
        keys["arrowleft"] ||
        keys["arrowright"] ||
        keys["arrowup"] ||
        keys["a"] ||
        keys["s"] ||
        keys["d"];

    return near && !movement;

}


function startAttack(f, type) {

    if (!running) {
        return;
    }

    if (isBusy(f)) {
        return;
    }

    if (f.attack) {
        return;
    }

    const a = ATTACKS[type];

    f.attack = type;
    f.attackFrame = 0;

    f.stateTimer =
        a.startup +
        a.active +
        a.recovery;

}


function attackActive(f) {

    if (!f.attack) {
        return false;
    }

    const a = ATTACKS[f.attack];

    return (
        f.attackFrame >= a.startup &&
        f.attackFrame <
        a.startup + a.active
    );

}


function canHit(attacker, defender) {

    const a = ATTACKS[attacker.attack];

    if (!a) {
        return false;
    }

    const d = dist(
        attacker,
        defender
    );

    if (d > a.range) {
        return false;
    }

    if (Math.abs(
        attacker.y - defender.y
    ) > 85) {
        return false;
    }

    const direction =
        Math.sign(
            defender.x -
            attacker.x
        );

    return direction === attacker.facing;

}


function spawnHit(x, y, color) {

    for (let i = 0; i < 14; i++) {

        particles.push({

            x: x,
            y: y,

            vx:
                (Math.random() - .5) * 11,

            vy:
                (Math.random() - .5) * 11,

            life: 25,

            color: color

        });

    }

}


function showState(text) {

    stateText.innerText = text;

    stateText.style.opacity = "1";

    setTimeout(() => {

        stateText.style.opacity = "0";

    }, 400);

}


function showCombo(f) {

    if (f.combo < 2) {
        return;
    }

    comboEl.innerText =
        f.combo + " HIT COMBO";

    comboEl.classList.add("show");

    clearTimeout(showCombo.timeout);

    showCombo.timeout =
        setTimeout(() => {

            comboEl.classList.remove("show");

        }, 650);

}


function hit(attacker, defender) {

    const a =
        ATTACKS[attacker.attack];

    if (!a) {
        return;
    }

    if (!canHit(attacker, defender)) {
        return;
    }

    if (defender.hitstun > 0) {
        return;
    }

    const guarding =
        autoGuard(
            defender,
            attacker
        );

    if (guarding) {

        const damage =
            Math.max(
                1,
                Math.floor(
                    a.guardDamage
                )
            );

        defender.hp -= damage;

        defender.blockstun = 12;

        defender.vx =
            attacker.facing * 2;

        defender.state = "guard";

        spawnHit(
            defender.x,
            defender.y + 90,
            "#8fdcff"
        );

        showState("GUARD");

        attacker.combo = 0;

        return;
    }

    defender.hp -= a.damage;

    defender.hitstun =
        a.hitstun;

    defender.vx =
        attacker.facing *
        a.knockback;

    defender.state = "hit";

    attacker.combo++;

    attacker.comboTimer = 45;

    spawnHit(
        defender.x,
        defender.y + 85,
        "#ffe15b"
    );

    flashEl.classList.remove("on");

    void flashEl.offsetWidth;

    flashEl.classList.add("on");

    showCombo(attacker);

    if (
        a.knockback >= 20
    ) {

        defender.knockdown = 38;

    }

}


function updateAttack(f, opponent) {

    if (!f.attack) {
        return;
    }

    f.attackFrame++;

    if (
        attackActive(f)
    ) {

        if (!f.attackHasHit) {

            hit(
                f,
                opponent
            );

            f.attackHasHit = true;

        }

    }

    const a =
        ATTACKS[f.attack];

    const total =
        a.startup +
        a.active +
        a.recovery;

    if (
        f.attackFrame >= total
    ) {

        f.attack = null;

        f.attackFrame = 0;

        f.attackHasHit = false;

    }

}


function updatePlayer() {

    if (!running) {
        return;
    }

    facingOpponent(
        player,
        cpu
    );

    if (
        player.knockdown > 0
    ) {

        player.knockdown--;

        player.vx *= .90;

        return;

    }

    if (
        player.hitstun > 0
    ) {

        player.hitstun--;

        player.vx *= .88;

        player.x += player.vx;

        return;

    }

    if (
        player.blockstun > 0
    ) {

        player.blockstun--;

        player.vx *= .85;

        player.x += player.vx;

        return;

    }

    if (player.attack) {

        updateAttack(
            player,
            cpu
        );

        return;

    }

    let moving = false;

    if (keys["arrowleft"]) {

        player.x -= 5;

        moving = true;

    }

    if (keys["arrowright"]) {

        player.x += 5;

        moving = true;

    }

    if (
        keys["arrowup"] &&
        player.y === 0
    ) {

        player.vy = 14;

    }

    if (keys["a"]) {

        startAttack(
            player,
            "punch"
        );

    }

    else if (keys["s"]) {

        startAttack(
            player,
            "kick"
        );

    }

    else if (keys["d"]) {

        startAttack(
            player,
            "special"
        );

    }

    player.vy -= .75;

    player.y += player.vy;

    if (player.y < 0) {

        player.y = 0;

        player.vy = 0;

    }

    player.x =
        clamp(
            player.x,
            25,
            game.clientWidth - 105
        );

    player.state =
        player.y > 0
        ? "jump"
        : moving
        ? "walk"
        : autoGuard(player,cpu)
        ? "guard"
        : "idle";

}


function updateCPU() {

    if (!running) {
        return;
    }

    facingOpponent(
        cpu,
        player
    );

    if (
        cpu.knockdown > 0
    ) {

        cpu.knockdown--;

        cpu.vx *= .90;

        return;

    }

    if (
        cpu.hitstun > 0
    ) {

        cpu.hitstun--;

        cpu.vx *= .88;

        cpu.x += cpu.vx;

        return;

    }

    if (
        cpu.blockstun > 0
    ) {

        cpu.blockstun--;

        cpu.vx *= .85;

        cpu.x += cpu.vx;

        return;

    }

    if (cpu.attack) {

        updateAttack(
            cpu,
            player
        );

        return;

    }

    const d =
        dist(cpu,player);

    cpu.aiTimer++;

    /*
       CPU가 공격을 맞을 것 같으면
       가끔 자동으로 가드한다.
    */

    if (
        d < 190 &&
        Math.random() < .018
    ) {

        cpu.aiBlockTimer =
            30 +
            Math.floor(
                Math.random() * 25
            );

    }

    if (
        cpu.aiBlockTimer > 0
    ) {

        cpu.aiBlockTimer--;

        cpu.state = "guard";

        return;

    }

    if (d > 125) {

        if (
            player.x < cpu.x
        ) {

            cpu.x -= 2.5;

        } else {

            cpu.x += 2.5;

        }

        cpu.state = "walk";

    }

    else {

        const chance =
            Math.random();

        if (
            cpu.aiTimer % 30 === 0
        ) {

            if (chance < .48) {

                startAttack(
                    cpu,
                    "punch"
                );

            }

            else if (
                chance < .83
            ) {

                startAttack(
                    cpu,
                    "kick"
                );

            }

            else {

                startAttack(
                    cpu,
                    "special"
                );

            }

        }

        cpu.state =
            autoGuard(cpu,player)
            ? "guard"
            : "idle";

    }

    cpu.x =
        clamp(
            cpu.x,
            25,
            game.clientWidth - 105
        );

}


function updatePhysics() {

    player.x += player.vx;
    cpu.x += cpu.vx;

    player.vx *= .85;
    cpu.vx *= .85;

    player.x =
        clamp(
            player.x,
            25,
            game.clientWidth - 105
        );

    cpu.x =
        clamp(
            cpu.x,
            25,
            game.clientWidth - 105
        );

}


function updateCombos() {

    if (player.comboTimer > 0) {

        player.comboTimer--;

    } else {

        player.combo = 0;

    }

    if (cpu.comboTimer > 0) {

        cpu.comboTimer--;

    } else {

        cpu.combo = 0;

    }

}


function renderFighter(f, el) {

    el.style.left =
        f.x + "px";

    el.style.bottom =
        (125 + f.y) + "px";

    el.className =
        "fighter " +
        f.state;

    if (f.facing < 0) {

        el.classList.add("flip");

    }

    if (f.attack) {

        el.classList.add(
            f.attack
        );

    }

    if (f.hitstun > 0) {

        el.classList.add("stun");

    }

}


function renderParticles() {

    particles.forEach(
        p => {

            p.x += p.vx;
            p.y += p.vy;

            p.vy += .35;

            p.life--;

        }
    );

    particles =
        particles.filter(
            p => p.life > 0
        );

}


function render() {

    renderFighter(
        player,
        playerEl
    );

    renderFighter(
        cpu,
        cpuEl
    );

    playerHpEl.style.width =
        Math.max(
            0,
            player.hp
        ) + "%";

    cpuHpEl.style.width =
        Math.max(
            0,
            cpu.hp
        ) + "%";

    timerEl.innerText =
        timer;

}


function gameOver(text) {

    running = false;

    messageEl.innerText =
        text;

    messageEl.style.display =
        "block";

    startEl.style.display =
        "flex";

    startButton.innerText =
        "REMATCH";

}


function updateTimer(dt) {

    timerAccumulator += dt;

    if (
        timerAccumulator >= 1000
    ) {

        timerAccumulator -= 1000;

        timer--;

        if (timer <= 0) {

            if (
                player.hp >
                cpu.hp
            ) {

                gameOver(
                    "PLAYER WINS!"
                );

            }

            else if (
                cpu.hp >
                player.hp
            ) {

                gameOver(
                    "CPU WINS!"
                );

            }

            else {

                gameOver(
                    "DRAW!"
                );

            }

        }

    }

}


function checkGameOver() {

    if (
        player.hp <= 0
    ) {

        player.state =
            "down";

        gameOver(
            "CPU WINS!"
        );

    }

    else if (
        cpu.hp <= 0
    ) {

        cpu.state =
            "down";

        gameOver(
            "PLAYER WINS!"
        );

    }

}


function loop(now) {

    if (!running) {
        return;
    }

    const dt =
        Math.min(
            40,
            now - lastTime
        );

    lastTime = now;

    updatePlayer();
    updateCPU();

    updatePhysics();

    updateCombos();

    updateTimer(dt);

    renderParticles();

    render();

    checkGameOver();

    if (running) {

        requestAnimationFrame(
            loop
        );

    }

}


document.addEventListener(
    "keydown",
    e => {

        keys[
            e.key.toLowerCase()
        ] = true;

        if (
            [
                "arrowleft",
                "arrowright",
                "arrowup",
                " "
            ].includes(
                e.key.toLowerCase()
            )
        ) {

            e.preventDefault();

        }

    }
);


document.addEventListener(
    "keyup",
    e => {

        keys[
            e.key.toLowerCase()
        ] = false;

    }
);


startButton.addEventListener(
    "click",
    resetGame
);


</script>

</body>
</html>
"""

components.html(
    GAME,
    height=750,
    scrolling=False
)
