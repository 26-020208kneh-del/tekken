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

html,
body {
    margin: 0;
    padding: 0;

    width: 100%;
    height: 100%;

    overflow: hidden;

    background: #08090d;

    font-family:
        Arial,
        sans-serif;
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
            ellipse at 50% 30%,
            rgba(100,120,170,.20),
            transparent 45%
        ),

        linear-gradient(
            #111a2c 0%,
            #253c60 48%,
            #493528 49%,
            #201b1a 52%,
            #090909 100%
        );

    border:
        2px solid #3c414b;

    border-radius: 8px;

    user-select: none;
}


/* ==============================
   배경
============================== */

#backLight {

    position: absolute;

    width: 600px;
    height: 600px;

    left: 50%;
    top: -250px;

    transform:
        translateX(-50%);

    background:

        radial-gradient(
            ellipse,
            rgba(255,255,255,.15),
            transparent 68%
        );

    pointer-events: none;
}


#floorLine {

    position: absolute;

    left: 0;
    right: 0;

    bottom: 124px;

    height: 4px;

    background:
        #c99a43;

    box-shadow:
        0 0 15px
        rgba(255,190,60,.45);
}


#floor {

    position: absolute;

    left: 0;
    right: 0;

    bottom: 0;

    height: 126px;

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

    background-size:
        40px 40px;
}


/* ==============================
   HUD
============================== */

#hud {

    position: absolute;

    z-index: 50;

    left: 20px;
    right: 20px;

    top: 18px;

    display: grid;

    grid-template-columns:
        90px
        1fr
        65px
        1fr
        90px;

    gap: 10px;

    align-items: center;
}


.name {

    color: #fff;

    font-weight: 900;

    font-size: 15px;

    letter-spacing: 1px;
}


.name.right {

    text-align: right;
}


.hp {

    height: 25px;

    background:
        #080808;

    border:
        2px solid #d7d7d7;

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
            #5eff94,
            #139343
        );
}


#cpuHP {

    background:
        linear-gradient(
            #ff6262,
            #b50f24
        );

    float: right;
}


#timer {

    text-align: center;

    color: #fff;

    font-size: 30px;

    font-weight: 1000;
}


/* ==============================
   COMBO
============================== */

#combo {

    position: absolute;

    z-index: 80;

    left: 50%;
    top: 110px;

    transform:
        translateX(-50%)
        scale(.8);

    opacity: 0;

    color: #ffd94d;

    font-size: 38px;

    font-weight: 1000;

    text-shadow:
        0 3px 0 #684b00,
        0 6px 18px #000;

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

    font-size: 19px;

    font-weight: 1000;

    opacity: 0;
}


#hitText.show {

    opacity: 1;
}


/* ==============================
   KO
============================== */

#message {

    position: absolute;

    z-index: 120;

    left: 50%;
    top: 42%;

    transform:
        translate(-50%,-50%);

    color: #fff;

    font-size: 62px;

    font-weight: 1000;

    text-shadow:
        0 5px 25px #000;

    display: none;

    white-space: nowrap;
}


/* ==============================
   SKILL
============================== */

#skills {

    position: absolute;

    z-index: 70;

    left: 50%;
    bottom: 16px;

    transform:
        translateX(-50%);

    display: flex;

    gap: 8px;
}


.skill {

    position: relative;

    width: 66px;
    height: 42px;

    overflow: hidden;

    background:
        #15171b;

    border:
        2px solid #777;

    border-radius: 5px;

    text-align: center;
}


.skill.ready {

    border-color:
        #54e989;

    box-shadow:
        0 0 10px
        rgba(60,255,140,.25);
}


.skill.cooling {

    border-color:
        #e94a4a;
}


.key {

    position: relative;

    z-index: 4;

    line-height: 38px;

    color: white;

    font-weight: 1000;

    font-size: 16px;
}


.cooldown {

    position: absolute;

    z-index: 2;

    left: 0;
    bottom: 0;

    width: 100%;
    height: 0%;

    background:
        rgba(220,30,40,.75);
}


