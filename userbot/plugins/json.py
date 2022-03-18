from userbot import lionx

from ..funcs.managers import eor
from ..helpers.utils import _format

plugin_type = "tools"

# yaml_format is ported from uniborg
@lionx.lion_cmd(
    pattern="json$",
    command=("json", plugin_type),
    info={
        "header": "To get details of that message in json format.",
        "usage": "{tr}json reply to message",
    },
)
async def _(event):
    "To get details of that message in json format."
    lionxevent = await event.get_reply_message() if event.reply_to_msg_id else event
    the_real_message = lionxevent.stringify()
    await eor(event, the_real_message, parse_mode=_format.parse_pre)


@lionx.lion_cmd(
    pattern="yaml$",
    command=("yaml", plugin_type),
    info={
        "header": "To get details of that message in yaml format.",
        "usage": "{tr}yaml reply to message",
    },
)
async def _(event):
    "To get details of that message in yaml format."
    lionxevent = await event.get_reply_message() if event.reply_to_msg_id else event
    the_real_message = _format.yaml_format(lionxevent)
    await eor(event, the_real_message, parse_mode=_format.parse_pre)
