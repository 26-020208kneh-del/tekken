import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="IRON FIGHTERS",
    page_icon="🥊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
#MainMenu {visibility:hidden;}
header {visibility:hidden;}
footer {visibility:hidden;}

.block-container {
    padding: 0 !important;
    max-width: 1400px !important;
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

html,
body {
    margin: 0;
    padding: 0;
    width: 100%;
    height: 100%;
    overflow: hidden;
    background: #050608;
    font-family: Arial, sans-serif;
}

#game {
    position: relative;

    width: 100%;
    height: 760px;

    max-width: 1400px;

    margin: auto;

    overflow: hidden;

    background:
        radial-gradient(
            ellipse at 50% 20%,
            rgba(90,120,180,.32),
            transparent 48%
        ),
        linear-gradient(
            #0c1424 0%,
            #203a60 47%,
            #3c3027 48%,
            #171515 55%,
            #08090b 100%
        );

    border: 2px solid #414752;
}


/* =========================
   CANVAS
========================= */

#canvas {

    position: absolute;

    left: 0;
    top: 0;

    width: 100%;
    height: 100%;

    z-index: 10;
}


/* =========================
   FLOOR
========================= */

#floor {

    position: absolute;

    left: 0;
    right: 0;
    bottom: 0;

    height: 135px;

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

    background-size: 45px 45px;
}


#floorLine {

    position: absolute;

    left: 0;
    right: 0;

    bottom: 133px;

    height: 4px;

    z-index: 5;

    background: #d09a3c;

    box-shadow:
        0 0 18px rgba(255,190,60,.5);
}


/* =========================
   HUD
========================= */

#hud {

    position: absolute;

    z-index: 60;

    left: 22px;
    right: 22px;
    top: 18px;

    display: grid;

    grid-template-columns:
        85px
        1fr
        70px
        1fr
        85px;

    gap: 10px;

    align-items: center;
}


.name {

    color: white;

    font-size: 15px;

    font-weight: 1000;
}


.name.right {

    text-align: right;
}


.hp {

    height: 28px;

    background: #050505;

    border: 2px solid #ddd;

    overflow: hidden;
}


.hpBar {

    height: 100%;

    width: 100%;

    transition:
        width .12s linear;
}


#playerHP {

    background:
        linear-gradient(
            #63b8ff,
            #1767dc
        );
}


#cpuHP {

    background:
        linear-gradient(
            #ff6666,
            #b31328
        );

    float: right;
}


#timer {

    text-align: center;

    color: white;

    font-size: 31px;

    font-weight: 1000;
}


/* =========================
   COMBO
========================= */

#combo {

    position: absolute;

    z-index: 80;

    left: 50%;
    top: 110px;

    transform:
        translateX(-50%)
        scale(.7);

    opacity: 0;

    color: #ffd83d;

    font-size: 42px;

    font-weight: 1000;

    text-shadow:
        0 4px 0 #604700,
        0 7px 25px #000;

    transition:
        .12s;
}


#combo.show {

    opacity: 1;

    transform:
        translateX(-50%)
        scale(1);
}


#hitText {

    position: absolute;

    z-index: 80;

    left: 50%;
    top: 165px;

    transform:
        translateX(-50%);

    color: white;

    font-size: 21px;

    font-weight: 1000;

    opacity: 0;
}


#hitText.show {

    opacity: 1;
}


/* =========================
   MESSAGE
========================= */

#message {

    position: absolute;

    z-index: 200;

    left: 50%;
    top: 44%;

    transform:
        translate(-50%,-50%);

    color: white;

    font-size: 65px;

    font-weight: 1000;

    text-shadow:
        0 5px 30px #000;

    display: none;

    white-space: nowrap;
}


/* =========================
   CONTROLS
========================= */

#controls {

    position: absolute;

    z-index: 70;

    left: 50%;
    bottom: 17px;

    transform:
        translateX(-50%);

    display: flex;

    gap: 6px;
}


