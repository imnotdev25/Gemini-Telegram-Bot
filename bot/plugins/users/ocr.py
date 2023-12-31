import aiofiles
import os

from pyrogram.types import Message
from pyrogram import Client, filters
# from bot.helpers.decorators import ratelimiter
from bot.helpers.ocr import ocrImg
from bot.helpers.functions import random_string


@Client.on_message(filters.command(["ocr", "read"]))
async def ocr(_, message: Message):
    """ OCR """

    ocr_usage = f"**Usage:** ocr. Reply to an image or just type the text after command. \n\n**Image to Text.** \n\n**Example:** /ocr type your text"
    ocr_reply = await message.reply_text("...", quote=True)
    replied_message = message.reply_to_message

    if len(message.command) > 1:
        await message.reply_text(ocr_usage)
    elif replied_message.document and any(
            formatz in replied_message.document.mime_type for formatz in {"png", "jpg", "jpeg", "webp"}):
        content = await message.reply_to_message.download(os.path.join(os.getcwd(), f"{random_string(10)}.{replied_message.document.mime_type}"))
        r = await ocrImg(content)
        await ocr_reply.edit(r)
    elif replied_message.media.PHOTO:
        content = await message.reply_to_message.download(os.path.join(os.getcwd(), f"{random_string(10)}.jpg"))
        r = await ocrImg(content)
        await message.reply_text(r)
    else:
        return await ocr_reply.edit(ocr_usage)
