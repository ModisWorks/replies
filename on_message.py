import logging

from modis import main
from modis.tools import data

logger = logging.getLogger(__name__)


async def on_message(msgobj):
    """The on_message event handler for this module

    Args:
        msgobj (discord.Message): Input message
    """

    # Only reply to guild messages and don't reply to myself
    if msgobj.guild is None or msgobj.author == main.client.user:
        return

    # Retrieve replies from guild data
    normal_replies = data.cache["guilds"][str(msgobj.guild.id)]["modules"]["replies"]["normal"]
    tts_replies = data.cache["guilds"][str(msgobj.guild.id)]["modules"]["replies"]["tts"]

    # Check normal replies
    for r in normal_replies.keys():
        if r in msgobj.content.lower().replace(' ', ''):
            await msgobj.channel.trigger_typing()
            await msgobj.channel.send(normal_replies[r])

    # Check tts replies
    for r in tts_replies.keys():
        if r in msgobj.content.lower().replace(' ', ''):
            await msgobj.channel.trigger_typing()
            await msgobj.channel.send(tts_replies[r], tts=True)
