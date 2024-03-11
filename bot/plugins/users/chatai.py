from pyrogram import Client, filters
from pyrogram.types import Message

# from bot.helpers.decorators import ratelimiter
from bot.helpers.ai import bing, meta, mistral, llama, rewrite, starCoder, codeLLM


@Client.on_message(filters.command(["bing", "bingbot"]))
async def bingBot(_, message: Message):
    """ Bing Bot"""

    bing_usage = f"**Usage:** bing bot. Reply to a text file, text message or just type the text after command. \n\n**Bing Bot.** \n\n**Example:** /bing type your text"
    bing_reply = await message.reply_text("...", quote=True)
    replied_message = message.reply_to_message

    if len(message.command) > 1:
        content = message.text.split(None, 1)[1]

    elif len(message.command) < 2:
        return await bing_reply.edit(bing_usage)

    output = await bing(content)
    return await bing_reply.edit(f"{output}")


@Client.on_message(filters.command(["meta", "metabot", "metabot"]))
async def metaBot(_, message: Message):
    """ Meta Bot"""

    meta_usage = f"**Usage:** meta bot. Reply to a text file, text message or just type the text after command. \n\n**Meta Bot.** \n\n**Example:** /meta type your text"
    meta_reply = await message.reply_text("...", quote=True)
    replied_message = message.reply_to_message

    if len(message.command) > 1:
        content = message.text.split(None, 1)[1]

    elif len(message.command) < 2:
        return await meta_reply.edit(meta_usage)

    output = await meta(content)
    return await meta_reply.edit(f"{output}", disable_web_page_preview=True)


@Client.on_message(filters.command(["mistral", "mistralbot", "mb", "chat"]))
async def mistralBot(_, message: Message):
    """ Mistral Bot"""

    mistral_usage = f"**Usage:** mistral bot. Reply to a text file, text message or just type the text after command. \n\n**Mistral Bot.** \n\n**Example:** /mistral type your text"
    mistral_reply = await message.reply_text("...", quote=True)
    replied_message = message.reply_to_message

    if len(message.command) > 1:
        content = message.text.split(None, 1)[1]

    elif len(message.command) < 2:
        return await mistral_reply.edit(mistral_usage)

    output = await mistral(content)
    return await mistral_reply.edit(f"{output}", disable_web_page_preview=True)


@Client.on_message(filters.command(["llm", "llamabot", "llamabot"]))
async def llamaBot(_, message: Message):
    """ Llama Bot"""

    llama_usage = f"**Usage:** llama bot. Reply to a text file, text message or just type the text after command. \n\n**Llama Bot.** \n\n**Example:** /llama type your text"
    llama_reply = await message.reply_text("...", quote=True)
    replied_message = message.reply_to_message

    if len(message.command) > 1:
        content = message.text.split(None, 1)[1]

    elif len(message.command) < 2:
        return await llama_reply.edit(llama_usage)

    output = await llama(content)
    await llama_reply.edit(f"{output}", disable_web_page_preview=True)


@Client.on_message(filters.command(["rewrite", "rb", "grammar"]))
async def rewriteBot(_, message: Message):
    """ Rewrite Bot"""

    rewrite_usage = f"**Usage:** rewrite bot. Reply to a text file, text message or just type the text after command. \n\n**Rewrite Bot.** \n\n**Example:** /rewrite type your text"
    rewrite_reply = await message.reply_text("...", quote=True)
    replied_message = message.reply_to_message

    if len(message.command) > 1:
        content = message.text.split(None, 1)[1]

    elif len(message.command) < 2:
        return await rewrite_reply.edit(rewrite_usage)

    output = await rewrite(content)
    await rewrite_reply.edit(f"{output}", disable_web_page_preview=True)


@Client.on_message(filters.command(["codellm", "cl", "codellmbot"]))
async def codeLLMBot(_, message: Message):
    """ Code LLM Bot"""

    codeLLM_usage = f"**Usage:** code llm bot. Reply to a text file, text message or just type the text after command. \n\n**Code LLM Bot.** \n\n**Example:** /codellm type your text"
    codeLLM_reply = await message.reply_text("...", quote=True)
    replied_message = message.reply_to_message

    if len(message.command) > 1:
        content = message.text.split(None, 1)[1]

    elif len(message.command) < 2:
        return await codeLLM_reply.edit(codeLLM_usage)

    output = await codeLLM(content)
    await codeLLM_reply.edit(f"```{output}```", disable_web_page_preview=True) and replied_message.delete()


@Client.on_message(filters.command(["starcoder", "sc"]))
async def starCoderBot(_, message: Message):
    """ Star Coder Bot"""

    starCoder_usage = f"**Usage:** star coder bot. Reply to a text file, text message or just type the text after command. \n\n**Star Coder Bot.** \n\n**Example:** /starcoder type your text"
    starCoder_reply = await message.reply_text("...", quote=True)
    replied_message = message.reply_to_message

    if len(message.command) > 1:
        content = message.text.split(None, 1)[1]

    elif len(message.command) < 2:
        return await starCoder_reply.edit(starCoder_usage)

    output = await starCoder(content)
    await starCoder_reply.edit(f"```{output}```", disable_web_page_preview=True) and replied_message.delete()
