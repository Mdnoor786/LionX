import asyncio
from collections import deque

from . import eor, lionx

plugin_type = "fun"


@lionx.lion_cmd(
    pattern="degi$",
    command=("degi", plugin_type),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}degi",
    },
)
async def _(event):
    event = await eor(event, "degi")
    await event.edit("WO")
    await asyncio.sleep(1.5)
    await event.edit("DegI")
    await asyncio.sleep(1.5)
    await event.edit("TuM")
    await asyncio.sleep(1.5)
    await event.edit("EkbaR")
    await asyncio.sleep(1.5)
    await event.edit("ManG")
    await asyncio.sleep(1.5)
    await event.edit("KaR")
    await asyncio.sleep(1.5)
    await event.edit("ToH")
    await asyncio.sleep(1.5)
    await event.edit("DekhO")
    await asyncio.sleep(1.5)
    await event.edit("Wo DeGi TuM eKbAr MaNg KaR tOh DeKhO😄")


@lionx.lion_cmd(
    pattern="nehi$",
    command=("nehi", plugin_type),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}nehi",
    },
)
async def _(event):
    event = await eor(event, "nehi")
    await event.edit(
        "`Wo PaKkA DeGi Tu ManG KaR ToH DekH\n AuR NaA De To UskI BheN Ko PakaD😚😚`"
    )


@lionx.lion_cmd(
    pattern="hnd$",
    command=("hnd", plugin_type),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}hnd <name>",
    },
)
async def _(event):
    name = event.text[4:]
    animation_interval = 0.5
    animation_ttl = range(6)
    event = await eor(event, "✌️")
    animation_chars = [
        "👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿\n👉🏿                                          👈🏿\n👉🏿                                          👈🏿\n👉🏿                                          👈🏿\n👉🏿                                          👈🏿\n👉🏿                                          👈🏿\n👉🏿                                          👈🏿\n👉🏿                                          👈🏿\n👉🏿                                          👈🏿\n👉🏿                                          👈🏿\n👉🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👈🏿",
        "👇🏾👇🏾👇🏾👇🏾👇🏾👇🏾👇🏾👇🏾👇🏾\n👉🏾                                  👈🏾\n👉🏾                                  👈🏾\n👉🏾                                  👈🏾\n👉🏾                                  👈🏾\n👉🏾                                  👈🏾\n👉🏾                                  👈🏾\n👉🏾                                  👈🏾\n👆🏾👆🏾👆🏾👆🏾👆🏾👆🏾👆🏾👆🏾👆🏾",
        "👇🏽👇🏽👇🏽👇🏽👇🏽👇🏽👇🏽\n👉🏽                        👈🏽\n👉🏽                        👈🏽\n👉🏽                        👈🏽\n👉🏽                        👈🏽\n👉🏽                        👈🏽\n👆🏽👆🏽👆🏽👆🏽👆🏽👆🏽👆🏽",
        "👇🏼👇🏼👇🏼👇🏼👇🏼\n👉🏼              👈🏼\n👉🏼              👈🏼\n👉🏼              👈🏼\n👆🏼👆🏼👆🏼👆🏼👆🏼",
        f"👇🏻👇🏻👇🏻\n{name}\n👆🏻👆🏻👆🏻",
        f"👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿\n👉🏿👇🏾👇🏾👇🏾👇🏾👇🏾👇🏾👇🏾👇🏾👇🏾👈🏿\n👉🏿👉🏾👇🏽👇🏽👇🏽👇🏽👇🏽👇🏽👇🏽👈🏾👈🏿\n👉🏿👉🏾👉🏽👇🏼👇🏼👇🏼👇🏼👇🏼👈🏽👈🏾👈🏿\n👉🏿👉🏾👉🏽👉🏼👇🏻👇🏻👇🏻👈🏼👈🏽👈🏾👈🏿\n👉🏿  {name}  👈🏿\n👉🏿👉🏾👉🏽👉🏼👆🏻👆🏻👆🏻👈🏼👈🏽👈🏾👈🏿\n👉🏿👉🏾👉🏽👆🏼👆🏼👆🏼👆🏼👆🏼👈🏽👈🏾👈🏿\n👉🏿👉🏾👆🏽👆🏽👆🏽👆🏽👆🏽👆🏽👆🏽👈🏾👈🏿\n👉🏿👆🏾👆🏾👆🏾👆🏾👆🏾👆🏾👆🏾👆🏾👆🏾👈🏿\n👉🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👈🏿",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 6])


@lionx.lion_cmd(
    pattern="think$",
    command=("think", plugin_type),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}think",
    },
)
async def _(event):
    "animation command"
    event = await eor(event, "think")
    deq = deque(list("🤔🧐🤔🧐🤔🧐"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@lionx.lion_cmd(
    pattern="lmao$",
    command=("lmao", plugin_type),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}lmao",
    },
)
async def _(event):
    "animation command"
    event = await eor(event, "lmao")
    deq = deque(list("😂🤣😂🤣😂🤣"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@lionx.lion_cmd(
    pattern="nothappy$",
    command=("nothappy", plugin_type),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}nothappy",
    },
)
async def _(event):
    "animation command"
    event = await eor(event, "nathappy")
    deq = deque(list("😁☹️😁☹️😁☹️😁"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@lionx.lion_cmd(
    pattern="clock$",
    command=("clock", plugin_type),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}clock",
    },
)
async def _(event):
    "animation command"
    event = await eor(event, "clock")
    deq = deque(list("🕙🕘🕗🕖🕕🕔🕓🕒🕑🕐🕛"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@lionx.lion_cmd(
    pattern="muah$",
    command=("muah", plugin_type),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}muah",
    },
)
async def _(event):
    "animation command"
    event = await eor(event, "muah")
    deq = deque(list("😗😙😚😚😘"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@lionx.lion_cmd(
    pattern="heart$",
    command=("heart", plugin_type),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}heart",
    },
)
async def _(event):
    "animation command"
    event = await eor(event, "heart")
    deq = deque(list("❤️🧡💛💚💙💜🖤"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@lionx.lion_cmd(
    pattern="gym$",
    command=("gym", plugin_type),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}gym",
    },
)
async def _(event):
    "animation command"
    event = await eor(event, "gym")
    deq = deque(list("🏃‍🏋‍🤸‍🏃‍🏋‍🤸‍🏃‍🏋‍🤸‍"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@lionx.lion_cmd(
    pattern="earth$",
    command=("earth", plugin_type),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}earth",
    },
)
async def _(event):
    "animation command"
    event = await eor(event, "earth")
    deq = deque(list("🌏🌍🌎🌎🌍🌏🌍🌎"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@lionx.lion_cmd(
    pattern="moon$",
    command=("moon", plugin_type),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}moon",
    },
)
async def _(event):
    "animation command"
    event = await eor(event, "moon")
    deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@lionx.lion_cmd(
    pattern="smoon$",
    command=("smoon", plugin_type),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}smoon",
    },
)
async def _(event):
    "animation command"
    event = await eor(event, "smoon")
    animation_interval = 0.2
    animation_ttl = range(101)
    await event.edit("smoon..")
    animation_chars = [
        "🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗",
        "🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘",
        "🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑",
        "🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒",
        "🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓",
        "🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔",
        "🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕",
        "🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 8])


@lionx.lion_cmd(
    pattern="tmoon$",
    command=("tmoon", plugin_type),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}tmoon",
    },
)
async def _(event):
    "animation command"
    event = await eor(event, "tmoon")
    animation_interval = 0.2
    animation_ttl = range(96)
    await event.edit("tmoon..")
    animation_chars = [
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 32])
