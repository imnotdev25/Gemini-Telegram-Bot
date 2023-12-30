"""
Creating custom filters 
https://docs.pyrogram.org/topics/create-filters
"""

from pyrogram import filters
from pyrogram.types import Message
from bot.config import SUDO_USERID, OWNER_USERID, ALLOWED_USERS, ALLOWED_CHATS
from bot.database import database


def dev_users(_, __, message: Message) -> bool:
    return message.from_user.id in OWNER_USERID if message.from_user else False


def sudo_users(_, __, message: Message) -> bool:
    return message.from_user.id in SUDO_USERID if message.from_user else False


def allowed_users(_, __, message: Message) -> bool:
    return message.from_user.id in ALLOWED_USERS and database.getUser(message.from_user.id) if message.from_user else False


def allowed_chats(_, __, message: Message) -> bool:
    return message.chat.id in ALLOWED_CHATS and database.getChat(message.chat.id) if message.chat else False


dev_cmd = filters.create(dev_users)
sudo_cmd = filters.create(sudo_users)
allowed_chat = filters.create(allowed_chats)
allowed_users = filters.create(allowed_users)
