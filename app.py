import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="IRON FIGHTERS",
    page_icon="🥊",
    layout="wide"
)

st.markdown("""
<style>
.block-container {
    padding: 0 !important;
    max-width: 1400px !important;
}
[data-testid="stHeader"] {
    display: none;
}
iframe {
    border: none !important;
}
</style>
""", unsafe_allow_html=True)


GAME = r"""
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">

<style>
* {
    box-sizing: border-box;
}

html, body {
    margin: 0;
    padding: 0;
    width: 100%;
    height: 100%;
    overflow: hidden;
    background: #07090d;
    font-family: Arial, sans-serif;
}

#game {
    position: relative;
    width: 100%;
    height: 720px;
    max-width: 1280px;
    margin: auto;
    overflow: hidden;

    background:
        radial-gradient(
            ellipse at 50% 25%,
            rgba(100,120,170,.25),
            transparent 48%
        ),
        linear-gradient(
            #101a2c 0%,
            #233b5e 48%,
            #49372a 49%,
            #171515 53%,
            #08090b 100%
        );

    border: 2px solid #3e434c;
}

#canvas {
    position: absolute;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    z-index: 10;
}

#floor {
    position: absolute;
    left: 0;
    right: 0;
    bottom: 0;
    height: 125px;
    z-index: 3;

    background:
        linear-gradient(
            rgba(255,255,255,.035) 1px,
            transparent 1px
        ),
        linear-gradient(
            90deg,
            rgba(255,255,255,.035) 1px,
            transparent 1px
        ),
        #111214;

    background-size: 40px 40px;
}

#floorLine {
    position: absolute;
    left: 0;
    right: 0;
    bottom: 123px;
    height: 4px;
    z-index: 5;

    background: #c99a43;
    box-shadow: 0 0 15px rgba(255,190,60,.45);
}

/* HUD */

#hud {
    position: absolute;
    z-index: 50;
    left: 20px;
    right: 20px;
    top: 18px;

    display: grid;
    grid-template-columns:
        80px
        1fr
        65px
        1fr
        80px;

    gap: 10px;
    align-items: center;
}

.name {
    color: white;
    font-weight: 900;
    font-size: 14px;
}

.name.right {
    text-align: right;
}

.hp {
    height: 27px;
    background: #070707;
    border: 2px solid #ddd;
    overflow: hidden;
}

.hpBar {
    height: 100%;
    width: 100%;
    transition: width .1s linear;
}

#playerHP {
    background: linear-gradient(#5fff96,#139343);
}

#cpuHP {
    background: linear-gradient(#ff6262,#b50f24);
    float: right;
}

#timer {
    text-align: center;
    color: white;
    font-size: 30px;
    font-weight: 1000;
}

/* COMBO */

#combo {
    position: absolute;
    z-index: 80;
    left: 50%;
    top: 110px;
    transform: translateX(-50%) scale(.75);
    opacity: 0;

    color: #ffd84d;
    font-size: 38px;
    font-weight: 1000;

    text-shadow:
        0 4px 0 #674a00,
        0 7px 20px #000;

    transition: .12s;
}

#combo.show {
    opacity: 1;
    transform: translateX(-50%) scale(1);
}

#hitText {
    position: absolute;
    z-index: 80;
    left: 50%;
    top: 165px;
    transform: translateX(-50%);

    font-size: 19px;
    font-weight: 1000;

    opacity: 0;
}

#hitText.show {
    opacity: 1;
}

/* MESSAGE */

#message {
    position: absolute;
    z-index: 150;
    left: 50%;
    top: 43%;

    transform: translate(-50%,-50%);

    color: white;
    font-size: 64px;
    font-weight: 1000;

    text-shadow:
        0 5px 25px #000;

    display: none;
    white-space: nowrap;
}

/* CONTROLS */

#controls {
    position: absolute;
    z-index: 60;

    left: 50%;
    bottom: 17px;

    transform: translateX(-50%);

    display: flex;
    gap: 7px;
}

.control {
    width: 58px;
    height: 45px;

    background: #14161a;

    border:
        2px solid #666;

    border-radius: 5px;

    color: white;

    display: flex;
    align-items: center;
    justify-content: center;

    flex-direction: column;

    font-weight: 900;
}

.control .key {
    font-size: 15px;
}

.control .label {
    font-size: 8px;
    color: #aaa;
    margin-top: 2px;
}

/* START */

#start {
    position: absolute;
    z-index: 200;
    inset: 0;

    display: flex;

    align-items: center;
    justify-content: center;

    flex-direction: column;

    background: rgba(3,4,7,.84);
}

#start h1 {
    margin: 0;

    color: white;

    font-size: 54px;

    font-weight: 1000;

    letter-spacing: 4px;
}

#start p {
    color: #999;
    margin: 8px 0 25px;
}

button {
    border: 0;
    border-radius: 5px;

    padding: 13px 40px;

    background:
        linear-gradient(
            #ed3c47,
            #941521
        );

    color: white;

    font-size: 19px;

    font-weight: 1000;

    cursor: pointer;
}

button:hover {
    filter: brightness(1.18);
}

#hint {
    position: absolute;

    z-index: 70;

    left: 50%;
    bottom: 68px;

    transform: translateX(-50%);

    color: #bbb;

    background: rgba(0,0,0,.62);

    padding: 7px 15px;

    border-radius: 14px;

    font-size: 11px;

    white-space: nowrap;
}

#flash {
    position: absolute;
    z-index: 120;

    inset: 0;

    background: white;

    pointer-events: none;

    opacity: 0;
}

#flash.active {
    animation: flash .08s;
}

@keyframes flash {
    from { opacity: .4; }
    to { opacity: 0; }
}

@media(max-width:700px) {

    #game {
        height: 650px;
    }

    #controls {
        gap: 3px;
    }

    .control {
        width: 45px;
        height: 40px;
    }

    .control .label {
        font-size: 7px;
    }

    #hint {
        width: 96%;
        text-align: center;
        white-space: normal;
    }

    #start h1 {
        font-size: 32px;
    }
}
</style>
</head>


<body>

<div id="game">

    <canvas id="canvas"></canvas>

    <div id="floor"></div>
    <div id="floorLine"></div>

    <div id="hud">

        <div class="name">
            BLUE
        </div>

        <div class="hp">
            <div id="playerHP" class="hpBar"></div>
        </div>

        <div id="timer">
            60
        </div>

        <div class="hp">
            <div id="cpuHP" class="hpBar"></div>
        </div>

        <div class="name right">
            RED
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


    <div id="controls">

        <div class="control">
            <div class="key">← →</div>
            <div class="label">MOVE</div>
        </div>

        <div class="control">
            <div class="key">→→</div>
            <div class="label">DASH</div>
        </div>

        <div class="control">
            <div class="key">←←</div>
            <div class="label">BACK</div>
        </div>

        <div class="control">
            <div class="key">J</div>
            <div class="label">LEFT</div>
        </div>

        <div class="control">
            <div class="key">K</div>
            <div class="label">RIGHT</div>
        </div>

        <div class="control">
            <div class="key">U</div>
            <div class="label">UPPER</div>
        </div>

        <div class="control">
            <div class="key">I</div>
            <div class="label">KICK</div>
        </div>

        <div class="control">
            <div class="key">O</div>
            <div class="label">LOW</div>
        </div>

    </div>


    <div id="hint">
        ←→ 이동 · →→ 대시 · ←← 백대시 · J 왼손 · K 오른손 · U 어퍼 · I 앞발차기 · O 하단발차기 · SPACE 가드
    </div>


    <div id="start">

        <h1>
            IRON FIGHTERS
        </h1>

        <p>
            ORIGINAL STICKMAN FIGHTING GAME
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

    const dpr =
        window.devicePixelRatio || 1;

    canvas.width =
        W * dpr;

    canvas.height =
        H * dpr;

    canvas.style.width =
        W + "px";

    canvas.style.height =
        H + "px";

    ctx.setTransform(
        dpr,
        0,
        0,
        dpr,
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

let lastLeft = 0;
let lastRight = 0;

let dashBuffer = 0;
let backBuffer = 0;


document.addEventListener(
    "keydown",
    e => {

        const k =
            e.key.toLowerCase();

        if (!keys[k]) {

            if (k === "arrowright") {

                const now =
                    performance.now();

                if (
                    now - lastRight < 280
                ) {

                    dashBuffer = 18;
                }

                lastRight = now;
            }


            if (k === "arrowleft") {

                const now =
                    performance.now();

                if (
                    now - lastLeft < 280
                ) {

                    backBuffer = 18;
                }

                lastLeft = now;
            }
        }

        keys[k] = true;

        if (
            [
                "arrowleft",
                "arrowright",
                "arrowup",
                "arrowdown",
                " ",
                "j",
                "k",
                "u",
                "i",
                "o"
            ].includes(k)
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


/* =========================================================
   ATTACKS
========================================================= */

const ATTACKS = {

    leftPunch: {

        name: "LEFT PUNCH",

        level: "high",

        startup: 5,

        active: 4,

        recovery: 12,

        range: 118,

        damage: 5,

        hitstun: 16,

        guardstun: 7,

        knockback: 3,

        cooldown: 8,

        animation: "leftPunch"
    },


    rightPunch: {

        name: "RIGHT PUNCH",

        level: "high",

        startup: 7,

        active: 4,

        recovery: 14,

        range: 125,

        damage: 7,

        hitstun: 18,

        guardstun: 8,

        knockback: 4,

        cooldown: 10,

        animation: "rightPunch"
    },


    uppercut: {

        name: "UPPERCUT",

        level: "mid",

        startup: 12,

        active: 6,

        recovery: 22,

        range: 128,

        damage: 10,

        hitstun: 38,

        guardstun: 12,

        knockback: 5,

        cooldown: 28,

        launcher: true,

        animation: "uppercut"
    },


    frontKick: {

        name: "FRONT KICK",

        level: "mid",

        startup: 10,

        active: 6,

        recovery: 18,

        range: 145,

        damage: 9,

        hitstun: 22,

        guardstun: 10,

        knockback: 6,

        cooldown: 18,

        animation: "frontKick"
    },


    lowKick: {

        name: "LOW KICK",

        level: "low",

        startup: 11,

        active: 6,

        recovery: 20,

        range: 132,

        damage: 7,

        hitstun: 19,

        guardstun: 8,

        knockback: 4,

        cooldown: 20,

        animation: "lowKick"
    },


    heavyKick: {

        name: "HEAVY KICK",

        level: "mid",

        startup: 16,

        active: 7,

        recovery: 27,

        range: 152,

        damage: 13,

        hitstun: 28,

        guardstun: 13,

        knockback: 9,

        cooldown: 32,

        animation: "heavyKick"
    }
};


/* =========================================================
   FIGHTER
========================================================= */

function makeFighter(
    x,
    cpu
) {

    return {

        x: x,

        y: 0,

        vx: 0,

        vy: 0,

        facing:
            cpu ? -1 : 1,

        cpu: cpu,

        hp: 100,

        state: "idle",

        attack: null,

        attackFrame: 0,

        attackConnected: false,

        hitstun: 0,

        blockstun: 0,

        airborne: false,

        combo: 0,

        comboTimer: 0,

        animationTime: 0,

        dash: 0,

        backdash: 0,

        dashCooldown: 0,

        aiAttackCooldown: 0,

        aiGuard: 0
    };
}


let player;
let cpu;

let running = false;

let gameTime = 60;

let secondTimer = 0;

let lastTime = 0;


/* =========================================================
   DOM
========================================================= */

const playerHP =
    document.getElementById(
        "playerHP"
    );

const cpuHP =
    document.getElementById(
        "cpuHP"
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


/* =========================================================
   START
========================================================= */

function startGame() {

    player =
        makeFighter(
            W * .24,
            false
        );

    cpu =
        makeFighter(
            W * .76,
            true
        );

    gameTime = 60;

    secondTimer = 0;

    dashBuffer = 0;
    backBuffer = 0;

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


startButton.addEventListener(
    "click",
    startGame
);


/* =========================================================
   HELPERS
========================================================= */

function clamp(
    v,
    min,
    max
) {

    return Math.max(
        min,
        Math.min(
            max,
            v
        )
    );
}


function distance(a,b) {

    return Math.abs(
        a.x - b.x
    );
}


function busy(f) {

    return (
        f.hitstun > 0 ||
        f.blockstun > 0 ||
        f.attack ||
        f.dash > 0 ||
        f.backdash > 0
    );
}


function faceOpponent(
    f,
    opponent
) {

    f.facing =
        opponent.x >= f.x
        ? 1
        : -1;
}


/* =========================================================
   ATTACK
========================================================= */

function startAttack(
    f,
    type
) {

    if (!running) return false;

    if (
        f.hitstun > 0 ||
        f.blockstun > 0 ||
        f.attack ||
        f.dash > 0 ||
        f.backdash > 0
    ) {

        return false;
    }

    f.attack = type;

    f.attackFrame = 0;

    f.attackConnected = false;

    return true;
}


function attackActive(f) {

    if (!f.attack) return false;

    const a =
        ATTACKS[
            f.attack
        ];

    return (
        f.attackFrame >= a.startup &&
        f.attackFrame <
        a.startup + a.active
    );
}


function attackFinished(f) {

    if (!f.attack) return false;

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
   GUARD
========================================================= */

function isGuarding(f) {

    if (f.hitstun > 0) {
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

    return (
        keys[" "] === true
    );
}


function guardResult(
    defender,
    attack
) {

    if (
        attack.level === "high"
    ) {

        if (
            keys["arrowdown"] &&
            !defender.cpu
        ) {

            return "evade";
        }

        return isGuarding(
            defender
        );
    }


    if (
        attack.level === "mid"
    ) {

        return isGuarding(
            defender
        );
    }


    if (
        attack.level === "low"
    ) {

        return (
            isGuarding(
                defender
            ) &&
            keys["arrowdown"]
        );
    }


    return false;
}


/* =========================================================
   HIT
========================================================= */

function inRange(
    attacker,
    defender
) {

    const a =
        ATTACKS[
            attacker.attack
        ];

    if (!a) return false;

    if (
        distance(
            attacker,
            defender
        ) > a.range
    ) {

        return false;
    }

    const dir =
        Math.sign(
            defender.x -
            attacker.x
        );

    return (
        dir === attacker.facing
    );
}


function resolveHit(
    attacker,
    defender
) {

    if (
        attacker.attackConnected
    ) {

        return;
    }

    if (
        !inRange(
            attacker,
            defender
        )
    ) {

        return;
    }

    attacker.attackConnected =
        true;

    const a =
        ATTACKS[
            attacker.attack
        ];

    const guard =
        guardResult(
            defender,
            a
        );


    if (
        guard === "evade"
    ) {

        showHitText(
            "HIGH CRUSH",
            "#61dfff"
        );

        return;
    }


    if (guard) {

        defender.blockstun =
            a.guardstun;

        defender.state =
            "guard";

        showHitText(
            "GUARD",
            "#61dfff"
        );

        spawnImpact(
            defender.x,
            H - 245,
            "#62dfff"
        );

        return;
    }


    let damage =
        a.damage;


    /*
       공중 콤보 보정
    */

    if (
        defender.airborne
    ) {

        damage *=
            Math.pow(
                .92,
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


    defender.hp -=
        damage;

    defender.hitstun =
        a.hitstun;

    defender.vx =
        attacker.facing *
        a.knockback;

    defender.state =
        "hit";


    attacker.combo++;

    attacker.comboTimer =
        55;


    /*
       런처
    */

    if (
        a.launcher &&
        !defender.airborne
    ) {

        defender.airborne =
            true;

        defender.vy =
            12;

        defender.y =
            1;

        defender.hitstun =
            42;

        showHitText(
            "LAUNCH!",
            "#ffe34f"
        );
    }

    else {

        showHitText(
            a.name,
            "#ffe34f"
        );
    }


    spawnImpact(
        defender.x,
        H - 235 - defender.y,
        "#ffe34f"
    );

    flashScreen();

    showCombo(
        attacker
    );
}


/* =========================================================
   UPDATE ATTACK
========================================================= */

function updateAttack(
    f,
    opponent
) {

    if (!f.attack) return;

    f.attackFrame++;


    if (
        attackActive(f)
    ) {

        resolveHit(
            f,
            opponent
        );
    }


    if (
        attackFinished(f)
    ) {

        f.attack = null;

        f.attackFrame = 0;

        f.attackConnected =
            false;
    }
}


/* =========================================================
   DASH
========================================================= */

function startDash(f) {

    if (
        f.hitstun > 0 ||
        f.blockstun > 0 ||
        f.attack ||
        f.airborne
    ) {

        return;
    }

    f.dash = 10;

    f.state = "dash";
}


function startBackdash(f) {

    if (
        f.hitstun > 0 ||
        f.blockstun > 0 ||
        f.attack ||
        f.airborne
    ) {

        return;
    }

    f.backdash = 13;

    f.state = "backdash";
}


/* =========================================================
   PLAYER UPDATE
========================================================= */

function updatePlayer() {

    faceOpponent(
        player,
        cpu
    );


    /*
       피격
    */

    if (
        player.hitstun > 0
    ) {

        player.hitstun--;

        player.x +=
            player.vx;

        player.vx *= .88;


        if (
            player.airborne
        ) {

            player.vy -= .65;

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


    /*
       가드 경직
    */

    if (
        player.blockstun > 0
    ) {

        player.blockstun--;

        player.state =
            "guard";

        return;
    }


    /*
       공중
    */

    if (
        player.airborne
    ) {

        player.vy -= .65;

        player.y +=
            player.vy;


        if (
            player.attack
        ) {

            updateAttack(
                player,
                cpu
            );
        }


        if (
            player.y <= 0
        ) {

            player.y = 0;

            player.vy = 0;

            player.airborne =
                false;
        }

        return;
    }


    /*
       공격 중
    */

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


    /*
       대시
    */

    if (
        dashBuffer > 0
    ) {

        startDash(
            player
        );

        dashBuffer = 0;
    }


    if (
        backBuffer > 0
    ) {

        startBackdash(
            player
        );

        backBuffer = 0;
    }


    if (
        player.dash > 0
    ) {

        player.dash--;

        player.x +=
            player.facing * 10;

        player.state =
            "dash";

        return;
    }


    if (
        player.backdash > 0
    ) {

        player.backdash--;

        player.x -=
            player.facing * 8;

        player.state =
            "backdash";

        return;
    }


    /*
       점프
    */

    if (
        keys["arrowup"]
    ) {

        player.vy =
            12;

        player.airborne =
            true;

        player.state =
            "jump";

        return;
    }


    /*
       공격 입력
    */

    if (
        keys["j"]
    ) {

        startAttack(
            player,
            "leftPunch"
        );

        return;
    }


    if (
        keys["k"]
    ) {

        startAttack(
            player,
            "rightPunch"
        );

        return;
    }


    if (
        keys["u"]
    ) {

        startAttack(
            player,
            "uppercut"
        );

        return;
    }


    if (
        keys["i"]
    ) {

        startAttack(
            player,
            "frontKick"
        );

        return;
    }


    if (
        keys["o"]
    ) {

        startAttack(
            player,
            "lowKick"
        );

        return;
    }


    /*
       하단 자세
    */

    if (
        keys["arrowdown"]
    ) {

        player.state =
            "crouch";

        return;
    }


    /*
       이동
    */

    let moved = false;


    if (
        keys["arrowleft"]
    ) {

        player.x -= 5;

        moved = true;
    }


    if (
        keys["arrowright"]
    ) {

        player.x += 5;

        moved = true;
    }


    if (
        keys[" "]
    ) {

        player.state =
            "guard";

        return;
    }


    player.state =
        moved
        ? "walk"
        : "idle";


    player.x =
        clamp(
            player.x,
            70,
            W - 70
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
        cpu.hitstun > 0
    ) {

        cpu.hitstun--;

        cpu.x +=
            cpu.vx;

        cpu.vx *= .88;


        if (
            cpu.airborne
        ) {

            cpu.vy -= .65;

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

        cpu.state =
            "guard";

        return;
    }


    if (
        cpu.airborne
    ) {

        cpu.vy -= .65;

        cpu.y +=
            cpu.vy;


        if (
            cpu.attack
        ) {

            updateAttack(
                cpu,
                player
            );
        }


        if (
            cpu.y <= 0
        ) {

            cpu.y = 0;

            cpu.vy = 0;

            cpu.airborne =
                false;
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


    /*
       접근
    */

    if (
        d > 155
    ) {

        cpu.x +=
            Math.sign(
                player.x -
                cpu.x
            ) * 2.5;

        cpu.state =
            "walk";

        return;
    }


    /*
       플레이어가 공격 중이면
       일정 확률로 가드
    */

    if (
        player.attack &&
        Math.random() < .5
    ) {

        cpu.aiGuard =
            18 +
            Math.floor(
                Math.random() * 22
            );

        cpu.state =
            "guard";

        return;
    }


    if (
        cpu.aiGuard > 0
    ) {

        cpu.aiGuard--;

        cpu.state =
            "guard";

        return;
    }


    if (
        cpu.aiAttackCooldown > 0
    ) {

        cpu.aiAttackCooldown--;

        cpu.state =
            "idle";

        return;
    }


    const r =
        Math.random();


    let attack;


    if (
        r < .16
    ) {

        attack =
            "leftPunch";
    }

    else if (
        r < .33
    ) {

        attack =
            "rightPunch";
    }

    else if (
        r < .50
    ) {

        attack =
            "frontKick";
    }

    else if (
        r < .67
    ) {

        attack =
            "lowKick";
    }

    else if (
        r < .84
    ) {

        attack =
            "uppercut";
    }

    else {

        attack =
            "heavyKick";
    }


    startAttack(
        cpu,
        attack
    );


    cpu.aiAttackCooldown =
        22 +
        Math.floor(
            Math.random() * 24
        );
}


/* =========================================================
   COMBO
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


function showCombo(f) {

    if (
        f.combo < 2
    ) {

        return;
    }


    comboEl.innerText =
        f.combo +
        " HIT COMBO";


    comboEl.classList.add(
        "show"
    );


    clearTimeout(
        showCombo.timer
    );


    showCombo.timer =
        setTimeout(
            () => {

                comboEl.classList.remove(
                    "show"
                );

            },
            650
        );
}


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
            () => {

                hitTextEl.classList.remove(
                    "show"
                );

            },
            300
        );
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
        i < 15;
        i++
    ) {

        particles.push({

            x: x,

            y: y,

            vx:
                (
                    Math.random() -
                    .5
                ) * 9,

            vy:
                (
                    Math.random() -
                    .5
                ) * 9,

            life:
                15 +
                Math.random() * 18,

            color: color,

            size:
                2 +
                Math.random() * 3
        });
    }
}


function updateParticles() {

    for (
        const p of particles
    ) {

        p.x += p.vx;

        p.y += p.vy;

        p.vy += .25;

        p.life--;
    }


    particles =
        particles.filter(
            p =>
                p.life > 0
        );
}


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
   DRAW STICKMAN
========================================================= */

function drawStickman(
    f,
    color,
    darkColor
) {

    /*
       캐릭터 크기
       실제 화면에서 크게 보이도록 1.25
    */

    const scale =
        1.25;


    const baseY =
        H - 125 - f.y;


    ctx.save();


    ctx.translate(
        f.x,
        baseY
    );


    ctx.scale(
        f.facing * scale,
        scale
    );


    /*
       그림자
    */

    ctx.save();

    ctx.scale(
        1,
        .25
    );

    ctx.fillStyle =
        "rgba(0,0,0,.55)";

    ctx.beginPath();

    ctx.ellipse(
        0,
        10,
        45,
        14,
        0,
        0,
        Math.PI * 2
    );

    ctx.fill();

    ctx.restore();


    let bodyTilt = 0;

    let crouch = 0;

    let leftArm = {
        x: -32,
        y: -72
    };

    let rightArm = {
        x: 32,
        y: -72
    };

    let leftLeg = {
        x: -18,
        y: 36
    };

    let rightLeg = {
        x: 18,
        y: 36
    };


    /*
       WALK
    */

    if (
        f.state === "walk"
    ) {

        const w =
            Math.sin(
                f.animationTime * .32
            );

        leftLeg.x =
            -18 - w * 20;

        rightLeg.x =
            18 + w * 20;

        leftArm.x =
            -30 + w * 15;

        rightArm.x =
            30 - w * 15;
    }


    /*
       DASH
    */

    if (
        f.state === "dash"
    ) {

        bodyTilt =
            -.18;

        leftArm.x =
            -52;

        leftArm.y =
            -76;

        rightArm.x =
            48;

        rightArm.y =
            -55;

        leftLeg.x =
            -38;

        rightLeg.x =
            30;
    }


    /*
       BACKDASH
    */

    if (
        f.state === "backdash"
    ) {

        bodyTilt =
            .22;

        leftArm.x =
            -48;

        rightArm.x =
            38;

        leftLeg.x =
            -32;

        rightLeg.x =
            38;
    }


    /*
       CROUCH
    */

    if (
        f.state === "crouch"
    ) {

        crouch = 20;

        leftLeg.x =
            -28;

        rightLeg.x =
            28;
    }


    /*
       GUARD
    */

    if (
        f.state === "guard"
    ) {

        leftArm.x =
            15;

        leftArm.y =
            -100;

        rightArm.x =
            36;

        rightArm.y =
            -91;
    }


    /*
       LEFT PUNCH
    */

    if (
        f.state === "attack" &&
        f.attack === "leftPunch"
    ) {

        if (
            f.attackFrame <
            ATTACKS.leftPunch.startup
        ) {

            leftArm.x =
                -18;

            leftArm.y =
                -70;

        } else {

            leftArm.x =
                70;

            leftArm.y =
                -86;

            bodyTilt =
                -.06;
        }
    }


    /*
       RIGHT PUNCH
    */

    if (
        f.state === "attack" &&
        f.attack === "rightPunch"
    ) {

        if (
            f.attackFrame <
            ATTACKS.rightPunch.startup
        ) {

            rightArm.x =
                20;

            rightArm.y =
                -70;

        } else {

            rightArm.x =
                78;

            rightArm.y =
                -72;

            bodyTilt =
                -.10;
        }
    }


    /*
       UPPERCUT
    */

    if (
        f.state === "attack" &&
        f.attack === "uppercut"
    ) {

        rightArm.x =
            52;

        rightArm.y =
            -116;

        leftArm.x =
            -25;

        leftArm.y =
            -75;

        bodyTilt =
            -.08;
    }


    /*
       FRONT KICK
    */

    if (
        f.state === "attack" &&
        f.attack === "frontKick"
    ) {

        rightLeg.x =
            65;

        rightLeg.y =
            -5;

        bodyTilt =
            -.12;
    }


    /*
       LOW KICK
    */

    if (
        f.state === "attack" &&
        f.attack === "lowKick"
    ) {

        crouch = 13;

        rightLeg.x =
            68;

        rightLeg.y =
            25;

        bodyTilt =
            -.15;
    }


    /*
       HEAVY KICK
    */

    if (
        f.state === "attack" &&
        f.attack === "heavyKick"
    ) {

        rightLeg.x =
            75;

        rightLeg.y =
            -22;

        bodyTilt =
            -.18;
    }


    /*
       HIT
    */

    if (
        f.state === "hit"
    ) {

        bodyTilt =
            -.25;

        leftArm.x =
            -48;

        leftArm.y =
            -58;

        rightArm.x =
            42;

        rightArm.y =
            -54;

        leftLeg.x =
            -32;

        rightLeg.x =
            32;
    }


    ctx.rotate(
        bodyTilt
    );


    /*
       LEGS
    */

    ctx.lineCap =
        "round";

    ctx.lineJoin =
        "round";

    ctx.lineWidth =
        14;


    ctx.strokeStyle =
        darkColor;


    ctx.beginPath();

    ctx.moveTo(
        -9,
        -40 + crouch
    );

    ctx.lineTo(
        leftLeg.x,
        leftLeg.y
    );

    ctx.stroke();


    ctx.strokeStyle =
        color;


    ctx.beginPath();

    ctx.moveTo(
        9,
        -40 + crouch
    );

    ctx.lineTo(
        rightLeg.x,
        rightLeg.y
    );

    ctx.stroke();


    /*
       BODY
    */

    ctx.strokeStyle =
        color;

    ctx.lineWidth =
        19;

    ctx.beginPath();

    ctx.moveTo(
        0,
        -110 + crouch
    );

    ctx.lineTo(
        0,
        -42 + crouch
    );

    ctx.stroke();


    /*
       HEAD
    */

    ctx.fillStyle =
        color;

    ctx.beginPath();

    ctx.arc(
        0,
        -130 + crouch,
        20,
        0,
        Math.PI * 2
    );

    ctx.fill();


    /*
       ARMS
    */

    ctx.lineWidth =
        13;

    ctx.strokeStyle =
        darkColor;


    ctx.beginPath();

    ctx.moveTo(
        -10,
        -97 + crouch
    );

    ctx.lineTo(
        leftArm.x,
        leftArm.y + crouch
    );

    ctx.stroke();


    ctx.strokeStyle =
        color;


    ctx.beginPath();

    ctx.moveTo(
        10,
        -97 + crouch
    );

    ctx.lineTo(
        rightArm.x,
        rightArm.y + crouch
    );

    ctx.stroke();


    /*
       FIST
    */

    ctx.fillStyle =
        color;


    ctx.beginPath();

    ctx.arc(
        rightArm.x,
        rightArm.y + crouch,
        8,
        0,
        Math.PI * 2
    );

    ctx.fill();


    ctx.restore();
}


/* =========================================================
   ATTACK EFFECT
========================================================= */

function drawAttackEffect(f) {

    if (!f.attack) return;

    if (!attackActive(f)) return;


    const a =
        ATTACKS[
            f.attack
        ];


    let color;


    if (
        a.level === "high"
    ) {

        color =
            "#ffd34d";

    } else if (
        a.level === "mid"
    ) {

        color =
            "#5ddcff";

    } else {

        color =
            "#ff5d8a";
    }


    ctx.save();


    ctx.translate(
        f.x,
        H - 125 - f.y
    );


    ctx.scale(
        f.facing,
        1
    );


    ctx.globalAlpha =
        .75;

    ctx.strokeStyle =
        color;

    ctx.lineWidth =
        6;


    ctx.beginPath();


    if (
        a.level === "low"
    ) {

        ctx.arc(
            35,
            -40,
            50,
            -.2,
            1.2
        );

    } else {

        ctx.arc(
            45,
            -75,
            52,
            -.9,
            .6
        );
    }


    ctx.stroke();


    ctx.restore();
}


/* =========================================================
   BACKGROUND
========================================================= */

function drawBackground() {

    /*
       경기장 세로 구조물
    */

    for (
        let i = 0;
        i < 10;
        i++
    ) {

        const x =
            i * W / 9;

        ctx.fillStyle =
            "rgba(0,0,0,.13)";

        ctx.fillRect(
            x,
            90,
            22,
            H - 210
        );
    }


    /*
       바닥 원근선
    */

    ctx.strokeStyle =
        "rgba(255,255,255,.04)";

    ctx.lineWidth = 1;


    for (
        let y = H - 120;
        y < H;
        y += 32
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
}


/* =========================================================
   RENDER
========================================================= */

function render() {

    ctx.clearRect(
        0,
        0,
        W,
        H
    );


    drawBackground();


    /*
       PARTICLES
    */

    for (
        const p of particles
    ) {

        ctx.globalAlpha =
            p.life / 30;

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

        drawStickman(
            player,
            "#246bff",
            "#123d99"
        );

        drawAttackEffect(
            player
        );
    }


    if (cpu) {

        drawStickman(
            cpu,
            "#ed273b",
            "#8f1221"
        );

        drawAttackEffect(
            cpu
        );
    }


    updateHUD();
}


/* =========================================================
   HUD
========================================================= */

function updateHUD() {

    if (!player) return;


    playerHP.style.width =
        clamp(
            player.hp,
            0,
            100
        ) + "%";


    cpuHP.style.width =
        clamp(
            cpu.hp,
            0,
            100
        ) + "%";
}


/* =========================================================
   TIMER
========================================================= */

function updateTimer(dt) {

    secondTimer += dt;


    if (
        secondTimer >= 1000
    ) {

        secondTimer -= 1000;

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
                    "BLUE WINS!"
                );

            } else if (
                cpu.hp >
                player.hp
            ) {

                gameOver(
                    "RED WINS!"
                );

            } else {

                gameOver(
                    "DRAW!"
                );
            }
        }
    }
}


/* =========================================================
   WIN
========================================================= */

function checkWinner() {

    if (
        player.hp <= 0
    ) {

        player.hp = 0;

        gameOver(
            "RED WINS!"
        );

        return true;
    }


    if (
        cpu.hp <= 0
    ) {

        cpu.hp = 0;

        gameOver(
            "BLUE WINS!"
        );

        return true;
    }


    return false;
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


/* =========================================================
   LOOP
========================================================= */

function update(dt) {

    updatePlayer();

    updateCPU();

    updateCombos();

    updateParticles();

    updateTimer(dt);


    if (dashBuffer > 0) {
        dashBuffer--;
    }

    if (backBuffer > 0) {
        backBuffer--;
    }


    player.animationTime++;

    cpu.animationTime++;


    checkWinner();
}


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

</script>

</body>
</html>
"""


components.html(
    GAME,
    height=750,
    scrolling=False
)
