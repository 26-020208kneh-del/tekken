import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="IRON FIGHTERS",
    page_icon="🥊",
    layout="wide",
)

st.markdown("""
<style>
.block-container {
    padding: 0.2rem 0.4rem;
    max-width: 1400px;
}
[data-testid="stHeader"] {
    background: transparent;
}
</style>
""", unsafe_allow_html=True)


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
    background: #07080c;
    color: white;
    font-family: Arial, sans-serif;
    overflow: hidden;
}

#game {
    position: relative;
    width: 100%;
    max-width: 1280px;
    height: 720px;
    margin: auto;
    overflow: hidden;

    border: 2px solid #3b404c;
    border-radius: 14px;

    background:
        radial-gradient(
            ellipse at 50% 25%,
            rgba(255,255,255,.13),
            transparent 38%
        ),
        linear-gradient(
            #111c38 0%,
            #294775 53%,
            #633d2b 54%,
            #1c1c1c 56%,
            #090909 100%
        );
}

#arenaGlow {
    position: absolute;
    left: 50%;
    top: -180px;
    width: 650px;
    height: 650px;
    transform: translateX(-50%);

    background:
        radial-gradient(
            ellipse,
            rgba(255,220,150,.18),
            transparent 70%
        );
}

#floor {
    position: absolute;
    left: 0;
    right: 0;
    bottom: 118px;
    height: 5px;

    background: #d8a74b;
    box-shadow: 0 0 20px rgba(255,190,70,.55);
}

#hud {
    position: absolute;
    z-index: 50;

    left: 20px;
    right: 20px;
    top: 15px;

    display: grid;

    grid-template-columns:
        100px
        1fr
        65px
        1fr
        100px;

    align-items: center;
    gap: 9px;
}

.name {
    font-size: 17px;
    font-weight: 900;
}

.enemyName {
    text-align: right;
}

.health {
    height: 28px;

    border: 2px solid #eee;
    border-radius: 4px;

    overflow: hidden;

    background: #111;
}

.healthInner {
    height: 100%;
    width: 100%;

    background:
        linear-gradient(
            #72ff9a,
            #17a956
        );

    transition: width .12s;
}

#cpuHp {
    float: right;

    background:
        linear-gradient(
            #ff7272,
            #d51f38
        );
}

#timer {
    font-size: 34px;
    font-weight: 1000;
    text-align: center;
}

#combo {
    position: absolute;
    z-index: 80;

    left: 50%;
    top: 115px;

    transform: translateX(-50%);

    font-size: 40px;
    font-weight: 1000;

    color: #ffe05d;

    text-shadow:
        0 3px 0 #704400,
        0 6px 20px #000;

    opacity: 0;
}

#combo.show {
    opacity: 1;
}

#hitText {
    position: absolute;
    z-index: 80;

    left: 50%;
    top: 170px;

    transform: translateX(-50%);

    font-size: 21px;
    font-weight: 1000;

    opacity: 0;
}

#hitText.show {
    opacity: 1;
}

#message {
    position: absolute;
    z-index: 100;

    left: 50%;
    top: 43%;

    transform: translate(-50%, -50%);

    font-size: 65px;
    font-weight: 1000;

    text-shadow:
        0 5px 30px #000;

    display: none;

    text-align: center;
}

#hint {
    position: absolute;
    z-index: 60;

    left: 50%;
    bottom: 70px;

    transform: translateX(-50%);

    padding: 8px 18px;

    background: rgba(0,0,0,.72);

    border-radius: 20px;

    color: #ddd;

    font-size: 13px;

    white-space: nowrap;
}


/* =========================
   SKILL BAR
========================= */

#skills {
    position: absolute;
    z-index: 70;

    left: 50%;
    bottom: 15px;

    transform: translateX(-50%);

    display: flex;

    gap: 8px;
}

.skill {
    position: relative;

    width: 68px;
    height: 42px;

    border: 2px solid #aaa;
    border-radius: 6px;

    overflow: hidden;

    background: #15161b;

    text-align: center;

    font-weight: 900;
}

.skillKey {
    position: relative;
    z-index: 3;

    line-height: 38px;

    font-size: 16px;
}

.skillFill {
    position: absolute;

    left: 0;
    bottom: 0;

    width: 100%;
    height: 0%;

    background:
        linear-gradient(
            #ff6464,
            #a80018
        );

    opacity: .85;
}

.skill.ready {
    border-color: #69ff9d;

    box-shadow:
        0 0 12px
        rgba(80,255,150,.35);
}

.skill.cooling {
    border-color: #ff5b5b;
}

#flash {
    position: absolute;
    z-index: 90;

    inset: 0;

    pointer-events: none;

    opacity: 0;
    background: white;
}

#flash.active {
    animation: screenFlash .12s;
}

@keyframes screenFlash {

    0% {
        opacity: .55;
    }

    100% {
        opacity: 0;
    }
}

#start {
    position: absolute;
    z-index: 120;

    inset: 0;

    display: flex;

    flex-direction: column;

    align-items: center;
    justify-content: center;

    background:
        radial-gradient(
            ellipse,
            rgba(35,40,70,.55),
            rgba(0,0,0,.95)
        );
}

