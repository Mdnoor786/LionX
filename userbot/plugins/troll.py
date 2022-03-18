from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import lionx

from ..funcs.managers import eod, eor
from . import reply_id

plugin_type = "fun"


async def mememaker(borg, msg, lol, chat_id, reply_to_id):
    async with borg.conversation("@themememakerbot") as conv:
        try:
            msg = await conv.send_message(msg)
            pic = await conv.get_response()
            await borg.send_read_acknowledge(conv.chat_id)
            await lol.delete()
        except YouBlockedUserError:
            await lol.edit("Please unblock @themememakerbot and try again")
            return
        await borg.send_file(
            chat_id,
            pic,
            reply_to=reply_to_id,
        )
    await borg.delete_messages(conv.chat_id, [msg.id, pic.id])


@lionx.lion_cmd(
    pattern="fox ?([\s\S]*)",
    command=("fox", plugin_type),
    info={
        "header": "fox meme",
        "description": "Send sneeky fox troll",
        "usage": "{tr}fox <text>",
    },
)
async def ll(event):
    "sneeky fox troll"
    reply_to_id = await reply_id(event)
    input_text = event.pattern_match.group(1)
    if not input_text:
        return await eod(event, "`Give me some text to process...`")
    msg = f"/sf {input_text}"
    lol = await eor(event, "```Fox is on your way...```")
    await mememaker(event.client, msg, lol, event.chat_id, reply_to_id)


@lionx.lion_cmd(
    pattern="talkme ?([\s\S]*)",
    command=("talkme", plugin_type),
    info={
        "header": "talk to me meme",
        "description": "Send talk to me troll",
        "usage": "{tr}talkme <text>",
    },
)
async def lsnks(event):
    "talk to me troll"
    reply_to_id = await reply_id(event)
    input_text = event.pattern_match.group(1)
    if not input_text:
        return await eod(event, "`Give me some text to process...`")
    msg = f"/ttm {input_text}"
    lol = await eor(event, "```Wait making your hardcore meme...```")
    await mememaker(event.client, msg, lol, event.chat_id, reply_to_id)


@lionx.lion_cmd(
    pattern="slip ?([\s\S]*)",
    command=("slip", plugin_type),
    info={
        "header": "brain say meme",
        "description": "Send you a sleeping brain meme.",
        "usage": "{tr}slip <text>",
    },
)
async def lsns(event):
    "Sleeping brain meme."
    reply_to_id = await reply_id(event)
    input_text = event.pattern_match.group(1)
    if not input_text:
        return await eod(event, "`Give me some text to process...`")
    msg = f"/bbs {input_text}"
    lol = await eor(event, "```You can't sleep...```")
    await mememaker(event.client, msg, lol, event.chat_id, reply_to_id)


@lionx.lion_cmd(
    pattern="sbob ?([\s\S]*)",
    command=("sbob", plugin_type),
    info={
        "header": "spongebob meme",
        "description": "Send you spongebob meme.",
        "usage": "{tr}sbob <text>",
    },
)
async def lnzkz(event):
    "spongebob troll"
    reply_to_id = await reply_id(event)
    input_text = event.pattern_match.group(1)
    if not input_text:
        return await eod(event, "`Give me some text to process...`")
    msg = f"/sp {input_text}"
    await eor(event, "```Yaah wait for spongebob...```")
    await mememaker(event.client, msg, lionx, event.chat_id, reply_to_id)


@lionx.lion_cmd(
    pattern="child ?([\s\S]*)",
    command=("child", plugin_type),
    info={
        "header": "child meme",
        "description": "Send you child in trash meme.",
        "usage": "{tr}child <text>",
    },
)
async def lzkkz(event):
    "child troll"
    reply_to_id = await reply_id(event)
    input_text = event.pattern_match.group(1)
    if not input_text:
        return await eod(event, "`Give me some text to process...`")
    msg = f"/love {input_text}"
    lol = await eor(event, "```Wait for your son......```")
    await mememaker(event.client, msg, lol, event.chat_id, reply_to_id)


@lionx.lion_cmd(
    pattern="wyaac ?([\s\S]*)",
    command=("wyaac", plugin_type),
    info={
        "header": "yelling",
        "description": "Send you Woman Yelling At A LionX.",
        "usage": "{tr}wyaac <text> ; <text>",
    },
)
async def lzkkz(event):
    "lion troll"
    reply_to_id = await reply_id(event)
    input_text = event.pattern_match.group(1)
    if not input_text:
        return await eod(event, "`Give me some text to process...`")
    msg = f"/wyaac {input_text}"
    lol = await eor(event, "```Wait for your yelling......```")
    await mememaker(event.client, msg, lol, event.chat_id, reply_to_id)


@lionx.lion_cmd(
    pattern="wyaac ?([\s\S]*)",
    command=("wyaac", plugin_type),
    info={
        "header": "yelling",
        "description": "Send you Woman Yelling At A LionX.",
        "usage": "{tr}wyaac <text> ; <text>",
    },
)
async def lzkkz(event):
    "lion troll"
    reply_to_id = await reply_id(event)
    input_text = event.pattern_match.group(1)
    if not input_text:
        return await eod(event, "`Give me some text to process...`")
    msg = f"/wyaac {input_text}"
    lol = await eor(event, "```Wait for your yelling......```")
    await mememaker(event.client, msg, lol, event.chat_id, reply_to_id)


@lionx.lion_cmd(
    pattern="mp ?([\s\S]*)",
    command=("mp", plugin_type),
    info={
        "header": "Monkey Puppet",
        "description": "Send you Monkey Puppet.",
        "usage": "{tr}mp <text>",
    },
)
async def lzkkz(event):
    "Monkey Puppet"
    reply_to_id = await reply_id(event)
    input_text = event.pattern_match.group(1)
    if not input_text:
        return await eod(event, "`Give me some text to process...`")
    msg = f"/mp {input_text}"
    lol = await eor(event, "```Wait for your yelling......```")
    await mememaker(event.client, msg, lol, event.chat_id, reply_to_id)
