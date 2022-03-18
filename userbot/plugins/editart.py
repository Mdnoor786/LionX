import random

from . import eor, lionx

plugin_type = "fun"


# $$$$$$$$$$$$$$$$$¢$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$¢$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$¢

GENDER = [
    "u is mard",
    "u is man",
    "u is lionxt",
    "u is woman",
    "u is gey",
    "u is chakka",
]

EMOTICONS = [
    "(҂⌣̀_⌣́)",
    "（；¬＿¬)",
    "(-｡-;",
    "┌[ O ʖ̯ O ]┐",
    "〳 ͡° Ĺ̯ ͡° 〵",
]

WAVING = [
    "(ノ^∇^)",
    "(;-_-)/",
    "@(o・ェ・)@ノ",
    "ヾ(＾-＾)ノ",
    "ヾ(◍’౪◍)ﾉﾞ♡",
    "(ό‿ὸ)ﾉ",
    "(ヾ(´・ω・｀)",
]

WTF = [
    "༎ຶ‿༎ຶ",
    "(‿ˠ‿)",
    "╰U╯☜(◉ɷ◉ )",
    "(;´༎ຶ益༎ຶ)♡",
    "╭∩╮(︶ε︶*)chu",
    "( ＾◡＾)っ (‿|‿)",
]

LOB = [
    "乂❤‿❤乂",
    "(｡♥‿♥｡)",
    "( ͡~ ͜ʖ ͡°)",
    "໒( ♥ ◡ ♥ )७",
    "༼♥ل͜♥༽",
]

CONFUSED = [
    "(・_・ヾ",
    "｢(ﾟﾍﾟ)",
    "﴾͡๏̯͡๏﴿",
    "(￣■￣;)!?",
    "▐ ˵ ͠° (oo) °͠ ˵ ▐",
    "(-_-)ゞ゛",
]

DEAD = [
    "(✖╭╮✖)",
    "✖‿✖",
    "(+_+)",
    "(✖﹏✖)",
    "∑(✘Д✘๑)",
]

SED = [
    "(＠´＿｀＠)",
    "⊙︿⊙",
    "(▰˘︹˘▰)",
    "●︿●",
    "(　´_ﾉ` )",
    "彡(-_-;)彡",
]

DOG = [
    "-ᄒᴥᄒ-",
    "◖⚆ᴥ⚆◗",
]

SHRUG = [
    "( ͡° ͜ʖ ͡°)",
    "¯\_(ツ)_/¯",
    "( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)",
    "ʕ•ᴥ•ʔ",
    "(▀ Ĺ̯▀   )",
    "(ง ͠° ͟ل͜ ͡°)ง",
    "༼ つ ◕_◕ ༽つ",
    "ಠ_ಠ",
    "(☞ ͡° ͜ʖ ͡°)☞",
    "¯\_༼ ି ~ ି ༽_/¯",
    "c༼ ͡° ͜ʖ ͡° ༽⊃",
]

# ✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓


@lionx.lion_cmd(
    pattern="gender$",
    command=("gender", plugin_type),
    info={
        "header": "try out yourself to see",
        "usage": "{tr}gender <ur name first letter>",
    },
)
async def metoo(e):
    txt = random.choice(GENDER)
    await eor(e, txt)


@lionx.lion_cmd(
    pattern="shrug$",
    command=("shrug", plugin_type),
    info={
        "header": "try out yourself to see",
        "usage": "{tr}shrug",
    },
)
async def metoo(e):
    txt = random.choice(SHRUG)
    await eor(e, txt)


@lionx.lion_cmd(
    pattern="dome$",
    command=("dome", plugin_type),
    info={
        "header": "try out yourself to see",
        "usage": "{tr}dome <ur name first letter>",
    },
)
async def metoo(e):
    txt = random.choice(DOG)
    await eor(e, txt)


@lionx.lion_cmd(
    pattern="mesed$",
    command=("mesed", plugin_type),
    info={
        "header": "try out yourself to see",
        "usage": "{tr}mesed <ur name first letter>",
    },
)
async def metoo(e):
    txt = random.choice(SED)
    await eor(e, txt)


@lionx.lion_cmd(
    pattern="medead$",
    command=("medead", plugin_type),
    info={
        "header": "try out yourself to see",
        "usage": "{tr}medead <ur name first letter>",
    },
)
async def metoo(e):
    txt = random.choice(DEAD)
    await eor(e, txt)


@lionx.lion_cmd(
    pattern="confused$",
    command=("confused", plugin_type),
    info={
        "header": "try out yourself to see",
        "usage": "{tr}confused <ur name first letter>",
    },
)
async def metoo(e):
    txt = random.choice(CONFUSED)
    await eor(e, txt)


@lionx.lion_cmd(
    pattern="lobb$",
    command=("lobb", plugin_type),
    info={
        "header": "try out yourself to see",
        "usage": "{tr}lobb <ur name first letter>",
    },
)
async def metoo(e):
    txt = random.choice(LOB)
    await eor(e, txt)


@lionx.lion_cmd(
    pattern="wut$",
    command=("wut", plugin_type),
    info={
        "header": "try out yourself to see",
        "usage": "{tr}wut <ur name first letter>",
    },
)
async def metoo(e):
    txt = random.choice(WTF)
    await eor(e, txt)


@lionx.lion_cmd(
    pattern="wave$",
    command=("wave", plugin_type),
    info={
        "header": "try out yourself to see",
        "usage": "{tr}wavea <ur name first letter>",
    },
)
async def metoo(e):
    txt = random.choice(WAVING)
    await eor(e, txt)


@lionx.lion_cmd(
    pattern="hehe$",
    command=("hehe", plugin_type),
    info={
        "header": "try out yourself to see",
        "usage": "{tr}hehe <ur name first letter>",
    },
)
async def metoo(e):
    txt = random.choice(EMOTICONS)
    await eor(e, txt)
