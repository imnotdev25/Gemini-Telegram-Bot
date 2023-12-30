import aiofiles
import os

from pyrogram.types import Message
from pyrogram import Client, filters
# from bot.helpers.decorators import ratelimiter
from bot.helpers.ai import pyAssistant, dsAssist, codeAssistant
from bot.helpers.filters import allowed_chat, allowed_users, dev_cmd


@Client.on_message(filters.command(["pyassistant", "pya", "pyassist", "pybot", "python"]))
async def pyassistant(_, message: Message):
    """ Python Assistant"""

    py_usage = f"**Usage:** python assistant. Reply to a text file, text message or just type the text after command. \n\n**Code Generation. Rewrite. Debug.** \n\n**Example:** /python type your text"
    py_reply = await message.reply_text("...", quote=True)
    replied_message = message.reply_to_message

    if len(message.command) > 1:
        content = message.text.split(None, 1)[1]

    elif replied_message:
        if replied_message.text:
            content = replied_message.text

        elif replied_message.document and any(
                formatz in replied_message.document.mime_type for formatz in {"text", "json"}):

            await message.reply_to_message.download(os.path.join(os.getcwd(), "temp_file"))
            async with aiofiles.open("temp_file", "r+") as file:
                content = await file.read()
            os.remove("temp_file")

        else:
            return await py_reply.edit(py_usage)

    elif len(message.command) < 2:
        return await py_reply.edit(py_usage)

    output = await pyAssistant(content)
    return await py_reply.edit(f"{output}", disable_web_page_preview=True)


@Client.on_message(filters.command(["dsassistant", "dsa", "dsassist", "dsbot", "ds"]))
async def dsAssistant(_, message: Message):
    """ Data Science Assistant"""

    ds_usage = f"**Usage:** data science assistant. Reply to a text file, text message or just type the text after command. \n\n**Data Science. Machine Learning. Deep Learning.** \n\n**Example:** /ds type your text"
    ds_reply = await message.reply_text("...", quote=True)
    replied_message = message.reply_to_message

    if len(message.command) > 1:
        content = message.text.split(None, 1)[1]

    elif replied_message:
        if replied_message.text:
            content = replied_message.text

        elif replied_message.document and any(
                formatz in replied_message.document.mime_type for formatz in {"text", "json"}):

            await message.reply_to_message.download(os.path.join(os.getcwd(), "temp_file"))
            async with aiofiles.open("temp_file", "r+") as file:
                content = await file.read()
            os.remove("temp_file")

        else:
            return await ds_reply.edit(ds_usage)

    elif len(message.command) < 2:
        return await ds_reply.edit(ds_usage)

    output = await dsAssist(content)
    return await ds_reply.edit(f"{output}", disable_web_page_preview=True)


@Client.on_message(filters.command(["codeassistant", "codea", "codeassist", "codebot", "code"]))
async def codAssistant(_, message: Message):
    """ Code Assistant"""

    code_usage = f"**Usage:** code assistant. Reply to a text file, text message or just type the text after command. \n\n**Code Generation. Rewrite. Debug.** \n\n**Example:** /code type your text"
    code_reply = await message.reply_text("...", quote=True)
    replied_message = message.reply_to_message

    if len(message.command) > 1:
        content = message.text.split(None, 1)[1]

    elif replied_message:
        if replied_message.text:
            content = replied_message.text

        elif replied_message.document and any(
                formatz in replied_message.document.mime_type for formatz in {"text", "json"}):

            await message.reply_to_message.download(os.path.join(os.getcwd(), "temp_file"))
            async with aiofiles.open("temp_file", "r+") as file:
                content = await file.read()
            os.remove("temp_file")

        else:
            return await code_reply.edit(code_usage)

    elif len(message.command) < 2:
        return await code_reply.edit(code_usage)

    output = await codeAssistant(content)
    return await code_reply.edit(f"{output}", disable_web_page_preview=True)
