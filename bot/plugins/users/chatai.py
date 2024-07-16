from pyrogram import Client, filters
from pyrogram.types import Message

from bot.helpers.ai import meta, mistral, llama, rewrite, chatgpt4, chatgpt4o, codellama_ngc, codestral_ngc, \
    granite_ngc, snowflake_ngc, nemotron_ngc, mixtral_ngc


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


@Client.on_message(filters.command(["gpt4", "chatgpt4"]))
async def chatGPT4Bot(_, message: Message):
    """ Chat GPT4 Bot"""

    chatGPT4_usage = f"**Usage:** chat gpt4 bot. Reply to a text file, text message or just type the text after command. \n\n**Chat GPT4 Bot.** \n\n**Example:** /chatgpt4 type your text"
    chatGPT4_reply = await message.reply_text("...", quote=True)
    replied_message = message.reply_to_message

    if len(message.command) > 1:
        content = message.text.split(None, 1)[1]

    elif len(message.command) < 2:
        return await chatGPT4_reply.edit(chatGPT4_usage)

    output = await chatgpt4(content)
    await chatGPT4_reply.edit(f"{output}", disable_web_page_preview=True)


@Client.on_message(filters.command(["gpt4o", "chatgpt4o"]))
async def chatGPT4oBot(_, message: Message):
    """ Chat GPT4o Bot"""

    chatGPT4o_usage = f"**Usage:** chat gpt4o bot. Reply to a text file, text message or just type the text after command. \n\n**Chat GPT4o Bot.** \n\n**Example:** /chatgpt4o type your text"
    chatGPT4o_reply = await message.reply_text("...", quote=True)
    replied_message = message.reply_to_message

    if len(message.command) > 1:
        content = message.text.split(None, 1)[1]

    elif len(message.command) < 2:
        return await chatGPT4o_reply.edit(chatGPT4o_usage)

    output = await chatgpt4o(content)
    await chatGPT4o_reply.edit(f"{output}", disable_web_page_preview=True)


@Client.on_message(filters.command(["codellama", "codellamangc", "cl", "clngc"]))
async def codellamaNGCBot(_, message: Message):
    """ Code Llama NGC Bot"""

    codellamaNGC_usage = f"**Usage:** code llama ngc bot. Reply to a text file, text message or just type the text after command. \n\n**Code Llama NGC Bot.** \n\n**Example:** /codellama type your text"
    codellamaNGC_reply = await message.reply_text("...", quote=True)
    replied_message = message.reply_to_message

    if len(message.command) > 1:
        content = message.text.split(None, 1)[1]

    elif len(message.command) < 2:
        return await codellamaNGC_reply.edit(codellamaNGC_usage)

    output = await codellama_ngc(content)
    await codellamaNGC_reply.edit(f"{output}", disable_web_page_preview=True)


@Client.on_message(filters.command(["codestral", "codestralngc", "cs", "csngc"]))
async def codestralNGCBot(_, message: Message):
    """ Codestral NGC Bot"""

    codestralNGC_usage = f"**Usage:** codestral ngc bot. Reply to a text file, text message or just type the text after command. \n\n**Codestral NGC Bot.** \n\n**Example:** /codestral type your text"
    codestralNGC_reply = await message.reply_text("...", quote=True)
    replied_message = message.reply_to_message

    if len(message.command) > 1:
        content = message.text.split(None, 1)[1]

    elif len(message.command) < 2:
        return await codestralNGC_reply.edit(codestralNGC_usage)

    output = await codestral_ngc(content)
    await codestralNGC_reply.edit(f"{output}", disable_web_page_preview=True)


@Client.on_message(filters.command(["granite", "granitengc", "gn", "gngc"]))
async def graniteNGCBot(_, message: Message):
    """ Granite NGC Bot"""

    graniteNGC_usage = f"**Usage:** granite ngc bot. Reply to a text file, text message or just type the text after command. \n\n**Granite NGC Bot.** \n\n**Example:** /granite type your text"
    graniteNGC_reply = await message.reply_text("...", quote=True)
    replied_message = message.reply_to_message

    if len(message.command) > 1:
        content = message.text.split(None, 1)[1]

    elif len(message.command) < 2:
        return await graniteNGC_reply.edit(graniteNGC_usage)

    output = await granite_ngc(content)
    await graniteNGC_reply.edit(f"{output}", disable_web_page_preview=True)


@Client.on_message(filters.command(["snowflake", "snowflakengc", "sf", "sfngc"]))
async def snowflakeNGCBot(_, message: Message):
    """ Snowflake NGC Bot"""

    snowflakeNGC_usage = f"**Usage:** snowflake ngc bot. Reply to a text file, text message or just type the text after command. \n\n**Snowflake NGC Bot.** \n\n**Example:** /snowflake type your text"
    snowflakeNGC_reply = await message.reply_text("...", quote=True)
    replied_message = message.reply_to_message

    if len(message.command) > 1:
        content = message.text.split(None, 1)[1]

    elif len(message.command) < 2:
        return await snowflakeNGC_reply.edit(snowflakeNGC_usage)

    output = await snowflake_ngc(content)
    await snowflakeNGC_reply.edit(f"{output}", disable_web_page_preview=True)


@Client.on_message(filters.command(["nemotron", "nemotronngc", "nm", "nmngc"]))
async def nemotronNGCBot(_, message: Message):
    """ Nemotron NGC Bot"""

    nemotronNGC_usage = f"**Usage:** nemotron ngc bot. Reply to a text file, text message or just type the text after command. \n\n**Nemotron NGC Bot.** \n\n**Example:** /nemotron type your text"
    nemotronNGC_reply = await message.reply_text("...", quote=True)
    replied_message = message.reply_to_message

    if len(message.command) > 1:
        content = message.text.split(None, 1)[1]

    elif len(message.command) < 2:
        return await nemotronNGC_reply.edit(nemotronNGC_usage)

    output = await nemotron_ngc(content)
    await nemotronNGC_reply.edit(f"{output}", disable_web_page_preview=True)


@Client.on_message(filters.command(["mixtral", "mixtralngc", "mx", "mxngc"]))
async def mixtralNGCBot(_, message: Message):
    """ Mixtral NGC Bot"""

    mixtralNGC_usage = f"**Usage:** mixtral ngc bot. Reply to a text file, text message or just type the text after command. \n\n**Mixtral NGC Bot.** \n\n**Example:** /mixtral type your text"
    mixtralNGC_reply = await message.reply_text("...", quote=True)
    replied_message = message.reply_to_message

    if len(message.command) > 1:
        content = message.text.split(None, 1)[1]

    elif len(message.command) < 2:
        return await mixtralNGC_reply.edit(mixtralNGC_usage)

    output = await mixtral_ngc(content)
    await mixtralNGC_reply.edit(f"{output}", disable_web_page_preview=True)