.control {

    width: 62px;
    height: 47px;

    background:
        linear-gradient(
            #22252b,
            #111216
        );

    border:
        2px solid #626772;

    border-radius: 6px;

    color: white;

    display: flex;

    align-items: center;
    justify-content: center;

    flex-direction: column;

    font-weight: 1000;

    box-shadow:
        0 3px 8px #000;
}


.control .key {

    font-size: 16px;
}


.control .label {

    margin-top: 2px;

    color: #aaa;

    font-size: 8px;
}


/* =========================
   HINT
========================= */

#hint {

    position: absolute;

    z-index: 70;

    left: 50%;
    bottom: 70px;

    transform:
        translateX(-50%);

    color: #ddd;

    background:
        rgba(0,0,0,.65);

    padding:
        8px 17px;

    border-radius:
        16px;

    font-size:
        11px;

    white-space:
        nowrap;
}


/* =========================
   START
========================= */

#start {

    position: absolute;

    z-index: 250;

    inset: 0;

    display: flex;

    align-items: center;
    justify-content: center;

    flex-direction: column;

    background:
        rgba(3,4,7,.86);
}


#start h1 {

    margin: 0;

    color: white;

    font-size: 57px;

    font-weight: 1000;

    letter-spacing: 5px;

    text-shadow:
        0 7px 25px #000;
}


#start p {

    color: #aaa;

    margin:
        10px 0 28px;
}


button {

    border: 0;

    border-radius: 5px;

    padding:
        14px 45px;

    background:
        linear-gradient(
            #e83b48,
            #921321
        );

    color: white;

    font-size: 20px;

    font-weight: 1000;

    cursor: pointer;

    box-shadow:
        0 6px 20px rgba(0,0,0,.5);
}


button:hover {

    filter:
        brightness(1.2);
}


/* =========================
   FLASH
========================= */

#flash {

    position: absolute;

    z-index: 180;

    inset: 0;

    background: white;

    pointer-events: none;

    opacity: 0;
}


#flash.active {

    animation:
        flash .09s;
}


@keyframes flash {

    from {
        opacity: .42;
    }

    to {
        opacity: 0;
    }
}


/* =========================
   MOBILE
========================= */

@media(max-width:800px) {

    #game {
        height: 700px;
    }

    #controls {
        gap: 2px;
    }

    .control {
        width: 45px;
        height: 42px;
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
        font-size: 34px;
    }
}

</style>
</head>


<body>


<div id="game">


<canvas id="canvas"></canvas>


<div id="floor"></div>

<div id="floorLine"></div>


<!-- HUD -->

<div id="hud">

    <div class="name">
        BLUE
    </div>

    <div class="hp">

        <div
            id="playerHP"
            class="hpBar">
        </div>

    </div>


    <div id="timer">
        60
    </div>


    <div class="hp">

        <div
            id="cpuHP"
            class="hpBar">
        </div>

    </div>


    <div class="name right">
        RED
    </div>

</div>


<!-- COMBO -->

<div id="combo">
    3 HIT COMBO
</div>


<div id="hitText">
    MIDDLE
</div>


<div id="flash"></div>


<div id="message"></div>


<!-- CONTROLS -->

<div id="controls">

    <div class="control">
        <div class="key">W</div>
        <div class="label">JUMP</div>
    </div>

    <div class="control">
        <div class="key">A</div>
        <div class="label">BACK</div>
    </div>

    <div class="control">
        <div class="key">S</div>
        <div class="label">CROUCH</div>
    </div>

    <div class="control">
        <div class="key">D</div>
        <div class="label">FORWARD</div>
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
    W 점프 · A 뒤로 · S 앉기 · D 앞으로 · DD 대시 · AA 백대시 · J 왼손 · K 오른손 · U 어퍼 · I 앞발차기 · O 하단발차기 · SPACE 가드
</div>


<!-- START -->

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
    document.getElementById(
        "game"
    );


const canvas =
    document.getElementById(
        "canvas"
    );


const ctx =
    canvas.getContext(
        "2d"
    );


let W = 1200;
let H = 760;


