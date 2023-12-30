from pyrogram import Client, filters
from pyrogram.types import Message

from bot.database import database, MongoDb
# from bot.helpers.decorators import ratelimiter
from bot.helpers.filters import dev_cmd
from bot.logging import LOGGER


@Client.on_message(filters.command(["auth"]) & dev_cmd)
async def auth_user(client, message: Message):
    """ Authorize chats and users in same"""
    msg = message.text.split()
    if len(msg) > 1:
        id_ = int(msg[1].strip())
    elif reply_to := message.reply_to_message:
        id_ = reply_to.from_user.id if reply_to.from_user else reply_to.sender_chat.id
    else:
        id_ = message.chat.id
    if id_ in database.getUser(id_):
        msg = "User Already Authorized!"
    elif id_ in database.getChat(id_):
        msg = "Chat Already Authorized!"
    else:
        await database.allowedUser(id_) and database.allowedChat(id_)
        msg = "Authorized Successfully!"
    await message.reply_text(msg, quote=True)


@Client.on_message(filters.command(["unauth"]) & dev_cmd)
async def unauth_user(client, message: Message):
    """ Unauthorize chats and users in same"""
    msg = message.text.split()
    if len(msg) > 1:
        id_ = int(msg[1].strip())
    elif reply_to := message.reply_to_message:
        id_ = reply_to.from_user.id if reply_to.from_user else reply_to.sender_chat.id
    else:
        id_ = message.chat.id
    if id_ not in database.getUser(id_) and id_ not in database.getChat(id_):
        msg = "User or Chat is not Authorized!"
    else:
        await database.disallowedUser(id_) and database.disallowedChat(id_)
        msg = "Unauthorized Successfully!"
    await message.reply_text(msg, quote=True)

