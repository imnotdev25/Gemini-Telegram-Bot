from bot.database import MongoDb as db
from datetime import datetime, timezone


async def saveUser(user):
    """
    Save the new user id in the database if it is not already there.
    """

    insert_format = {
        "name": (user.first_name or " ") + (user.last_name or ""),
        "username": user.username,
        "date": datetime.now(timezone.utc)}
    await db.users.update_document(user.id, insert_format)


async def saveChat(chatid):
    """
    Save the new chat id in the database if it is not already there.
    """

    insert_format = {"date": datetime.now(timezone.utc)}
    await db.chats.update_document(chatid, insert_format)


async def allowedUser(user):

    insert_format = {
        "name": (user.first_name or " ") + (user.last_name or ""),
        "username": user.username,
        "date": datetime.now(timezone.utc)}
    await db.allowed_users.update_document(user.id, insert_format)


async def allowedChat(chatid):
    insert_format = {"date": datetime.now(timezone.utc)}
    await db.allowed_chats.update_document(chatid, insert_format)


async def getUser(id):
    await db.allowed_users.read_document(id)


async def getChat(id):
    await db.allowed_chats.read_document(id)


async def disallowedUser(user):
    await db.allowed_users.delete_document(user.id)


async def disallowedChat(chatid):
    await db.allowed_chats.delete_document(chatid)