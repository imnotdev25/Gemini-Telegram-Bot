import os

import aiofiles
from pyrogram import Client, filters
from pyrogram.types import Message

# from bot.helpers.decorators import ratelimiter
from bot.helpers.ai import stableDiffusion, deepaiImg, deepaiLogo, dreamShaper, stableDiffusionIn
from bot.helpers.filters import allowed_users


@Client.on_message(filters.command(["imagine", "im", "imgen"]))
async def imGen(_, message: Message):
    """ Imagine Generator"""

    imGen_usage = f"**Usage:** imagine generator. Reply to a text file, text message or just type the text after command. \n\n**Image Generation. AI.** \n\n**Example:** /imagine Hot Burger"
    imGen_reply = await message.reply_text("...", quote=True)
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
            return await imGen_reply.edit(imGen_usage)

    elif len(message.command) < 2:
        return await imGen_reply.edit(imGen_usage)

    output = await stableDiffusion(content)
    return await message.reply_photo(output) and await imGen_reply.delete() and os.remove(output)


@Client.on_message(filters.command(["deepai", "deep"]) & allowed_users)
async def deepAi(_, message: Message):
    """ Deep AI """

    deepAi_usage = f"**Usage:** deep ai. Reply to a text file, text message or just type the text after command. \n\n**Image Generation. AI.** \n\n**Example:** /deepai type your text"
    deepAi_reply = await message.reply_text("...", quote=True)
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
            return await deepAi_reply.edit(deepAi_usage)

    elif len(message.command) < 2:
        return await deepAi_reply.edit(deepAi_usage)

    output = await deepaiImg(content)
    return (await message.reply_photo(output) and await deepAi_reply.delete()) and os.remove(output)


@Client.on_message(filters.command(["logo", "lo"]) & allowed_users)
async def deepAiLogo(_, message: Message):
    """ Deep AI Logo Generator """

    deepAiLogo_usage = f"**Usage:** deep ai logo generator. Reply to a text file, text message or just type the text after command. \n\n**Image Generation. AI.** \n\n**Example:** /logo type your text"
    deepAiLogo_reply = await message.reply_text("...", quote=True)
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
            return await deepAiLogo_reply.edit(deepAiLogo_usage)

    elif len(message.command) < 2:
        return await deepAiLogo_reply.edit(deepAiLogo_usage)

    output = await deepaiLogo(content)
    return (await message.reply_photo(output) and await deepAiLogo_reply.delete()) and os.remove(output)


@Client.on_message(filters.command(["dream"]))
async def imGen(_, message: Message):
    """ Imagine Generator"""

    imGen_usage = f"**Usage:** imagine generator. Reply to a text file, text message or just type the text after command. \n\n**Image Generation. AI.** \n\n**Example:** /imagine Hot Burger"
    imGen_reply = await message.reply_text("...", quote=True)
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
            return await imGen_reply.edit(imGen_usage)

    elif len(message.command) < 2:
        return await imGen_reply.edit(imGen_usage)

    output = await dreamShaper(content)
    return await message.reply_photo(output) and await imGen_reply.delete() and os.remove(output)


@Client.on_message(filters.command(["imaginev2", "im", "imgen"]))
async def imGen(_, message: Message):
    """ Imagine Generator"""

    imGen_usage = f"**Usage:** imagine generator. Reply to a text file, text message or just type the text after command. \n\n**Image Generation. AI.** \n\n**Example:** /imagine Hot Burger"
    imGen_reply = await message.reply_text("...", quote=True)
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
            return await imGen_reply.edit(imGen_usage)

    elif len(message.command) < 2:
        return await imGen_reply.edit(imGen_usage)

    output = await stableDiffusionIn(content)
    return await message.reply_photo(output) and await imGen_reply.delete() and os.remove(output)
