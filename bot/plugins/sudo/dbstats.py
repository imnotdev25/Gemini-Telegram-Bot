from pyrogram.types import Message 
from pyrogram import Client, filters

from bot.database import MongoDb
from bot.helpers.filters import sudo_cmd
# from bot.helpers.decorators import ratelimiter


@Client.on_message(filters.command("dbstats") & sudo_cmd)
async def dbstats(_, message: Message):
    """
    Returns database stats of MongoDB, which includes Total number
    of bot user and total number of bot chats.
    """ 
    
    TotalUsers = await MongoDb.users.total_documents()
    TotalChats = await MongoDb.chats.total_documents()
    
    stats_string = f"**Bot Database Statics.\n\n**Total Number of users = {TotalUsers}\nTotal number of chats  = {TotalChats}"
    return await message.reply_text(stats_string)
