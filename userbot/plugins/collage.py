# collage plugin for LionX by @TeamLionX

# Copyright (C) 2020 Alfiananda P.A
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.import os

import os

from userbot import lionx

from ..funcs.managers import eod, eor
from ..helpers import _lionxutils, reply_id
from . import make_gif

plugin_type = "utils"


@lionx.lion_cmd(
    pattern="collage(?:\s|$)([\s\S]*)",
    command=("collage", plugin_type),
    info={
        "header": "To create collage from still images extracted from video/gif.",
        "description": "Shows you the grid image of images extracted from video/gif. you can customize the Grid size by giving integer between 1 to 9 to cmd by default it is 3",
        "usage": "{tr}collage <1-9> <reply to  ani sticker/mp4.",
    },
)
async def collage(event):
    "To create collage from still images extracted from video/gif."
    lionxinput = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    lionxid = await reply_id(event)
    event = await eor(event, "```Wait A Minute Its Collaging😁```")
    if not (reply and (reply.media)):
        await event.edit("`Media not found...`")
        return
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    lionxsticker = await reply.download_media(file="./temp/")
    if not lionxsticker.endswith((".mp4", ".mkv", ".tgs")):
        os.remove(lionxsticker)
        await event.edit("`Media format is not supported...`")
        return
    if lionxinput:
        if not lionxinput.isdigit():
            os.remove(lionxsticker)
            await event.edit("`You input is invalid, check help`")
            return
        lionxinput = int(lionxinput)
        if not 0 < lionxinput < 10:
            os.remove(lionxsticker)
            await event.edit(
                "`Why too big grid you cant see images, use size of grid between 1 to 9`"
            )
            return
    else:
        lionxinput = 3
    if lionxsticker.endswith(".tgs"):
        hmm = await make_gif(event, lionxsticker)
        if hmm.endswith(("@tgstogifbot")):
            os.remove(lionxsticker)
            return await event.edit(hmm)
        collagefile = hmm
    else:
        collagefile = lionxsticker
    endfile = "./temp/collage.png"
    lionxcmd = f"vcsi -g {lionxinput}x{lionxinput} '{collagefile}' -o {endfile}"
    stdout, stderr = (await _lionxutils.runcmd(lionxcmd))[:2]
    if not os.path.exists(endfile):
        for files in (lionxsticker, collagefile):
            if files and os.path.exists(files):
                os.remove(files)
        return await eod(
            event, "`media is not supported or try with smaller grid size`", 5
        )

    await event.client.send_file(
        event.chat_id,
        endfile,
        reply_to=lionxid,
    )
    await event.delete()
    for files in (lionxsticker, collagefile, endfile):
        if files and os.path.exists(files):
            os.remove(files)
