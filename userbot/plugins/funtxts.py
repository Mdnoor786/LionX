import nekos

from userbot import lionx

from ..funcs.managers import eor

plugin_type = "fun"


@lionx.lion_cmd(
    pattern="why$",
    command=("why", plugin_type),
    info={
        "header": "Sends you some random Funny questions",
        "usage": "{tr}why",
    },
)
async def hmm(lionx):
    "Some random Funny questions"
    lol = nekos.why()
    await eor(lionx, lol)


@lionx.lion_cmd(
    pattern="fact$",
    command=("fact", plugin_type),
    info={
        "header": "Sends you some random facts",
        "usage": "{tr}fact",
    },
)
async def hmm(lionx):
    "Some random facts"
    tol = nekos.fact()
    await eor(lionx, tol)