/* ==============================
   안내
============================== */

#hint {

    position: absolute;

    z-index: 60;

    left: 50%;
    bottom: 67px;

    transform:
        translateX(-50%);

    color: #bbb;

    background:
        rgba(0,0,0,.62);

    border-radius: 15px;

    padding:
        7px 17px;

    font-size: 12px;

    white-space: nowrap;
}


/* ==============================
   시작
============================== */

#start {

    position: absolute;

    z-index: 200;

    inset: 0;

    display: flex;

    align-items: center;
    justify-content: center;

    flex-direction: column;

    background:
        rgba(3,4,7,.82);
}


#start h1 {

    margin: 0;

    font-size: 55px;

    font-weight: 1000;

    letter-spacing: 4px;

    color: #fff;
}


#start p {

    margin:
        8px 0 28px;

    color: #999;
}


button {

    border: 0;

    border-radius: 5px;

    padding:
        13px 40px;

    background:
        linear-gradient(
            #ed3c47,
            #941521
        );

    color: #fff;

    font-size: 19px;

    font-weight: 1000;

    cursor: pointer;
}


button:hover {

    filter:
        brightness(1.18);
}


#flash {

    position: absolute;

    z-index: 100;

    inset: 0;

    background: #fff;

    pointer-events: none;

    opacity: 0;
}


#flash.active {

    animation:
        flash .1s;
}


@keyframes flash {

    from {
        opacity: .45;
    }

    to {
        opacity: 0;
    }
}


/* ==============================
   모바일
============================== */

@media(max-width:700px) {

    #game {
        height: 650px;
    }

    #hud {

        grid-template-columns:
            50px
            1fr
            45px
            1fr
            50px;
    }

    .name {

        font-size: 9px;
    }

    #timer {

        font-size: 22px;
    }

    #start h1 {

        font-size: 35px;
    }

    #hint {

        width: 95%;

        white-space: normal;

        text-align: center;

        font-size: 9px;
    }

    .skill {

        width: 55px;
        height: 38px;
    }
}

</style>
</head>


<body>


<div id="game">

    <div id="backLight"></div>


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


    <div id="combo">
        3 HIT COMBO
    </div>


    <div id="hitText">
        MIDDLE
    </div>


    <div id="flash"></div>


    <div id="message"></div>


    <!-- 기술 -->

    <div id="skills">

        <div
            id="highSkill"
            class="skill ready">

            <div class="key">
                A
            </div>

            <div
                id="highCooldown"
                class="cooldown">
            </div>

        </div>


        <div
            id="midSkill"
            class="skill ready">

            <div class="key">
                S
            </div>

            <div
                id="midCooldown"
                class="cooldown">
            </div>

        </div>


        <div
            id="lowSkill"
            class="skill ready">

            <div class="key">
                D
            </div>

            <div
                id="lowCooldown"
                class="cooldown">
            </div>

        </div>


        <div
            id="launcherSkill"
            class="skill ready">

            <div class="key">
                F
            </div>

            <div
                id="launcherCooldown"
                class="cooldown">
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
        · 가만히 있으면 가드

    </div>


    <!-- 시작 -->

    <div id="start">

        <h1>
            IRON FIGHTERS
        </h1>

        <p>
            SIMPLE FIGHTING GAME
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


