from pyrogram import Client, filters
from pyrogram.types import Message

from bot.helpers.pricehistory import get_price_history_text


@Client.on_message(filters.command(["price", "history"]))
async def pricehistory(_, message: Message):
    """ Price History"""
    pricehistory_usage = f"**Usage:** price history. Reply to text message or just type the text after command. \n\n**Price History.** \n\n**Example:** /price link"
    prehistory_reply = await message.reply_text("...", quote=True)
    replied_message = message.reply_to_message
    try:
        if len(message.command) > 1:
            content = replied_message.text.split(None, 1)[1]

        elif replied_message:
            if replied_message.text:
                content = replied_message.text
            else:
                return await prehistory_reply.edit(pricehistory_usage)
        elif len(message.command) < 2:
            return await prehistory_reply.edit(pricehistory_usage)

        output = await get_price_history_text(content)
        return await message.reply_text(output) and await prehistory_reply.delete()

    except Exception as e:
        return await prehistory_reply.edit(f"Something went wrong while getting history. Error: {e}")
