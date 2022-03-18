import random

from userbot import lionx

from ..funcs.managers import eor
from . import swtmemes

plugin_type = "fun"


@lionx.lion_cmd(
    pattern="congo$",
    command=("congo", plugin_type),
    info={
        "header": " Congratulate the people..",
        "usage": "{tr}congo",
    },
)
async def _(e):
    "Congratulate the people."
    txt = random.choice(swtmemes.CONGOREACTS)
    await eor(e, txt)


@lionx.lion_cmd(
    pattern="shg$",
    command=("shg", plugin_type),
    info={
        "header": "Shrug at it !!",
        "usage": "{tr}shg",
    },
)
async def shrugger(e):
    "Shrug at it !!"
    txt = random.choice(swtmemes.SHGS)
    await eor(e, txt)


@lionx.lion_cmd(
    pattern="runs$",
    command=("runs", plugin_type),
    info={
        "header": "Run, run, RUNNN!.",
        "usage": "{tr}runs",
    },
)
async def runner_lol(e):
    "Run, run, RUNNN!"
    txt = random.choice(swtmemes.RUNSREACTS)
    await eor(e, txt)


@lionx.lion_cmd(
    pattern="noob$",
    command=("noob", plugin_type),
    info={
        "header": "Whadya want to know? Are you a NOOB?",
        "usage": "{tr}noob",
    },
)
async def metoo(e):
    "Whadya want to know? Are you a NOOB?"
    txt = random.choice(swtmemes.NOOBSTR)
    await eor(e, txt)


@lionx.lion_cmd(
    pattern="insult$",
    command=("insult", plugin_type),
    info={
        "header": "insult someone.",
        "usage": "{tr}insult",
    },
)
async def insult(e):
    "insult someone."
    txt = random.choice(swtmemes.INSULT_STRINGS)
    await eor(e, txt)


@lionx.lion_cmd(
    pattern="love$",
    command=("love", plugin_type),
    info={
        "header": "Chutiyappa suru",
        "usage": "{tr}love",
    },
)
async def suru(chutiyappa):
    "Chutiyappa suru"
    txt = random.choice(swtmemes.LOVESTR)
    await eor(chutiyappa, txt)


@lionx.lion_cmd(
    pattern="dhoka$",
    command=("dhoka", plugin_type),
    info={
        "header": "Dhokha kha gya",
        "usage": "{tr}dhoka",
    },
)
async def katgya(chutiya):
    "Dhokha kha gya"
    txt = random.choice(swtmemes.DHOKA)
    await eor(chutiya, txt)


@lionx.lion_cmd(
    pattern="hey$",
    command=("hey", plugin_type),
    info={
        "header": "start a conversation with people",
        "usage": "{tr}hey",
    },
)
async def hoi(e):
    "start a conversation with people."
    txt = random.choice(swtmemes.HELLOSTR)
    await eor(e, txt)


@lionx.lion_cmd(
    pattern="pro$",
    command=("pro", plugin_type),
    info={
        "header": "If you think you're pro, try this.",
        "usage": "{tr}pro",
    },
)
async def proo(e):
    "If you think you're pro, try this."
    txt = random.choice(swtmemes.PRO_STRINGS)
    await eor(e, txt)


@lionx.lion_cmd(
    pattern="react ?([\s\S]*)",
    command=("react", plugin_type),
    info={
        "header": "Make your userbot react",
        "flags": [
            "happy",
            "think",
            "wave",
            "wtf",
            "love",
            "confused",
            "dead",
            "sad",
            "dog",
        ],
        "usage": ["{tr}react <type>", "{tr}react"],
    },
)
async def _(e):
    "Make your userbot react."
    input_str = e.pattern_match.group(1)
    if input_str in "happy":
        emoticons = swtmemes.FACEREACTS[0]
    elif input_str in "think":
        emoticons = swtmemes.FACEREACTS[1]
    elif input_str in "wave":
        emoticons = swtmemes.FACEREACTS[2]
    elif input_str in "wtf":
        emoticons = swtmemes.FACEREACTS[3]
    elif input_str in "love":
        emoticons = swtmemes.FACEREACTS[4]
    elif input_str in "confused":
        emoticons = swtmemes.FACEREACTS[5]
    elif input_str in "dead":
        emoticons = swtmemes.FACEREACTS[6]
    elif input_str in "sad":
        emoticons = swtmemes.FACEREACTS[7]
    elif input_str in "dog":
        emoticons = swtmemes.FACEREACTS[8]
    else:
        emoticons = swtmemes.FACEREACTS[9]
    txt = random.choice(emoticons)
    await eor(e, txt)


@lionx.lion_cmd(
    pattern="10iq$",
    command=("10iq", plugin_type),
    info={
        "header": "You retard !!",
        "usage": "{tr}10iq",
    },
)
async def iqless(e):
    "You retard !!"
    await eor(e, "♿")


@lionx.lion_cmd(
    pattern="fp$",
    command=("fp", plugin_type),
    info={
        "header": "send you face pam emoji!",
        "usage": "{tr}fp",
    },
)
async def facepalm(e):
    "send you face pam emoji!"
    await eor(e, "🤦‍♂")


@lionx.lion_cmd(
    pattern="bt$",
    command=("bt", plugin_type),
    info={
        "header": "Believe me, you will find this useful.",
        "usage": "{tr}bt",
    },
    groups_only=True,
)
async def bluetext(e):
    """Believe me, you will find this useful."""
    await eor(
        e,
        "/BLUETEXT /MUST /CLICK.\n"
        "/ARE /YOU /A /STUPID /ANIMAL /WHICH /IS /ATTRACTED /TO /COLOURS?",
    )


@lionx.lion_cmd(
    pattern="session$",
    command=("session", plugin_type),
    info={
        "header": "telethon session error code(fun)",
        "usage": "{tr}session",
    },
)
async def _(event):
    "telethon session error code(fun)."
    mentions = "**telethon.errors.rpcerrorlist.AuthKeyDuplicatedError: The authorization key (session file) was used under two different IP addresses simultaneously, and can no longer be used. Use the same session exclusively, or use different sessions (caused by GetMessagesRequest)**"
    await eor(event, mentions)
