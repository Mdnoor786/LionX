from validators.url import url

from userbot import lionx
from userbot.funcs.logger import logging

from ..Config import Config
from ..funcs.managers import eod, eor
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from . import BOTLOG_CHATID

plugin_type = "utils"
LOGS = logging.getLogger(__name__)
cmdhd = Config.HANDLER


vlist = [
    "ABUSE",
    "ABUSE_PIC",
    "ADMIN_PIC",
    "AFKFWD",
    "ALIVE_PIC",
    "ALIVE_EMOJI",
    "ALIVE_TEXT",
    "ALIVE_TEMPLATE",
    "ALLOW_NSFW",
    "EVAL",
    "HELP_EMOJI",
    "HELP_TEXT",
    "HELP_IMG",
    "IALIVE_PIC",
    "PING_IMG",
    "PM_PIC",
    "PM_TEXT",
    "PM_BLOCK",
    "MAX_FLOOD_IN_PMS",
    "START_TEXT",
    "ROWS_IN_HELP",
    "COLUMNS_IN_HELP",
    "CUSTOM_STICKER_PACKNAME",
    "CUSTOM_STICKER_SETNAME",
]

oldvars = {
    "PM_TEXT": "pmpermit_txt",
    "PM_BLOCK": "pmblock",
}


@lionx.lion_cmd(
    pattern="(set|get|del)db(?: |$)([\s\S]*)",
    command=("db", plugin_type),
    info={
        "header": "Set vars in database or Check or Delete",
        "description": "Set , Fetch or Delete values or vars directly in database without restart or heroku vars.\n\nYou can set multiple pics by giving space after links in alive, ialive, pm permit.",
        "flags": {
            "set": "To set new var in database or modify the old var",
            "get": "To show the already existing var value.",
            "del": "To delete the existing value",
        },
        "var name": "**[List of Database Vars]**",
        "usage": [
            "{tr}setdb <var name> <var value>",
            "{tr}getdb <var name>",
            "{tr}deldb <var name>",
        ],
        "examples": [
            "{tr}setdb ALIVE_PIC <pic link>",
            "{tr}setdb ALIVE_PIC <pic link 1> <pic link 2>",
            "{tr}getdb ALIVE_PIC",
            "{tr}deldb ALIVE_PIC",
        ],
    },
)
async def bad(event):  # sourcery no-metrics
    "To manage vars in database"
    cmd = event.pattern_match.group(1).lower()
    vname = event.pattern_match.group(2)
    vnlist = "".join(f"{i}. `{each}`\n" for i, each in enumerate(vlist, start=1))
    if not vname:
        return await eod(
            event, f"**📜 Give correct var name from the list :\n\n**{vnlist}", time=60
        )
    vinfo = None
    if " " in vname:
        vname, vinfo = vname.split(" ", 1)
    reply = await event.get_reply_message()
    if not vinfo and reply:
        vinfo = reply.text
    if vname in vlist:
        if vname in oldvars:
            vname = oldvars[vname]
        if cmd == "set":
            if not vinfo and vname == "ALIVE_TEMPLATE":
                return await eod(
                    event, "**💠 Visit @lionalive for alive template types.**", 60
                )
            if not vinfo:
                return await eod(
                    event, f"Give some values which you want to save for **{vname}**"
                )
            check = vinfo.split(" ")
            for i in check:
                if "PIC" in vname and not url(i):
                    return await eod(event, "**Give me a correct link...**")
            addgvar(vname, vinfo)
            if BOTLOG_CHATID:
                await event.client.send_message(
                    BOTLOG_CHATID,
                    f"#SET_DATAVAR\
                    \n**{vname}** is updated newly in database as below",
                )
                await event.client.send_message(BOTLOG_CHATID, vinfo, silent=True)
            await eod(
                event, f"📜 Value of **{vname}** is changed to :- `{vinfo}`", time=20
            )
        if cmd == "get":
            var_data = gvarstatus(vname)
            await eod(event, f"📜 Value of **{vname}** is  `{var_data}`", time=20)
        elif cmd == "del":
            delgvar(vname)
            if BOTLOG_CHATID:
                await event.client.send_message(
                    BOTLOG_CHATID,
                    f"#DEL_DATAVAR\
                    \n**{vname}** is deleted from database",
                )
            await eod(
                event,
                f"📜 Value of **{vname}** is now deleted & set to default.",
                time=20,
            )
    else:
        await eod(
            event, f"**📜 Give correct var name from the list :\n\n**{vnlist}", time=60
        )


@lionx.lion_cmd(
    pattern="custom (pmpermit|pmblock|startmsg)$",
    command=("custom", plugin_type),
    info={
        "header": "To customize your LionX.",
        "options": {
            "pmpermit": "To customize pmpermit text. ",
            "pmblock": "To customize pmpermit block message.",
            "startmsg": "To customize startmsg of bot when some one started it.",
        },
        "custom": {
            "{mention}": "mention user",
            "{first}": "first name of user",
            "{last}": "last name of user",
            "{fullname}": "fullname of user",
            "{username}": "username of user",
            "{userid}": "userid of user",
            "{my_first}": "your first name",
            "{my_last}": "your last name ",
            "{my_fullname}": "your fullname",
            "{my_username}": "your username",
            "{my_mention}": "your mention",
            "{totalwarns}": "totalwarns",
            "{warns}": "warns",
            "{remwarns}": "remaining warns",
        },
        "usage": "{tr}custom <option> reply",
        "NOTE": "You can set,fetch or delete these by `{tr}setdv` , `{tr}getdv` & `{tr}deldv` as well.",
    },
)
async def custom_LionX(event):
    "To customize your LionX."
    reply = await event.get_reply_message()
    text = None
    if reply:
        text = reply.text
    if text is None:
        return await eod(event, "__Reply to custom text or url__")
    input_str = event.pattern_match.group(1)
    if input_str == "pmpermit":
        addgvar("pmpermit_txt", text)
    if input_str == "pmblock":
        addgvar("pmblock", text)
    if input_str == "startmsg":
        addgvar("START_TEXT", text)
    await eor(event, f"__Your custom {input_str} has been updated__")
    if BOTLOG_CHATID:
        await event.client.send_message(
            BOTLOG_CHATID,
            f"#SET_DATAVAR\
                    \n**{input_str}** is updated newly in database as below",
        )
        await event.client.send_message(BOTLOG_CHATID, text, silent=True)