function resize() {

    const rect =
        game.getBoundingClientRect();


    W =
        rect.width;


    H =
        rect.height;


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


let lastA = 0;

let lastD = 0;


let dashBuffer = 0;

let backBuffer = 0;


document.addEventListener(
    "keydown",
    e => {

        const k =
            e.key.toLowerCase();


        /*
           중복 keydown 방지
        */

        if (!keys[k]) {

            /*
               D D = 대시
            */

            if (k === "d") {

                const now =
                    performance.now();


                if (
                    now - lastD < 280
                ) {

                    dashBuffer = 15;
                }


                lastD = now;
            }


            /*
               A A = 백대시
            */

            if (k === "a") {

                const now =
                    performance.now();


                if (
                    now - lastA < 280
                ) {

                    backBuffer = 15;
                }


                lastA = now;
            }
        }


        keys[k] = true;


        if (
            [
                "w",
                "a",
                "s",
                "d",
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
   ATTACK DATA
========================================================= */

const ATTACKS = {

    leftPunch: {

        name:
            "LEFT PUNCH",

        level:
            "high",

        startup:
            5,

        active:
            4,

        recovery:
            12,

        range:
            125,

        damage:
            5,

        hitstun:
            16,

        guardstun:
            7,

        knockback:
            3,

        cooldown:
            8
    },


    rightPunch: {

        name:
            "RIGHT PUNCH",

        level:
            "high",

        startup:
            7,

        active:
            4,

        recovery:
            14,

        range:
            132,

        damage:
            7,

        hitstun:
            18,

        guardstun:
            8,

        knockback:
            4,

        cooldown:
            10
    },


    uppercut: {

        name:
            "UPPERCUT",

        level:
            "mid",

        startup:
            12,

        active:
            6,

        recovery:
            23,

        range:
            135,

        damage:
            10,

        hitstun:
            40,

        guardstun:
            12,

        knockback:
            5,

        cooldown:
            28,

        launcher:
            true
    },


    frontKick: {

        name:
            "FRONT KICK",

        level:
            "mid",

        startup:
            10,

        active:
            6,

        recovery:
            18,

        range:
            150,

        damage:
            9,

        hitstun:
            23,

        guardstun:
            10,

        knockback:
            6,

        cooldown:
            18
    },


    lowKick: {

        name:
            "LOW KICK",

        level:
            "low",

        startup:
            11,

        active:
            6,

        recovery:
            20,

        range:
            138,

        damage:
            7,

        hitstun:
            20,

        guardstun:
            8,

        knockback:
            4,

        cooldown:
            20
    },


    heavyKick: {

        name:
            "HEAVY KICK",

        level:
            "mid",

        startup:
            16,

        active:
            7,

        recovery:
            28,

        range:
            160,

        damage:
            13,

        hitstun:
            29,

        guardstun:
            13,

        knockback:
            9,

        cooldown:
            32
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

        cpu:
            cpu,

        hp:
            100,

        state:
            "idle",

        attack:
            null,

        attackFrame:
            0,

        attackConnected:
            false,

        hitstun:
            0,

        blockstun:
            0,

        airborne:
            false,

        combo:
            0,

        comboTimer:
            0,

        animationTime:
            0,

        dash:
            0,

        backdash:
            0,

        aiAttackCooldown:
            0,

        aiGuard:
            0,

        /*
           기술 쿨타임
        */

        cooldowns: {

            leftPunch: 0,

            rightPunch: 0,

            uppercut: 0,

            frontKick: 0,

            lowKick: 0,

            heavyKick: 0
        }
    };
}


let player;

let cpu;


let running =
    false;


let gameTime =
    60;


let secondTimer =
    0;


let lastTime =
    0;


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
            W * .25,
            false
        );


    cpu =
        makeFighter(
            W * .75,
            true
        );


    gameTime =
        60;


    secondTimer =
        0;


    dashBuffer =
        0;


    backBuffer =
        0;


    running =
        true;


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
   UTILS
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


function distance(
    a,
    b
) {

    return Math.abs(
        a.x - b.x
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
   COOLDOWN
========================================================= */

function updateCooldowns(f) {

    for (
        const key in f.cooldowns
    ) {

        if (
            f.cooldowns[key] > 0
        ) {

            f.cooldowns[key]--;
        }
    }
}


/* =========================================================
   ATTACK START
========================================================= */

function startAttack(
    f,
    type
) {

    if (!running)
        return false;


    if (
        f.hitstun > 0 ||
        f.blockstun > 0 ||
        f.attack ||
        f.dash > 0 ||
        f.backdash > 0 ||
        f.airborne
    ) {

        return false;
    }


    /*
       쿨타임
    */

    if (
        f.cooldowns[type] > 0
    ) {

        return false;
    }


    f.attack =
        type;


    f.attackFrame =
        0;


    f.attackConnected =
        false;


    /*
       공격 쿨타임 시작
    */

    f.cooldowns[type] =
        ATTACKS[type].cooldown;


    return true;
}


/* =========================================================
   ATTACK ACTIVE
========================================================= */

function attackActive(f) {

    if (!f.attack)
        return false;


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

    if (!f.attack)
        return false;


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

    if (
        f.hitstun > 0
    )
        return false;


    if (
        f.attack
    )
        return false;


    if (
        f.airborne
    )
        return false;


    if (
        f.cpu
    ) {

        return f.aiGuard > 0;
    }


    return keys[" "];
}


/* =========================================================
   HIT CHECK
========================================================= */

function inRange(
    attacker,
    defender
) {

    const a =
        ATTACKS[
            attacker.attack
        ];


    if (!a)
        return false;


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


    return (
        direction ===
        attacker.facing
    );
}


/* =========================================================
   GUARD LOGIC
========================================================= */

function getGuardResult(
    defender,
    attack
) {

    /*
       HIGH

       S를 누르고 있으면
       상단 공격을 피할 수 있음
    */

    if (
        attack.level === "high"
    ) {

        if (
            !defender.cpu &&
            keys["s"]
        ) {

            return "evade";
        }


        return isGuarding(
            defender
        );
    }


    /*
       MID

       서서 가드
    */

    if (
        attack.level === "mid"
    ) {

        return isGuarding(
            defender
        );
    }


    /*
       LOW

       앉아서 방어
    */

    if (
        attack.level === "low"
    ) {

        if (
            defender.cpu
        ) {

            return (
                defender.aiGuard > 0
            );
        }


        return (
            keys[" "] &&
            keys["s"]
        );
    }


    return false;
}


/* =========================================================
   RESOLVE HIT
========================================================= */

function resolveHit(
    attacker,
    defender
) {

    if (
        attacker.attackConnected
    )
        return;


    if (
        !inRange(
            attacker,
            defender
        )
    )
        return;


    attacker.attackConnected =
        true;


    const attack =
        ATTACKS[
            attacker.attack
        ];


    const guard =
        getGuardResult(
            defender,
            attack
        );


    /*
       HIGH CRUSH
    */

    if (
        guard === "evade"
    ) {

        showHitText(
            "HIGH CRUSH",
            "#61dfff"
        );


        spawnImpact(
            defender.x,
            H - 245,
            "#61dfff"
        );


        return;
    }


    /*
       GUARD
    */

    if (guard) {

        defender.blockstun =
            attack.guardstun;


        defender.state =
            "guard";


        showHitText(
            "GUARD",
            "#61dfff"
        );


        spawnImpact(
            defender.x,
            H - 250,
            "#62dfff"
        );


        return;
    }


    /*
       DAMAGE
    */

    let damage =
        attack.damage;


    /*
       공중 콤보 데미지 감소
    */

    if (
        defender.airborne
    ) {

        damage *=
            Math.pow(
                .91,
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
        attack.hitstun;


    defender.vx =
        attacker.facing *
        attack.knockback;


    defender.state =
        "hit";


    attacker.combo++;


    attacker.comboTimer =
        60;


    /*
       LAUNCHER
    */

    if (
        attack.launcher &&
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
            "#ffe34f"
        );

    } else {

        showHitText(
            attack.name,
            "#ffe34f"
        );
    }


    spawnImpact(
        defender.x,
        H - 235 - defender.y,
        "#ffe34f"
    );


    flashScreen();
}


/* =========================================================
   UPDATE ATTACK
========================================================= */

function updateAttack(
    f,
    opponent
) {

    if (!f.attack)
        return;


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

        f.attack =
            null;


        f.attackFrame =
            0;


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
    )
        return;


    f.dash =
        10;


    f.state =
        "dash";
}


function startBackdash(f) {

    if (
        f.hitstun > 0 ||
        f.blockstun > 0 ||
        f.attack ||
        f.airborne
    )
        return;


    f.backdash =
        13;


    f.state =
        "backdash";
}


/* =========================================================
   PLAYER
========================================================= */

function updatePlayer() {

    faceOpponent(
        player,
        cpu
    );


    /*
       피격 경직
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

                player.y =
                    0;


                player.vy =
                    0;


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

        player.vy -=
            .65;


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

            player.y =
                0;


            player.vy =
                0;


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
       DD DASH
    */

    if (
        dashBuffer > 0
    ) {

        startDash(
            player
        );


        dashBuffer =
            0;
    }


    /*
       AA BACKDASH
    */

    if (
        backBuffer > 0
    ) {

        startBackdash(
            player
        );


        backBuffer =
            0;
    }


    /*
       DASH
    */

    if (
        player.dash > 0
    ) {

        player.dash--;


        player.x +=
            player.facing *
            11;


        player.state =
            "dash";


        return;
    }


    /*
       BACKDASH
    */

    if (
        player.backdash > 0
    ) {

        player.backdash--;


        player.x -=
            player.facing *
            9;


        player.state =
            "backdash";


        return;
    }


    /*
       W = JUMP
    */

    if (
        keys["w"]
    ) {

        player.vy =
            13;


        player.airborne =
            true;


        player.state =
            "jump";


        return;
    }


    /*
       ATTACKS
    */

    if (
        keys["j"]
    ) {

        if (
            startAttack(
                player,
                "leftPunch"
            )
        )
            return;
    }


    if (
        keys["k"]
    ) {

        if (
            startAttack(
                player,
                "rightPunch"
            )
        )
            return;
    }


    if (
        keys["u"]
    ) {

        if (
            startAttack(
                player,
                "uppercut"
            )
        )
            return;
    }


    if (
        keys["i"]
    ) {

        if (
            startAttack(
                player,
                "frontKick"
            )
        )
            return;
    }


    if (
        keys["o"]
    ) {

        if (
            startAttack(
                player,
                "lowKick"
            )
        )
            return;
    }


    /*
       S = CROUCH
    */

    if (
        keys["s"]
    ) {

        player.state =
            "crouch";


        return;
    }


    /*
       SPACE = GUARD
    */

    if (
        keys[" "]
    ) {

        player.state =
            "guard";


        return;
    }


    /*
       A = BACK
       D = FORWARD
    */

    let moved =
        false;


    if (
        keys["a"]
    ) {

        player.x -=
            5;


        moved =
            true;
    }


    if (
        keys["d"]
    ) {

        player.x +=
            5;


        moved =
            true;
    }


    if (
        moved
    ) {

        player.state =
            "walk";

    } else {

        player.state =
            "idle";
    }


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


    /*
       HIT
    */

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

            cpu.vy -=
                .65;


            cpu.y +=
                cpu.vy;


            if (
                cpu.y <= 0
            ) {

                cpu.y =
                    0;


                cpu.vy =
                    0;


                cpu.airborne =
                    false;
            }
        }


        return;
    }


    /*
       BLOCK
    */

    if (
        cpu.blockstun > 0
    ) {

        cpu.blockstun--;


        cpu.state =
            "guard";


        return;
    }


    /*
       AIR
    */

    if (
        cpu.airborne
    ) {

        cpu.vy -=
            .65;


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

            cpu.y =
                0;


            cpu.vy =
                0;


            cpu.airborne =
                false;
        }


        return;
    }


    /*
       ATTACK
    */

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
       APPROACH
    */

    if (
        d > 160
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
       RANDOM GUARD
    */

    if (
        player.attack &&
        Math.random() < .55
    ) {

        cpu.aiGuard =
            18 +
            Math.floor(
                Math.random() * 25
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


    /*
       AI ATTACK
    */

    const r =
        Math.random();


    let attack;


    if (
        r < .18
    ) {

        attack =
            "leftPunch";

    } else if (
        r < .34
    ) {

        attack =
            "rightPunch";

    } else if (
        r < .50
    ) {

        attack =
            "frontKick";

    } else if (
        r < .66
    ) {

        attack =
            "lowKick";

    } else if (
        r < .82
    ) {

        attack =
            "uppercut";

    } else {

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
            Math.random() * 25
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

    } else {

        player.combo =
            0;
    }


    if (
        cpu.comboTimer > 0
    ) {

        cpu.comboTimer--;

    } else {

        cpu.combo =
            0;
    }
}


function showCombo(f) {

    if (
        f.combo < 2
    )
        return;


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
            700
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
            350
        );
}


/* =========================================================
   PARTICLES
========================================================= */

let particles =
    [];


function spawnImpact(
    x,
    y,
    color
) {

    for (
        let i = 0;
        i < 18;
        i++
    ) {

        particles.push({

            x:
                x,

            y:
                y,

            vx:
                (
                    Math.random() -
                    .5
                ) * 10,

            vy:
                (
                    Math.random() -
                    .5
                ) * 10,

            life:
                15 +
                Math.random() * 20,

            color:
                color,

            size:
                2 +
                Math.random() * 4
        });
    }
}


function updateParticles() {

    for (
        const p of particles
    ) {

        p.x +=
            p.vx;


        p.y +=
            p.vy;


        p.vy +=
            .25;


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
   STICKMAN
========================================================= */

function drawStickman(
    f,
    color,
    darkColor
) {

    /*
       화면에서 크게 보이도록
       기존보다 큰 사이즈
    */

    const scale =
        1.45;


    const baseY =
        H - 135 - f.y;


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
       SHADOW
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
        12,
        48,
        15,
        0,
        0,
        Math.PI * 2
    );


    ctx.fill();


    ctx.restore();


    /*
       DEFAULT
    */

    let bodyTilt =
        0;


    let crouch =
        0;


    let leftArm = {

        x: -32,

        y: -73
    };


    let rightArm = {

        x: 32,

        y: -73
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

        const wave =
            Math.sin(
                f.animationTime * .32
            );


        leftLeg.x =
            -18 -
            wave * 22;


        rightLeg.x =
            18 +
            wave * 22;


        leftArm.x =
            -30 +
            wave * 16;


        rightArm.x =
            30 -
            wave * 16;
    }


    /*
       DASH
    */

    if (
        f.state === "dash"
    ) {

        bodyTilt =
            -.2;


        leftArm.x =
            -53;


        leftArm.y =
            -76;


        rightArm.x =
            51;


        rightArm.y =
            -54;


        leftLeg.x =
            -42;


        rightLeg.x =
            35;
    }


    /*
       BACKDASH
    */

    if (
        f.state === "backdash"
    ) {

        bodyTilt =
            .23;


        leftArm.x =
            -49;


        rightArm.x =
            40;


        leftLeg.x =
            -36;


        rightLeg.x =
            39;
    }


    /*
       CROUCH
    */

    if (
        f.state === "crouch"
    ) {

        crouch =
            22;


        leftLeg.x =
            -30;


        rightLeg.x =
            30;
    }


    /*
       GUARD
    */

    if (
        f.state === "guard"
    ) {

        leftArm.x =
            18;


        leftArm.y =
            -104;


        rightArm.x =
            39;


        rightArm.y =
            -94;
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
                -17;


            leftArm.y =
                -70;

        } else {

            leftArm.x =
                73;


            leftArm.y =
                -86;


            bodyTilt =
                -.07;
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
                82;


            rightArm.y =
                -74;


            bodyTilt =
                -.11;
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
            54;


        rightArm.y =
            -119;


        leftArm.x =
            -27;


        leftArm.y =
            -75;


        bodyTilt =
            -.10;
    }


    /*
       FRONT KICK
    */

    if (
        f.state === "attack" &&
        f.attack === "frontKick"
    ) {

        rightLeg.x =
            72;


        rightLeg.y =
            -8;


        bodyTilt =
            -.13;
    }


    /*
       LOW KICK
    */

    if (
        f.state === "attack" &&
        f.attack === "lowKick"
    ) {

        crouch =
            14;


        rightLeg.x =
            72;


        rightLeg.y =
            27;


        bodyTilt =
            -.16;
    }


    /*
       HEAVY KICK
    */

    if (
        f.state === "attack" &&
        f.attack === "heavyKick"
    ) {

        rightLeg.x =
            82;


        rightLeg.y =
            -24;


        bodyTilt =
            -.20;
    }


    /*
       HIT
    */

    if (
        f.state === "hit"
    ) {

        bodyTilt =
            -.27;


        leftArm.x =
            -50;


        leftArm.y =
            -59;


        rightArm.x =
            45;


        rightArm.y =
            -54;


        leftLeg.x =
            -34;


        rightLeg.x =
            34;
    }


    /*
       BODY ROTATION
    */

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
        15;


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
        21;


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
        21,
        0,
        Math.PI * 2
    );


    ctx.fill();


    /*
       ARMS
    */

    ctx.lineWidth =
        14;


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
        9,
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

    if (!f.attack)
        return;


    if (!attackActive(f))
        return;


    const attack =
        ATTACKS[
            f.attack
        ];


    let color;


    if (
        attack.level === "high"
    ) {

        color =
            "#ffd34d";

    } else if (
        attack.level === "mid"
    ) {

        color =
            "#59ddff";

    } else {

        color =
            "#ff5d8d";
    }


    ctx.save();


    ctx.translate(
        f.x,
        H - 135 - f.y
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
        7;


    ctx.beginPath();


    if (
        attack.level === "low"
    ) {

        ctx.arc(
            42,
            -43,
            53,
            -.2,
            1.25
        );

    } else {

        ctx.arc(
            48,
            -76,
            55,
            -.95,
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
       벽 기둥
    */

    for (
        let i = 0;
        i < 11;
        i++
    ) {

        const x =
            i * W / 10;


        ctx.fillStyle =
            "rgba(0,0,0,.13)";


        ctx.fillRect(
            x,
            90,
            24,
            H - 230
        );
    }


    /*
       바닥 원근선
    */

    ctx.strokeStyle =
        "rgba(255,255,255,.045)";


    ctx.lineWidth =
        1;


    for (
        let y = H - 130;
        y < H;
        y += 31
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


    /*
       중앙선
    */

    ctx.strokeStyle =
        "rgba(255,200,80,.12)";


    ctx.lineWidth =
        2;


    ctx.beginPath();


    ctx.moveTo(
        W / 2,
        H - 133
    );


    ctx.lineTo(
        W / 2,
        H
    );


    ctx.stroke();
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
            Math.max(
                0,
                p.life / 30
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


    ctx.globalAlpha =
        1;


    if (player) {

        drawStickman(
            player,
            "#246BFF",
            "#123C9C"
        );


        drawAttackEffect(
            player
        );
    }


    if (cpu) {

        drawStickman(
            cpu,
            "#ED273B",
            "#8F1221"
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

    if (!player)
        return;


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

    secondTimer +=
        dt;


    if (
        secondTimer >= 1000
    ) {

        secondTimer -=
            1000;


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

        player.hp =
            0;


        gameOver(
            "RED WINS!"
        );


        return true;
    }


    if (
        cpu.hp <= 0
    ) {

        cpu.hp =
            0;


        gameOver(
            "BLUE WINS!"
        );


        return true;
    }


    return false;
}


function gameOver(
    text
) {

    running =
        false;


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
   GAME LOOP
========================================================= */

function update(dt) {

    updateCooldowns(
        player
    );


    updateCooldowns(
        cpu
    );


    updatePlayer();


    updateCPU();


    updateCombos();


    updateParticles();


    updateTimer(
        dt
    );


    if (
        dashBuffer > 0
    ) {

        dashBuffer--;
    }


    if (
        backBuffer > 0
    ) {

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


    lastTime =
        now;


    update(
        dt
    );


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
    height=780,
    scrolling=False
)