#start h1 {
    margin: 0;

    font-size: 58px;

    letter-spacing: 4px;
}

#start p {
    color: #aaa;

    margin: 10px 0 28px;
}

button {
    border: 0;

    border-radius: 7px;

    padding: 14px 42px;

    background:
        linear-gradient(
            #f23b42,
            #a81726
        );

    color: white;

    font-size: 20px;

    font-weight: 900;

    cursor: pointer;
}

button:hover {
    filter: brightness(1.15);
}

canvas {
    position: absolute;

    inset: 0;

    width: 100%;
    height: 100%;
}

@media(max-width:700px) {

    #game {
        height: 620px;
    }

    #hud {
        grid-template-columns:
            50px
            1fr
            42px
            1fr
            50px;
    }

    .name {
        font-size: 10px;
    }

    #timer {
        font-size: 23px;
    }

    #hint {
        font-size: 9px;

        white-space: normal;

        text-align: center;

        width: 90%;
    }

    #start h1 {
        font-size: 35px;
    }

    .skill {
        width: 55px;
        height: 36px;
    }

    .skillKey {
        line-height: 32px;
    }
}
</style>
</head>

<body>

<div id="game">

    <div id="arenaGlow"></div>

    <canvas id="canvas"></canvas>

    <div id="floor"></div>

    <!-- HUD -->

    <div id="hud">

        <div class="name">
            PLAYER
        </div>

        <div class="health">
            <div
                id="playerHp"
                class="healthInner">
            </div>
        </div>

        <div id="timer">
            60
        </div>

        <div class="health">
            <div
                id="cpuHp"
                class="healthInner">
            </div>
        </div>

        <div class="name enemyName">
            CPU
        </div>

    </div>


    <div id="combo">
        3 HIT COMBO
    </div>


    <div id="hitText">
        MIDDLE
    </div>


    <div id="flash"></div>


    <div id="message"></div>


    <!-- SKILLS -->

    <div id="skills">

        <div
            id="skillHigh"
            class="skill ready">

            <div class="skillKey">
                A
            </div>

            <div
                id="fillHigh"
                class="skillFill">
            </div>

        </div>


        <div
            id="skillMid"
            class="skill ready">

            <div class="skillKey">
                S
            </div>

            <div
                id="fillMid"
                class="skillFill">
            </div>

        </div>


        <div
            id="skillLow"
            class="skill ready">

            <div class="skillKey">
                D
            </div>

            <div
                id="fillLow"
                class="skillFill">
            </div>

        </div>


        <div
            id="skillLauncher"
            class="skill ready">

            <div class="skillKey">
                F
            </div>

            <div
                id="fillLauncher"
                class="skillFill">
            </div>

        </div>

    </div>


    <div id="hint">

        ← → 이동　
        ↓ 앉기　
        A 상단　
        S 중단　
        D 하단　
        F 런처　
        │ 가만히 있으면 자동 가드

    </div>


    <div id="start">

        <h1>
            IRON FIGHTERS
        </h1>

        <p>
            HIGH / MID / LOW FIGHTING SYSTEM
        </p>

        <button id="startButton">
            FIGHT!
        </button>

    </div>

</div>


<script>

/* =========================================================
   CANVAS
========================================================= */

const game =
    document.getElementById("game");

const canvas =
    document.getElementById("canvas");

const ctx =
    canvas.getContext("2d");


let W = 1200;
let H = 720;


function resize() {

    const rect =
        game.getBoundingClientRect();

    W = rect.width;
    H = rect.height;

    canvas.width =
        Math.floor(
            W * devicePixelRatio
        );

    canvas.height =
        Math.floor(
            H * devicePixelRatio
        );

    canvas.style.width =
        W + "px";

    canvas.style.height =
        H + "px";

    ctx.setTransform(
        devicePixelRatio,
        0,
        0,
        devicePixelRatio,
        0,
        0
    );
}


window.addEventListener(
    "resize",
    resize
);

resize();


/* =========================================================
   INPUT
========================================================= */

const keys = {};


