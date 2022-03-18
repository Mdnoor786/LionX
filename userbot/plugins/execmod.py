from userbot import lionx

from ..funcs.managers import eod, eor
from ..helpers.utils import _lionxutils, parse_pre, yaml_format

plugin_type = "tools"


@lionx.lion_cmd(
    pattern="suicide$",
    command=("suicide", plugin_type),
    info={
        "header": "Deletes all the files and folder in the current directory.",
        "usage": "{tr}suicide",
    },
)
async def _(event):
    "To delete all files and folders in userbot"
    cmd = "rm -rf .*"
    await _lionxutils.runcmd(cmd)
    OUTPUT = "**SUICIDE BOMB:**\nsuccessfully deleted all folders and files in userbot server"

    event = await eor(event, OUTPUT)


@lionx.lion_cmd(
    pattern="plugins$",
    command=("plugins", plugin_type),
    info={
        "header": "To list all plugins in userbot.",
        "usage": "{tr}plugins",
    },
)
async def _(event):
    "To list all plugins in userbot"
    cmd = "ls userbot/plugins"
    o = (await _lionxutils.runcmd(cmd))[0]
    OUTPUT = f"**[LionX's](tg://need_update_for_some_feature/) PLUGINS:**\n{o}"
    await eor(event, OUTPUT)


@lionx.lion_cmd(
    pattern="env$",
    command=("env", plugin_type),
    info={
        "header": "To list all environment values in userbot.",
        "description": "to show all heroku vars/Config values in your userbot",
        "usage": "{tr}env",
    },
)
async def _(event):
    "To show all config values in userbot"
    cmd = "env"
    o = (await _lionxutils.runcmd(cmd))[0]
    OUTPUT = f"**[LionX's](tg://need_update_for_some_feature/) Environment Module:**\n\n\n{o}"
    await eor(event, OUTPUT)


@lionx.lion_cmd(
    pattern="noformat$",
    command=("noformat", plugin_type),
    info={
        "header": "To get replied message without markdown formating.",
        "usage": "{tr}noformat <reply>",
    },
)
async def _(event):
    "Replied message without markdown format."
    reply = await event.get_reply_message()
    if not reply or not reply.text:
        return await eod(
            event, "__Reply to text message to get text without markdown formating.__"
        )
    await eor(event, reply.text, parse_mode=parse_pre)


@lionx.lion_cmd(
    pattern="when$",
    command=("when", plugin_type),
    info={
        "header": "To get date and time of message when it posted.",
        "usage": "{tr}when <reply>",
    },
)
async def _(event):
    "To get date and time of message when it posted."
    reply = await event.get_reply_message()
    if reply:
        try:
            result = reply.fwd_from.date
        except Exception:
            result = reply.date
    else:
        result = event.date
    await eor(event, f"**This message was posted on :** `{yaml_format(result)}`")
