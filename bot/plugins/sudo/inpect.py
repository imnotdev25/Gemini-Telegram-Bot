from pyrogram.types import Message 
from pyrogram import Client, filters
from pyrogram.errors import MessageTooLong

from bot.helpers.filters import dev_cmd
# from bot.helpers.decorators import ratelimiter
from bot.helpers.pasting_services import katbin_paste


@Client.on_message(filters.command("inspect", "json") & dev_cmd)
async def inspect(_, message: Message):
    """
    inspects the message and give reply in json format.
    """
    
    try:
        return await message.reply_text(message, quote=True)
    except MessageTooLong:
        output = await katbin_paste(message)
        return await message.reply_text(output, quote=True)