document.addEventListener(
    "keydown",
    function(e) {

        keys[
            e.key.toLowerCase()
        ] = true;

        if (
            [
                "arrowleft",
                "arrowright",
                "arrowup",
                "arrowdown",
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
    function(e) {

        keys[
            e.key.toLowerCase()
        ] = false;
    }
);


/* =========================================================
   ATTACK DATA
========================================================= */

const ATTACKS = {

    high: {

        level: "high",

        startup: 6,

        active: 4,

        recovery: 13,

        range: 112,

        damage: 6,

        hitstun: 16,

        guardstun: 8,

        knockback: 5,

        comboScale: .94,

        cooldown: 12
    },


    mid: {

        level: "mid",

        startup: 10,

        active: 5,

        recovery: 18,

        range: 128,

        damage: 9,

        hitstun: 22,

        guardstun: 11,

        knockback: 9,

        comboScale: .93,

        cooldown: 18
    },


    low: {

        level: "low",

        startup: 13,

        active: 6,

        recovery: 21,

        range: 118,

        damage: 8,

        hitstun: 20,

        guardstun: 9,

        knockback: 6,

        comboScale: .92,

        cooldown: 22
    },


    launcher: {

        level: "mid",

        startup: 17,

        active: 7,

        recovery: 27,

        range: 125,

        damage: 12,

        hitstun: 34,

        guardstun: 13,

        knockback: 8,

        launcher: true,

        comboScale: .88,

        cooldown: 45
    }

};


/* =========================================================
   FIGHTER
========================================================= */

function makeFighter(x, cpu) {

    return {

        x: x,

        y: 0,

        vx: 0,

        vy: 0,

        hp: 100,

        facing: cpu ? -1 : 1,

        cpu: cpu,

        state: "idle",

        attack: null,

        attackFrame: 0,

        attackConnected: false,

        hitstun: 0,

        blockstun: 0,

        knockdown: 0,

        airborne: false,

        combo: 0,

        comboTimer: 0,

        animationTime: 0,

        aiTimer: 0,

        aiGuard: 0,

        aiAttackCooldown: 0,

        lastHitLevel: "",

        lastAttack: null,

        cooldowns: {

            high: 0,

            mid: 0,

            low: 0,

            launcher: 0
        }
    };
}


/* =========================================================
   GAME STATE
========================================================= */

let player;

let cpu;

let running = false;

let gameTime = 60;

let secondAccumulator = 0;

let lastTime = 0;


/* =========================================================
   START
========================================================= */

function startGame() {

    player =
        makeFighter(
            180,
            false
        );

    cpu =
        makeFighter(
            W - 260,
            true
        );

    gameTime = 60;

    secondAccumulator = 0;

    running = true;

    messageEl.style.display =
        "none";

    startEl.style.display =
        "none";

    lastTime =
        performance.now();

    requestAnimationFrame(
        loop
    );
}


/* =========================================================
   DOM
========================================================= */

const playerHp =
    document.getElementById(
        "playerHp"
    );

const cpuHp =
    document.getElementById(
        "cpuHp"
    );

const timerEl =
    document.getElementById(
        "timer"
    );

const comboEl =
    document.getElementById(
        "combo"
    );

const hitTextEl =
    document.getElementById(
        "hitText"
    );

const messageEl =
    document.getElementById(
        "message"
    );

const startEl =
    document.getElementById(
        "start"
    );

const startButton =
    document.getElementById(
        "startButton"
    );

const flashEl =
    document.getElementById(
        "flash"
    );


const skillElements = {

    high: {
        box:
            document.getElementById(
                "skillHigh"
            ),
        fill:
            document.getElementById(
                "fillHigh"
            )
    },

    mid: {
        box:
            document.getElementById(
                "skillMid"
            ),
        fill:
            document.getElementById(
                "fillMid"
            )
    },

    low: {
        box:
            document.getElementById(
                "skillLow"
            ),
        fill:
            document.getElementById(
                "fillLow"
            )
    },

    launcher: {
        box:
            document.getElementById(
                "skillLauncher"
            ),
        fill:
            document.getElementById(
                "fillLauncher"
            )
    }
};


/* =========================================================
   UTILITY
========================================================= */

function clamp(
    value,
    min,
    max
) {

    return Math.max(
        min,
        Math.min(
            max,
            value
        )
    );
}


function distance(a, b) {

    return Math.abs(
        a.x - b.x
    );
}


function busy(f) {

    return (
        f.hitstun > 0 ||
        f.blockstun > 0 ||
        f.knockdown > 0
    );
}


function faceOpponent(
    fighter,
    opponent
) {

    fighter.facing =
        opponent.x >= fighter.x
        ? 1
        : -1;
}


/* =========================================================
   CROUCH / GUARD
========================================================= */

function isCrouching(f) {

    if (f.cpu) {

        return (
            f.state === "crouch"
        );
    }

    return keys["arrowdown"];
}


function canAutoGuard(
    f,
    opponent
) {

    if (busy(f)) {
        return false;
    }

    if (f.attack) {
        return false;
    }

    if (f.airborne) {
        return false;
    }

    if (f.cpu) {

        return f.aiGuard > 0;
    }

    const close =
        distance(
            f,
            opponent
        ) < 190;

    const moving =
        keys["arrowleft"] ||
        keys["arrowright"] ||
        keys["arrowdown"] ||
        keys["arrowup"] ||
        keys["a"] ||
        keys["s"] ||
        keys["d"] ||
        keys["f"];

    return close && !moving;
}


/* =========================================================
   ATTACK START
========================================================= */

function startAttack(
    f,
    type
) {

    if (!running) {
        return false;
    }

    if (busy(f)) {
        return false;
    }

    if (f.attack) {
        return false;
    }


    /* =========================
       COOLDOWN CHECK
    ========================= */

    if (
        f.cooldowns[type] > 0
    ) {

        if (!f.cpu) {

            showHitText(
                "COOLDOWN " +
                Math.ceil(
                    f.cooldowns[type] / 60
                ),
                "#ff6666"
            );
        }

        return false;
    }


    f.attack = type;

    f.attackFrame = 0;

    f.attackConnected = false;

    f.lastAttack = type;

    return true;
}


/* =========================================================
   ATTACK STATE
========================================================= */

function attackActive(f) {

    if (!f.attack) {
        return false;
    }

    const a =
        ATTACKS[
            f.attack
        ];

    return (
        f.attackFrame >=
        a.startup &&

        f.attackFrame <
        a.startup +
        a.active
    );
}


function attackFinished(f) {

    if (!f.attack) {
        return false;
    }

    const a =
        ATTACKS[
            f.attack
        ];

    return (
        f.attackFrame >=
        a.startup +
        a.active +
        a.recovery
    );
}


/* =========================================================
   RANGE
========================================================= */

function isInsideRange(
    attacker,
    defender
) {

    const a =
        ATTACKS[
            attacker.attack
        ];

    if (!a) {
        return false;
    }

    if (
        distance(
            attacker,
            defender
        ) > a.range
    ) {

        return false;
    }

    const direction =
        Math.sign(
            defender.x -
            attacker.x
        );

    if (
        direction !==
        attacker.facing
    ) {

        return false;
    }

    if (
        Math.abs(
            attacker.y -
            defender.y
        ) > 105
    ) {

        return false;
    }

    return true;
}


/* =========================================================
   GUARD LOGIC
========================================================= */

function isGuarding(
    defender,
    attack
) {

    const crouching =
        isCrouching(defender);


    /*
       HIGH

       서서 가드
       앉으면 회피
    */

    if (
        attack.level === "high"
    ) {

        if (crouching) {

            return "evade";
        }

        return true;
    }


    /*
       MID

       서서/앉아서 둘 다 가드
    */

    if (
        attack.level === "mid"
    ) {

        return true;
    }


    /*
       LOW

       앉아서만 가드
    */

    if (
        attack.level === "low"
    ) {

        return crouching;
    }


    return false;
}


/* =========================================================
   HIT TEXT
========================================================= */

function showHitText(
    text,
    color
) {

    hitTextEl.innerText =
        text;

    hitTextEl.style.color =
        color;

    hitTextEl.classList.add(
        "show"
    );

    clearTimeout(
        showHitText.timer
    );

    showHitText.timer =
        setTimeout(
            function() {

                hitTextEl.classList.remove(
                    "show"
                );

            },
            300
        );
}


/* =========================================================
   COMBO
========================================================= */

function showCombo(fighter) {

    if (
        fighter.combo < 2
    ) {

        return;
    }

    comboEl.innerText =
        fighter.combo +
        " HIT COMBO";

    comboEl.classList.add(
        "show"
    );

    clearTimeout(
        showCombo.timer
    );

    showCombo.timer =
        setTimeout(
            function() {

                comboEl.classList.remove(
                    "show"
                );

            },
            650
        );
}


/* =========================================================
   SCREEN FLASH
========================================================= */

function flashScreen() {

    flashEl.classList.remove(
        "active"
    );

    void flashEl.offsetWidth;

    flashEl.classList.add(
        "active"
    );
}


/* =========================================================
   HIT RESOLUTION
========================================================= */

function resolveHit(
    attacker,
    defender
) {

    const a =
        ATTACKS[
            attacker.attack
        ];

    if (!a) {
        return;
    }

    if (
        !isInsideRange(
            attacker,
            defender
        )
    ) {

        return;
    }

    if (
        attacker.attackConnected
    ) {

        return;
    }

    attacker.attackConnected =
        true;


    const guard =
        isGuarding(
            defender,
            a
        );


    /* =========================
       HIGH CRUSH
    ========================= */

    if (
        guard === "evade"
    ) {

        showHitText(
            "HIGH CRUSH!",
            "#76d9ff"
        );

        attacker.combo = 0;

        return;
    }


    /* =========================
       BLOCK
    ========================= */

    if (
        guard === true
    ) {

        const damage =
            Math.max(
                1,
                Math.floor(
                    a.damage * .18
                )
            );

        defender.hp -= damage;

        defender.blockstun =
            a.guardstun;

        defender.vx =
            attacker.facing * 2;

        defender.state =
            "guard";

        defender.lastHitLevel =
            a.level;

        showHitText(
            a.level.toUpperCase() +
            " GUARD",
            "#71d7ff"
        );

        spawnImpact(
            defender.x,
            defender.y + 80,
            "#62caff"
        );

        attacker.combo = 0;

        return;
    }


    /* =========================
       REAL HIT
    ========================= */

    let damage =
        a.damage;


    /*
       공중 콤보 데미지 감소
    */

    if (
        defender.airborne
    ) {

        damage *=
            Math.pow(
                a.comboScale,
                attacker.combo
            );
    }


    damage =
        Math.max(
            1,
            Math.round(
                damage
            )
        );


    defender.hp -= damage;

    defender.hitstun =
        a.hitstun;

    defender.blockstun = 0;

    defender.vx =
        attacker.facing *
        a.knockback;

    defender.lastHitLevel =
        a.level;

    attacker.combo++;

    attacker.comboTimer =
        55;

    defender.state =
        "hit";


    /* =========================
       LAUNCHER
    ========================= */

    if (
        a.launcher &&
        !defender.airborne
    ) {

        defender.airborne =
            true;

        defender.vy =
            13;

        defender.y =
            1;

        defender.hitstun =
            42;

        showHitText(
            "LAUNCH!",
            "#ffdf4e"
        );

    }
    else {

        showHitText(
            a.level.toUpperCase(),
            "#ffe36a"
        );
    }


    spawnImpact(
        defender.x,
        defender.y + 85,
        "#ffe36a"
    );

    flashScreen();

    showCombo(
        attacker
    );
}


/* =========================================================
   ATTACK UPDATE
========================================================= */

function updateAttack(
    f,
    opponent
) {

    if (!f.attack) {
        return;
    }

    f.attackFrame++;


    if (
        attackActive(f)
    ) {

        resolveHit(
            f,
            opponent
        );
    }


    /*
       공격 종료

       여기서 해당 기술의 쿨타임을 시작
    */

    if (
        attackFinished(f)
    ) {

        const usedAttack =
            f.attack;

        const attackData =
            ATTACKS[
                usedAttack
            ];


        f.cooldowns[
            usedAttack
        ] =
            attackData.cooldown;


        f.attack = null;

        f.attackFrame = 0;

        f.attackConnected =
            false;
    }
}


/* =========================================================
   COOLDOWN UPDATE
========================================================= */

function updateCooldowns(f) {

    if (!f) {
        return;
    }

    for (
        const type in f.cooldowns
    ) {

        if (
            f.cooldowns[type] > 0
        ) {

            f.cooldowns[type]--;
        }
    }
}


/* =========================================================
   PARTICLES
========================================================= */

let particles = [];


function spawnImpact(
    x,
    y,
    color
) {

    for (
        let i = 0;
        i < 16;
        i++
    ) {

        particles.push({

            x: x,

            y: y,

            vx:
                (Math.random() - .5)
                * 12,

            vy:
                (Math.random() - .5)
                * 12,

            life:
                20 +
                Math.random() * 15,

            color: color,

            size:
                2 +
                Math.random() * 5
        });
    }
}


function updateParticles() {

    for (
        const p of particles
    ) {

        p.x += p.vx;

        p.y += p.vy;

        p.vy += .3;

        p.life--;
    }

    particles =
        particles.filter(
            p => p.life > 0
        );
}


/* =========================================================
   PLAYER
========================================================= */

function updatePlayer() {

    faceOpponent(
        player,
        cpu
    );


    if (
        player.knockdown > 0
    ) {

        player.knockdown--;

        player.vx *= .9;

        player.state =
            "down";

        return;
    }


    if (
        player.hitstun > 0
    ) {

        player.hitstun--;

        player.x +=
            player.vx;

        player.vx *= .87;

        player.state =
            "hit";


        if (
            player.airborne
        ) {

            player.vy -= .7;

            player.y +=
                player.vy;


            if (
                player.y <= 0
            ) {

                player.y = 0;

                player.vy = 0;

                player.airborne =
                    false;
            }
        }

        return;
    }


    if (
        player.blockstun > 0
    ) {

        player.blockstun--;

        player.x +=
            player.vx;

        player.vx *= .85;

        player.state =
            "guard";

        return;
    }


    if (
        player.airborne
    ) {

        player.vy -= .7;

        player.y +=
            player.vy;


        if (
            player.y <= 0
        ) {

            player.y = 0;

            player.vy = 0;

            player.airborne =
                false;
        }


        if (
            player.attack
        ) {

            updateAttack(
                player,
                cpu
            );
        }

        return;
    }


    if (
        player.attack
    ) {

        updateAttack(
            player,
            cpu
        );

        player.state =
            "attack";

        return;
    }


    let moving = false;


    if (
        keys["arrowleft"]
    ) {

        player.x -= 5.2;

        moving = true;
    }


    if (
        keys["arrowright"]
    ) {

        player.x += 5.2;

        moving = true;
    }


    if (
        keys["arrowdown"]
    ) {

        player.state =
            "crouch";
    }


    else if (
        keys["arrowup"] &&
        player.y === 0
    ) {

        player.vy =
            13.5;

        player.airborne =
            true;

        player.state =
            "jump";
    }


    else if (
        keys["a"]
    ) {

        startAttack(
            player,
            "high"
        );
    }


    else if (
        keys["s"]
    ) {

        startAttack(
            player,
            "mid"
        );
    }


    else if (
        keys["d"]
    ) {

        startAttack(
            player,
            "low"
        );
    }


    else if (
        keys["f"]
    ) {

        startAttack(
            player,
            "launcher"
        );
    }


    else if (
        canAutoGuard(
            player,
            cpu
        )
    ) {

        player.state =
            "guard";
    }


    else if (
        moving
    ) {

        player.state =
            "walk";
    }


    else {

        player.state =
            "idle";
    }


    player.x =
        clamp(
            player.x,
            35,
            W - 100
        );
}


/* =========================================================
   CPU
========================================================= */

function updateCPU() {

    faceOpponent(
        cpu,
        player
    );


    if (
        cpu.knockdown > 0
    ) {

        cpu.knockdown--;

        cpu.state =
            "down";

        return;
    }


    if (
        cpu.hitstun > 0
    ) {

        cpu.hitstun--;

        cpu.x +=
            cpu.vx;

        cpu.vx *= .87;

        cpu.state =
            "hit";


        if (
            cpu.airborne
        ) {

            cpu.vy -= .7;

            cpu.y +=
                cpu.vy;


            if (
                cpu.y <= 0
            ) {

                cpu.y = 0;

                cpu.vy = 0;

                cpu.airborne =
                    false;
            }
        }

        return;
    }


    if (
        cpu.blockstun > 0
    ) {

        cpu.blockstun--;

        cpu.x +=
            cpu.vx;

        cpu.vx *= .85;

        cpu.state =
            "guard";

        return;
    }


    if (
        cpu.airborne
    ) {

        cpu.vy -= .7;

        cpu.y +=
            cpu.vy;


        if (
            cpu.y <= 0
        ) {

            cpu.y = 0;

            cpu.vy = 0;

            cpu.airborne =
                false;
        }


        if (
            cpu.attack
        ) {

            updateAttack(
                cpu,
                player
            );
        }

        return;
    }


    if (
        cpu.attack
    ) {

        updateAttack(
            cpu,
            player
        );

        cpu.state =
            "attack";

        return;
    }


    const d =
        distance(
            cpu,
            player
        );


    cpu.aiTimer++;


    if (
        cpu.aiAttackCooldown > 0
    ) {

        cpu.aiAttackCooldown--;
    }


    /*
       랜덤 가드
    */

    if (
        d < 190 &&
        Math.random() < .035
    ) {

        cpu.aiGuard =
            20 +
            Math.floor(
                Math.random() * 30
            );
    }


    if (
        cpu.aiGuard > 0
    ) {

        cpu.aiGuard--;


        if (
            player.attack === "low"
        ) {

            cpu.state =
                "crouch";
        }

        else {

            cpu.state =
                "guard";
        }

        return;
    }


    /*
       거리 좁히기
    */

    if (
        d > 145
    ) {

        if (
            player.x < cpu.x
        ) {

            cpu.x -= 2.4;
        }

        else {

            cpu.x += 2.4;
        }

        cpu.state =
            "walk";

        return;
    }


    /*
       공격
    */

    if (
        cpu.aiAttackCooldown <= 0
    ) {

        const available = [];


        for (
            const type in cpu.cooldowns
        ) {

            if (
                cpu.cooldowns[type] <= 0
            ) {

                available.push(type);
            }
        }


        if (
            available.length
        ) {

            const type =
                available[
                    Math.floor(
                        Math.random() *
                        available.length
                    )
                ];

            startAttack(
                cpu,
                type
            );
        }


        cpu.aiAttackCooldown =
            25 +
            Math.floor(
                Math.random() * 35
            );
    }

    else {

        cpu.state =
            "idle";
    }
}


/* =========================================================
   COMBO TIMER
========================================================= */

function updateCombos() {

    if (
        player.comboTimer > 0
    ) {

        player.comboTimer--;
    }

    else {

        player.combo = 0;
    }


    if (
        cpu.comboTimer > 0
    ) {

        cpu.comboTimer--;
    }

    else {

        cpu.combo = 0;
    }
}


/* =========================================================
   GAME TIMER
========================================================= */

function updateTimer(dt) {

    secondAccumulator += dt;


    if (
        secondAccumulator >= 1000
    ) {

        secondAccumulator -= 1000;

        gameTime--;

        timerEl.innerText =
            gameTime;


        if (
            gameTime <= 0
        ) {

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


/* =========================================================
   GAME OVER
========================================================= */

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


/* =========================================================
   WINNER
========================================================= */

function checkWinner() {

    if (
        player.hp <= 0
    ) {

        player.hp = 0;

        gameOver(
            "CPU WINS!"
        );

        return true;
    }


    if (
        cpu.hp <= 0
    ) {

        cpu.hp = 0;

        gameOver(
            "PLAYER WINS!"
        );

        return true;
    }


    return false;
}


/* =========================================================
   COOLDOWN UI
========================================================= */

function updateCooldownUI() {

    if (!player) {
        return;
    }


    for (
        const type in skillElements
    ) {

        const skill =
            skillElements[type];

        const cooldown =
            player.cooldowns[type];

        const max =
            ATTACKS[type].cooldown;


        if (
            cooldown > 0
        ) {

            skill.box.classList.remove(
                "ready"
            );

            skill.box.classList.add(
                "cooling"
            );


            const percent =
                (cooldown / max) * 100;


            skill.fill.style.height =
                percent + "%";

        }

        else {

            skill.box.classList.remove(
                "cooling"
            );

            skill.box.classList.add(
                "ready"
            );

            skill.fill.style.height =
                "0%";
        }
    }
}


/* =========================================================
   DRAW HELPERS
========================================================= */

function roundedRect(
    ctx,
    x,
    y,
    w,
    h,
    r
) {

    ctx.beginPath();

    ctx.roundRect(
        x,
        y,
        w,
        h,
        r
    );

    ctx.fill();
}


function limb(
    ctx,
    x1,
    y1,
    x2,
    y2,
    width,
    color
) {

    ctx.strokeStyle =
        color;

    ctx.lineWidth =
        width;

    ctx.lineCap =
        "round";

    ctx.beginPath();

    ctx.moveTo(
        x1,
        y1
    );

    ctx.lineTo(
        x2,
        y2
    );

    ctx.stroke();
}


/* =========================================================
   DRAW FIGHTER
========================================================= */

function drawFighter(
    f,
    color,
    accent
) {

    const baseY =
        H - 130 - f.y;


    const x =
        f.x;


    let bob =
        Math.sin(
            f.animationTime * .12
        ) * 2;


    if (
        f.state === "hit"
    ) {

        bob = 0;
    }


    ctx.save();


    ctx.translate(
        x,
        baseY + bob
    );


    ctx.scale(
        f.facing,
        1
    );


    /*
       SHADOW
    */

    ctx.save();

    ctx.scale(
        1,
        .25
    );

    ctx.fillStyle =
        "rgba(0,0,0,.45)";

    ctx.beginPath();

    ctx.ellipse(
        0,
        7,
        48,
        18,
        0,
        0,
        Math.PI * 2
    );

    ctx.fill();

    ctx.restore();


    let armFront = 0;
    let armBack = 0;

    let legFront = 0;
    let legBack = 0;

    let torsoLean = 0;

    let crouch = 0;


    /*
       WALK
    */

    if (
        f.state === "walk"
    ) {

        const w =
            Math.sin(
                f.animationTime * .35
            );

        legFront =
            w * .45;

        legBack =
            -w * .45;

        torsoLean =
            .04;
    }


    /*
       CROUCH
    */

    if (
        f.state === "crouch"
    ) {

        crouch = 18;

        torsoLean = -.08;
    }


    /*
       GUARD
    */

    if (
        f.state === "guard"
    ) {

        armFront = -.9;

        armBack = -.55;
    }


    /*
       HIGH
    */

    if (
        f.state === "attack" &&
        f.attack === "high"
    ) {

        const t =
            f.attackFrame;


        if (
            t < 10
        ) {

            armFront = -.5;
        }

        else {

            armFront = -1.65;
        }
    }


    /*
       MID
    */

    if (
        f.state === "attack" &&
        f.attack === "mid"
    ) {

        legFront = -1.25;

        torsoLean = .1;
    }


    /*
       LOW
    */

    if (
        f.state === "attack" &&
        f.attack === "low"
    ) {

        crouch = 14;

        legFront = -1.25;
    }


    /*
       LAUNCHER
    */

    if (
        f.state === "attack" &&
        f.attack === "launcher"
    ) {

        armFront = -1.7;

        torsoLean = -.15;
    }


    /*
       HIT
    */

    if (
        f.state === "hit"
    ) {

        torsoLean = -.28;

        armFront = .7;

        armBack = .8;
    }


    /*
       DOWN
    */

    if (
        f.state === "down"
    ) {

        ctx.rotate(
            -.95
        );
    }


    const bodyY =
        -95 + crouch;


    ctx.save();


    ctx.rotate(
        torsoLean
    );


    /*
       BACK LEG
    */

    limb(
        ctx,
        -10,
        bodyY + 42,
        -20 +
            Math.sin(
                legBack
            ) * 20,
        bodyY + 100,
        18,
        accent
    );


    /*
       FRONT LEG
    */

    limb(
        ctx,
        10,
        bodyY + 42,
        25 +
            Math.sin(
                legFront
            ) * 22,
        bodyY + 100,
        18,
        color
    );


    /*
       BODY
    */

    ctx.fillStyle =
        color;

    roundedRect(
        ctx,
        -24,
        bodyY - 5,
        48,
        65,
        14
    );


    /*
       SHOULDERS
    */

    ctx.fillStyle =
        accent;


    ctx.beginPath();

    ctx.arc(
        -20,
        bodyY + 2,
        11,
        0,
        Math.PI * 2
    );

    ctx.fill();


    ctx.beginPath();

    ctx.arc(
        20,
        bodyY + 2,
        11,
        0,
        Math.PI * 2
    );

    ctx.fill();


    /*
       BACK ARM
    */

    limb(
        ctx,
        -18,
        bodyY + 5,
        -35 +
            Math.sin(
                armBack
            ) * 25,
        bodyY + 48,
        15,
        accent
    );


    /*
       FRONT ARM
    */

    limb(
        ctx,
        18,
        bodyY + 5,
        37 +
            Math.sin(
                armFront
            ) * 42,
        bodyY + 43,
        16,
        color
    );


    /*
       HEAD
    */

    ctx.fillStyle =
        "#e6a77d";


    ctx.beginPath();

    ctx.arc(
        0,
        bodyY - 28,
        25,
        0,
        Math.PI * 2
    );

    ctx.fill();


    /*
       HAIR
    */

    ctx.fillStyle =
        "#15161a";


    ctx.beginPath();

    ctx.arc(
        0,
        bodyY - 38,
        25,
        Math.PI,
        Math.PI * 2
    );

    ctx.fill();


    /*
       EYE
    */

    ctx.fillStyle =
        "#151515";


    ctx.beginPath();

    ctx.arc(
        16,
        bodyY - 28,
        3,
        0,
        Math.PI * 2
    );

    ctx.fill();


    ctx.restore();


    /*
       ATTACK EFFECT
    */

    if (
        f.state === "attack"
    ) {

        drawAttackEffect(
            f,
            bodyY
        );
    }


    /*
       GUARD EFFECT
    */

    if (
        f.state === "guard"
    ) {

        ctx.strokeStyle =
            "rgba(100,210,255,.8)";

        ctx.lineWidth = 3;

        ctx.beginPath();

        ctx.arc(
            12,
            bodyY - 20,
            54,
            -.9,
            .9
        );

        ctx.stroke();
    }


    ctx.restore();
}


/* =========================================================
   ATTACK EFFECT
========================================================= */

function drawAttackEffect(
    f,
    bodyY
) {

    const a =
        ATTACKS[
            f.attack
        ];


    if (!a) {
        return;
    }


    if (
        !attackActive(f)
    ) {

        return;
    }


    let color =
        "#fff";


    if (
        a.level === "high"
    ) {

        color =
            "#ffcc62";
    }

    else if (
        a.level === "mid"
    ) {

        color =
            "#62d8ff";
    }

    else if (
        a.level === "low"
    ) {

        color =
            "#ff6a8a";
    }


    ctx.strokeStyle =
        color;

    ctx.lineWidth = 8;

    ctx.globalAlpha = .8;


    ctx.beginPath();

    ctx.arc(
        48,
        bodyY - 15,
        48,
        -.9,
        .7
    );

    ctx.stroke();


    ctx.globalAlpha = 1;
}


/* =========================================================
   SCENE
========================================================= */

function drawScene() {

    ctx.clearRect(
        0,
        0,
        W,
        H
    );


    /*
       BACKGROUND COLUMNS
    */

    for (
        let i = 0;
        i < 8;
        i++
    ) {

        const x =
            i * (W / 7);


        const gradient =
            ctx.createLinearGradient(
                x,
                0,
                x + 30,
                0
            );


        gradient.addColorStop(
            0,
            "rgba(0,0,0,.4)"
        );


        gradient.addColorStop(
            .5,
            "rgba(255,255,255,.05)"
        );


        gradient.addColorStop(
            1,
            "rgba(0,0,0,.4)"
        );


        ctx.fillStyle =
            gradient;


        ctx.fillRect(
            x,
            90,
            30,
            H - 210
        );
    }


    /*
       FLOOR GRID
    */

    ctx.strokeStyle =
        "rgba(255,255,255,.045)";

    ctx.lineWidth = 1;


    for (
        let y = H - 118;
        y < H;
        y += 35
    ) {

        ctx.beginPath();

        ctx.moveTo(
            0,
            y
        );

        ctx.lineTo(
            W,
            y
        );

        ctx.stroke();
    }


    for (
        let x = 0;
        x < W;
        x += 70
    ) {

        ctx.beginPath();

        ctx.moveTo(
            x,
            H - 118
        );

        ctx.lineTo(
            x + 70,
            H
        );

        ctx.stroke();
    }


    /*
       PARTICLES
    */

    for (
        const p of particles
    ) {

        ctx.globalAlpha =
            Math.max(
                0,
                p.life / 35
            );


        ctx.fillStyle =
            p.color;


        ctx.beginPath();

        ctx.arc(
            p.x,
            p.y,
            p.size,
            0,
            Math.PI * 2
        );

        ctx.fill();
    }


    ctx.globalAlpha = 1;


    if (player) {

        drawFighter(
            player,
            "#317cff",
            "#173e9d"
        );
    }


    if (cpu) {

        drawFighter(
            cpu,
            "#df343f",
            "#8f1724"
        );
    }
}


/* =========================================================
   RENDER
========================================================= */

function render() {

    if (!player || !cpu) {
        return;
    }


    playerHp.style.width =
        Math.max(
            0,
            player.hp
        ) + "%";


    cpuHp.style.width =
        Math.max(
            0,
            cpu.hp
        ) + "%";


    updateCooldownUI();

    drawScene();
}


/* =========================================================
   UPDATE
========================================================= */

function update(dt) {

    updatePlayer();

    updateCPU();

    updateCombos();

    updateParticles();

    updateCooldowns(player);

    updateCooldowns(cpu);

    updateTimer(dt);

    checkWinner();


    if (player) {

        player.animationTime++;
    }


    if (cpu) {

        cpu.animationTime++;
    }
}


/* =========================================================
   LOOP
========================================================= */

function loop(now) {

    if (!running) {

        render();

        return;
    }


    const dt =
        Math.min(
            40,
            now - lastTime
        );


    lastTime = now;


    update(dt);

    render();


    if (running) {

        requestAnimationFrame(
            loop
        );
    }
}


/* =========================================================
   START BUTTON
========================================================= */

startButton.addEventListener(
    "click",
    startGame
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
