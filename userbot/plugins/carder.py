from faker import Faker

from . import eor, lionx

plugin_type = "useless"


@lionx.lion_cmd(
    pattern="gencc(?:\s|$)([\s\S]*)",
    command=("gencc", plugin_type),
    info={
        "header": "Carbon generators for given text (Fixed style)",
        "usage": [
            "{tr}carbon <text>",
            "{tr}carbon <reply to text>",
        ],
    },
)
async def _(LIONXevent):
    if LIONXevent.fwd_from:
        return
    LIONXcc = Faker()
    LIONXname = LIONXcc.name()
    LIONXadre = LIONXcc.address()
    LIONXcard = LIONXcc.credit_card_full()

    await eor(
        LIONXevent,
        f"__**👤 NAME :- **__\n`{LIONXname}`\n\n__**🏡 ADDRESS :- **__\n`{LIONXadre}`\n\n__**💸 CARD :- **__\n`{LIONXcard}`",
    )
