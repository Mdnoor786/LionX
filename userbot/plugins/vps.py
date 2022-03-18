import asyncio
import glob
import os

from userbot import lionxub

from ..funcs.managers import edit_delete, edit_or_reply
from ..helpers.utils import _lionxutils

plugin_category = "tools"


# ============================@ Constants @===============================
config = "./config.py"
var_checker = [
    "APP_ID",
    "PM_LOGGER_GROUP_ID",
    "PRIVATE_CHANNEL_BOT_API_ID",
    "PRIVATE_GROUP_BOT_API_ID",
]
exts = ["jpg", "png", "webp", "webm", "m4a", "mp4", "mp3", "tgs"]

cmds = [
    "rm -rf downloads",
    "mkdir downloads",
]
# ========================================================================


@lionxub.lionx_cmd(
    pattern="(set|get|del) var ([\s\S]*)",
    command=("var", plugin_category),
    info={
        "header": "To manage config vars.",
        "flags": {
            "set": "To set new var in vps or modify the old var",
            "get": "To show the already existing var value.",
            "del": "To delete the existing value",
        },
        "usage": [
            "{tr}set var <var name> <var value>",
            "{tr}get var <var name>",
            "{tr}del var <var name>",
        ],
        "examples": [
            "{tr}get var ALIVE_NAME",
        ],
    },
)
async def variable(event):  # sourcery no-metrics
    """
    Manage most of ConfigVars setting, set new var, get current var, or delete var...
    """
    if not os.path.exists(config):
        return await edit_delete(
            event, "`There no Config file , You can't use this plugin.`"
        )
    cmd = event.pattern_match.group(1)
    string = ""
    match = None
    with open(config, "r") as f:
        configs = f.readlines()
    if cmd == "get":
        lionx = await edit_or_reply(event, "`Getting information...`")
        await asyncio.sleep(1)
        variable = event.pattern_match.group(2).split()[0]
        for i in configs:
            if variable in i:
                return await lionx.edit("**ConfigVars**:" f"\n\n`{i}`")
        await lionx.edit(
            "**ConfigVars**:" f"\n\n__Error:\n-> __`{variable}`__ doesn't exists__"
        )
    elif cmd == "set":
        variable = "".join(event.text.split(maxsplit=2)[2:])
        lionx = await edit_or_reply(event, "`Setting information...`")
        if not variable:
            return await lionx.edit("`.set var <ConfigVars-name> <value>`")
        value = "".join(variable.split(maxsplit=1)[1:])
        variable = "".join(variable.split(maxsplit=1)[0])
        if variable not in var_checker:
            value = f'"{value}"'
        if not value:
            return await lionx.edit("`.set var <ConfigVars-name> <value>`")
        await asyncio.sleep(1)
        for i in configs:
            if variable in i:
                string += f"    {variable} = {value}\n"
                match = True
            else:
                string += f"{i}"
        if match:
            await lionx.edit(f"`{variable}` **successfully changed to  ->  **`{value}`")
        else:
            string += f"    {variable} = {value}\n"
            await lionx.edit(
                f"`{variable}`**  successfully added with value`  ->  **{value}`"
            )
        with open(config, "w") as f1:
            f1.write(string)
            f1.close()
        await event.client.reload(lionx)
    if cmd == "del":
        lionx = await edit_or_reply(event, "`Deleting information...`")
        await asyncio.sleep(1)
        variable = event.pattern_match.group(2).split()[0]
        for i in configs:
            if variable in i:
                match = True
            else:
                string += f"{i}"
        with open(config, "w") as f1:
            f1.write(string)
            f1.close()
        if match:
            await lionx.edit(f"`{variable}` **successfully deleted.**")
        else:
            await lionx.edit(
                "**ConfigVars**:" f"\n\n__Error:\n-> __`{variable}`__ doesn't exists__"
            )
        await event.client.reload(lionx)


@lionxub.lionx_cmd(
    pattern="(re|clean)load$",
    command=("reload", plugin_category),
    info={
        "header": "To reload your bot in vps/ similar to restart",
        "flags": {
            "re": "To set new var in vps or modify the old var",
            "clean": "To show the already existing var value.",
        },
        "usage": [
            "{tr}reload",
            "{tr}cleanload",
        ],
    },
)
async def _(event):
    "To reload Your bot"
    cmd = event.pattern_match.group(1)
    lionx = await edit_or_reply(event, "`Wait 2-3 min, reloading...`")
    if cmd == "clean":
        for file in exts:
            removing = glob.glob(f"./*.{file}")
            for i in removing:
                os.remove(i)
        for i in cmds:
            await _lionxutils.runcmd(i)
    await event.client.reload(lionx)


@lionxub.lionx_cmd(
    pattern="(good|bad)lionx$",
    command=("switch", plugin_category),
    info={
        "header": "To switch between lionx & lionx(For extra nsfw and gali).",
        "usage": [
            "{tr}lionx",
            "{tr}lionx",
        ],
    },
)
async def variable(event):
    "To update to lionx( for extra masala and gali)."
    if not os.path.exists(config):
        return await edit_delete(
            event, "`There no Config file , You can't use this plugin.`"
        )
    string = ""
    match = None
    switch = "LIONX"
    cmd = event.pattern_match.group(1).lower()
    with open(config, "r") as f:
        configs = f.readlines()
    for i in configs:
        if switch in i:
            match = True
        else:
            string += f"{i}"
    if cmd == "good":
        if match:
            lionx = await edit_or_reply(
                event, f"`Changing lionx to lionx wait for 2-3 minutes.`"
            )
            with open(config, "w") as f1:
                f1.write(string)
                f1.close()
            await _lionxutils.runcmd("rm -rf badlionxtext")
            return await event.client.reload(lionx)
        await edit_delete(event, "`You already using LionX`")
    elif cmd == "bad":
        if match:
            return await edit_or_reply(event, "`You already using LionX`")
        string += f'    {switch} = "True"\n'
        lionx = await edit_or_reply(
            event, "`Changing lionx to lionx wait for 2-3 minutes.`"
        )
        with open(config, "w") as f1:
            f1.write(string)
            f1.close()
        await event.client.reload(lionx)