document.addEventListener(
    "keydown",
    e => {

        const k =
            e.key.toLowerCase();


        keys[k] = true;


        if (
            [
                "arrowleft",
                "arrowright",
                "arrowup",
                "arrowdown",
                " "
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
   공격 데이터
========================================================= */

const ATTACKS = {

    high: {

        level: "high",

        startup: 6,

        active: 4,

        recovery: 13,

        range: 110,

        damage: 6,

        hitstun: 16,

        guardstun: 8,

        knockback: 4,

        cooldown: 12,

        comboScale: .94
    },


    mid: {

        level: "mid",

        startup: 10,

        active: 5,

        recovery: 18,

        range: 125,

        damage: 9,

        hitstun: 22,

        guardstun: 11,

        knockback: 7,

        cooldown: 18,

        comboScale: .93
    },


    low: {

        level: "low",

        startup: 13,

        active: 6,

        recovery: 21,

        range: 115,

        damage: 8,

        hitstun: 20,

        guardstun: 9,

        knockback: 5,

        cooldown: 22,

        comboScale: .92
    },


    launcher: {

        level: "mid",

        startup: 17,

        active: 7,

        recovery: 27,

        range: 120,

        damage: 12,

        hitstun: 38,

        guardstun: 13,

        knockback: 7,

        cooldown: 45,

        comboScale: .88,

        launcher: true
    }
};


/* =========================================================
   캐릭터
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

        knockdown: 0,

        airborne: false,

        combo: 0,

        comboTimer: 0,

        animationTime: 0,

        aiGuard: 0,

        aiAttackCooldown: 0,

        cooldowns: {

            high: 0,

            mid: 0,

            low: 0,

            launcher: 0
        }
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


const skillUI = {

    high: {

        box:
            document.getElementById(
                "highSkill"
            ),

        fill:
            document.getElementById(
                "highCooldown"
            )
    },


    mid: {

        box:
            document.getElementById(
                "midSkill"
            ),

        fill:
            document.getElementById(
                "midCooldown"
            )
    },


    low: {

        box:
            document.getElementById(
                "lowSkill"
            ),

        fill:
            document.getElementById(
                "lowCooldown"
            )
    },


    launcher: {

        box:
            document.getElementById(
                "launcherSkill"
            ),

        fill:
            document.getElementById(
                "launcherCooldown"
            )
    }
};


/* =========================================================
   게임 시작
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


    gameTime = 60;

    secondTimer = 0;

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
   기본 함수
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


function distance(a,b) {

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
    f,
    opponent
) {

    f.facing =
        opponent.x >= f.x
        ? 1
        : -1;
}


/* =========================================================
   가드
========================================================= */

function crouching(f) {

    return (
        f.state === "crouch"
    );
}


function canGuard(
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


    const near =
        distance(
            f,
            opponent
        ) < 180;


    const moving =
        keys["arrowleft"] ||
        keys["arrowright"] ||
        keys["arrowdown"] ||
        keys["arrowup"] ||
        keys["a"] ||
        keys["s"] ||
        keys["d"] ||
        keys["f"];


    return (
        near &&
        !moving
    );
}


/* =========================================================
   공격 시작
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


    if (
        f.cooldowns[type] > 0
    ) {

        if (!f.cpu) {

            showHitText(
                "COOLDOWN",
                "#ff5555"
            );
        }

        return false;
    }


    f.attack =
        type;


    f.attackFrame =
        0;


    f.attackConnected =
        false;


    return true;
}


/* =========================================================
   공격 프레임
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
   공격 범위
========================================================= */

function inRange(
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


    const dir =
        Math.sign(
            defender.x -
            attacker.x
        );


    if (
        dir !==
        attacker.facing
    ) {

        return false;
    }


    if (
        Math.abs(
            attacker.y -
            defender.y
        ) > 95
    ) {

        return false;
    }


    return true;
}


/* =========================================================
   가드 판정
========================================================= */

function guardResult(
    defender,
    attack
) {

    if (
        attack.level === "high"
    ) {

        if (
            crouching(defender)
        ) {

            return "evade";
        }


        return true;
    }


    if (
        attack.level === "mid"
    ) {

        return true;
    }


    if (
        attack.level === "low"
    ) {

        return crouching(
            defender
        );
    }


    return false;
}


/* =========================================================
   피격
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


    const guard =
        guardResult(
            defender,
            a
        );


    /* 하이 크러시 */

    if (
        guard === "evade"
    ) {

        showHitText(
            "HIGH CRUSH",
            "#65d7ff"
        );

        attacker.combo = 0;

        return;
    }


    /* 가드 */

    if (
        guard === true
    ) {

        defender.hp -=
            Math.max(
                1,
                Math.floor(
                    a.damage * .18
                )
            );


        defender.blockstun =
            a.guardstun;


        defender.vx =
            attacker.facing * 2;


        defender.state =
            "guard";


        attacker.combo = 0;


        showHitText(
            a.level.toUpperCase()
            + " GUARD",
            "#61d9ff"
        );


        spawnImpact(
            defender.x,
            H - 230,
            "#6adfff"
        );


        return;
    }


    /* 실제 피격 */

    let damage =
        a.damage;


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
            40;


        showHitText(
            "LAUNCH",
            "#ffe14d"
        );

    }

    else {

        showHitText(
            a.level.toUpperCase(),
            "#ffe14d"
        );
    }


    spawnImpact(
        defender.x,
        H - 220 - defender.y,
        "#ffe14d"
    );


    flashScreen();


    showCombo(
        attacker
    );
}


/* =========================================================
   공격 업데이트
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


    if (
        attackFinished(f)
    ) {

        const type =
            f.attack;


        f.cooldowns[type] =
            ATTACKS[type].cooldown;


        f.attack = null;

        f.attackFrame = 0;

        f.attackConnected =
            false;
    }
}


/* =========================================================
   쿨타임
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
   플레이어
========================================================= */

function updatePlayer() {

    faceOpponent(
        player,
        cpu
    );


    if (
        player.hitstun > 0
    ) {

        player.hitstun--;

        player.x +=
            player.vx;

        player.vx *= .88;

        player.state =
            "hit";


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


    if (
        player.blockstun > 0
    ) {

        player.blockstun--;

        player.x +=
            player.vx;

        player.vx *= .86;

        player.state =
            "guard";

        return;
    }


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


    let moved = false;


    if (
        keys["arrowleft"]
    ) {

        player.x -= 4.5;

        moved = true;
    }


    if (
        keys["arrowright"]
    ) {

        player.x += 4.5;

        moved = true;
    }


    if (
        keys["arrowup"]
    ) {

        player.vy = 12;

        player.airborne =
            true;

        player.state =
            "jump";

        return;
    }


    if (
        keys["arrowdown"]
    ) {

        player.state =
            "crouch";
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
        canGuard(
            player,
            cpu
        )
    ) {

        player.state =
            "guard";
    }


    else if (moved) {

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
            60,
            W - 60
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

        cpu.state =
            "hit";


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

        cpu.x +=
            cpu.vx;

        cpu.vx *= .86;

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


    if (
        cpu.aiGuard > 0
    ) {

        cpu.aiGuard--;

        cpu.state =
            "guard";

        return;
    }


    if (
        d > 135
    ) {

        if (
            cpu.x > player.x
        ) {

            cpu.x -= 2.3;
        }

        else {

            cpu.x += 2.3;
        }


        cpu.state =
            "walk";

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
       플레이어 공격을 보고
       가끔 가드
    */

    if (
        player.attack &&
        Math.random() < .4
    ) {

        cpu.aiGuard =
            20 +
            Math.floor(
                Math.random() * 20
            );

        cpu.state =
            "guard";

        return;
    }


    const attacks = [];


    for (
        const type in cpu.cooldowns
    ) {

        if (
            cpu.cooldowns[type] <= 0
        ) {

            attacks.push(type);
        }
    }


    if (
        attacks.length > 0
    ) {

        /*
           일정 확률로 하단/중단/상단 선택
        */

        const roll =
            Math.random();


        let type;


        if (
            roll < .25
        ) {

            type = "low";
        }

        else if (
            roll < .55
        ) {

            type = "mid";
        }

        else if (
            roll < .82
        ) {

            type = "high";
        }

        else {

            type = "launcher";
        }


        if (
            cpu.cooldowns[type] > 0
        ) {

            type =
                attacks[
                    Math.floor(
                        Math.random()
                        * attacks.length
                    )
                ];
        }


        startAttack(
            cpu,
            type
        );


        cpu.aiAttackCooldown =
            25 +
            Math.floor(
                Math.random() * 25
            );
    }
}


/* =========================================================
   콤보
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
            600
        );
}


/* =========================================================
   텍스트
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
            () => {

                hitTextEl.classList.remove(
                    "show"
                );

            },
            280
        );
}


/* =========================================================
   이펙트
========================================================= */

let particles = [];


function spawnImpact(
    x,
    y,
    color
) {

    for (
        let i = 0;
        i < 14;
        i++
    ) {

        particles.push({

            x: x,

            y: y,

            vx:
                (Math.random() - .5)
                * 9,

            vy:
                (Math.random() - .5)
                * 9,

            life:
                15 +
                Math.random() * 15,

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
   타이머
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
            }

            else if (
                cpu.hp >
                player.hp
            ) {

                gameOver(
                    "RED WINS!"
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
   승리
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
   졸라맨 그리기
========================================================= */

function drawStickman(
    f,
    color,
    darkColor
) {

    /*
       철권 1 느낌을 위해
       캐릭터 전체 크기를 작게 유지
    */

    const scale = 0.78;


    const baseY =
        H - 130 - f.y;


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
        7,
        42,
        12,
        0,
        0,
        Math.PI * 2
    );

    ctx.fill();

    ctx.restore();


    /*
       기본 포즈
    */

    let frontArmX = 28;
    let frontArmY = -72;

    let backArmX = -27;
    let backArmY = -70;

    let frontLegX = 16;
    let backLegX = -16;

    let bodyTilt = 0;

    let crouch = 0;


    /*
       걷기
    */

    if (
        f.state === "walk"
    ) {

        const w =
            Math.sin(
                f.animationTime * .32
            );


        frontLegX =
            16 + w * 18;


        backLegX =
            -16 - w * 18;
    }


    /*
       앉기
    */

    if (
        f.state === "crouch"
    ) {

        crouch = 19;

        frontLegX = 20;

        backLegX = -20;
    }


    /*
       가드
    */

    if (
        f.state === "guard"
    ) {

        frontArmX = 22;

        frontArmY = -88;

        backArmX = 4;

        backArmY = -92;
    }


    /*
       상단 공격
    */

    if (
        f.state === "attack" &&
        f.attack === "high"
    ) {

        const t =
            f.attackFrame;


        if (
            t < 7
        ) {

            frontArmX = 18;

            frontArmY = -70;
        }

        else {

            frontArmX = 63;

            frontArmY = -88;
        }
    }


    /*
       중단 공격
    */

    if (
        f.state === "attack" &&
        f.attack === "mid"
    ) {

        frontArmX = 61;

        frontArmY = -55;

        bodyTilt = .08;
    }


    /*
       하단 공격
    */

    if (
        f.state === "attack" &&
        f.attack === "low"
    ) {

        crouch = 15;

        frontLegX = 48;

        backLegX = -18;
    }


    /*
       런처
    */

    if (
        f.state === "attack" &&
        f.attack === "launcher"
    ) {

        frontArmX = 57;

        frontArmY = -100;

        bodyTilt = -.12;
    }


    /*
       피격
    */

    if (
        f.state === "hit"
    ) {

        bodyTilt = -.28;

        frontArmX = 42;

        frontArmY = -62;

        backArmX = -35;

        backArmY = -55;
    }


    ctx.rotate(
        bodyTilt
    );


    /*
       다리
    */

    ctx.lineCap =
        "round";


    ctx.lineJoin =
        "round";


    ctx.strokeStyle =
        color;


    ctx.lineWidth =
        12;


    /*
       뒤쪽 다리
    */

    ctx.beginPath();

    ctx.moveTo(
        -9,
        -40 + crouch
    );

    ctx.lineTo(
        backLegX,
        35
    );

    ctx.stroke();


    /*
       앞쪽 다리
    */

    ctx.beginPath();

    ctx.moveTo(
        9,
        -40 + crouch
    );

    ctx.lineTo(
        frontLegX,
        35
    );

    ctx.stroke();


    /*
       몸통
    */

    ctx.strokeStyle =
        color;


    ctx.lineWidth =
        16;


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
       머리

       얼굴 없음.
       단순한 원만 사용.
    */

    ctx.fillStyle =
        color;


    ctx.beginPath();

    ctx.arc(
        0,
        -130 + crouch,
        17,
        0,
        Math.PI * 2
    );

    ctx.fill();


    /*
       뒤쪽 팔
    */

    ctx.strokeStyle =
        darkColor;


    ctx.lineWidth =
        11;


    ctx.beginPath();

    ctx.moveTo(
        -10,
        -97 + crouch
    );

    ctx.lineTo(
        backArmX,
        backArmY + crouch
    );

    ctx.stroke();


    /*
       앞쪽 팔
    */

    ctx.strokeStyle =
        color;


    ctx.beginPath();

    ctx.moveTo(
        10,
        -97 + crouch
    );

    ctx.lineTo(
        frontArmX,
        frontArmY + crouch
    );

    ctx.stroke();


    /*
       주먹

       얼굴/눈/코/입 없음.
    */

    ctx.fillStyle =
        color;


    ctx.beginPath();

    ctx.arc(
        frontArmX,
        frontArmY + crouch,
        7,
        0,
        Math.PI * 2
    );

    ctx.fill();


    ctx.restore();
}


/* =========================================================
   공격 이펙트
========================================================= */

function drawAttackEffect(f) {

    if (!f.attack) {
        return;
    }


    if (
        !attackActive(f)
    ) {

        return;
    }


    const a =
        ATTACKS[
            f.attack
        ];


    let color =
        "#fff";


    if (
        a.level === "high"
    ) {

        color =
            "#ffd34d";
    }

    else if (
        a.level === "mid"
    ) {

        color =
            "#58d9ff";
    }

    else {

        color =
            "#ff6487";
    }


    ctx.save();


    ctx.translate(
        f.x,
        H - 130 - f.y
    );


    ctx.scale(
        f.facing,
        1
    );


    ctx.strokeStyle =
        color;


    ctx.lineWidth =
        5;


    ctx.globalAlpha =
        .7;


    ctx.beginPath();


    if (
        a.level === "low"
    ) {

        ctx.arc(
            25,
            -45,
            40,
            -.2,
            1.1
        );
    }

    else {

        ctx.arc(
            45,
            -75,
            45,
            -.9,
            .6
        );
    }


    ctx.stroke();


    ctx.restore();
}


/* =========================================================
   배경
========================================================= */

function drawBackground() {

    /*
       뒤쪽 기둥
    */

    for (
        let i = 0;
        i < 9;
        i++
    ) {

        const x =
            i * W / 8;


        ctx.fillStyle =
            "rgba(0,0,0,.15)";


        ctx.fillRect(
            x,
            90,
            25,
            H - 215
        );
    }


    /*
       경기장 라인
    */

    ctx.strokeStyle =
        "rgba(255,255,255,.035)";


    ctx.lineWidth = 1;


    for (
        let y = H - 125;
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
   렌더
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
       파티클
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

    if (!player) {
        return;
    }


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


    updateSkillUI();
}


/* =========================================================
   기술 UI
========================================================= */

function updateSkillUI() {

    for (
        const type in skillUI
    ) {

        const ui =
            skillUI[type];


        const cd =
            player.cooldowns[type];


        const max =
            ATTACKS[type].cooldown;


        if (
            cd > 0
        ) {

            ui.box.classList.remove(
                "ready"
            );


            ui.box.classList.add(
                "cooling"
            );


            ui.fill.style.height =
                (
                    cd / max * 100
                ) + "%";
        }

        else {

            ui.box.classList.remove(
                "cooling"
            );


            ui.box.classList.add(
                "ready"
            );


            ui.fill.style.height =
                "0%";
        }
    }
}


/* =========================================================
   메인 업데이트
========================================================= */

function update(dt) {

    updatePlayer();

    updateCPU();

    updateCooldowns(player);

    updateCooldowns(cpu);

    updateCombos();

    updateParticles();

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
   게임 루프
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


    lastTime =
        now;


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
