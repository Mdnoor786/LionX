import os

import requests

from userbot import lionx

plugin_type = "useless"


@lionx.lion_cmd(
    pattern="fpic(?:\s|$)([\s\S]*)",
    command=("fpic", plugin_type),
    info={
        "header": "Fake Pic Generation",
        "description": "Fake Pic Generation From UserBot.",
        "usage": "{tr}fpic",
    },
)
async def _(event):
    url = "https://thispersondoesnotexist.com/image"
    response = requests.get(url)
    await event.edit("`Creating a fake face...`")
    if response.status_code == 200:
        with open("LIONX.jpg", "wb") as f:
            f.write(response.content)

    captin = f"Fake Image By LIONX."
    fole = "LIONX.jpg"
    await event.client.send_file(event.chat_id, fole, caption=captin)
    await event.delete()
    os.system("rm /root/userbot/LIONX.jpg ")
