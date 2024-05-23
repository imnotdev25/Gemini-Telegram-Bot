import json
from os import getenv

from dotenv import load_dotenv

load_dotenv("config.env")

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")

OWNER_USERID = json.loads(getenv("OWNER_USERID"))
SUDO_USERID = OWNER_USERID
try:SUDO_USERID += json.loads(getenv("SUDO_USERID"))
except:pass
SUDO_USERID = list(set(SUDO_USERID))
MONGO_URI = getenv("MONGO_URI")
ALLOWED_USERS = list(set(json.loads(getenv("ALLOWED_USERS"))))
ALLOWED_CHATS = list(set(json.loads(getenv("ALLOWED_CHATS"))))
PALM_API_KEY = getenv("PALM_API_KEY")
DEEPAI_API_KEY = getenv("DEEPAI_API_KEY")
CF_API_KEY = getenv("CF_API_KEY")
CHATLULU_COOKIE = getenv("CHATLULU_COOKIE")
CHATLULU_AUTH = getenv("CHATLULU_AUTH")
NVIDIA_API_KEY = getenv("NVIDIA_API_KEY")
MS_TOKEN = getenv("MS_TOKEN")
BING_U = getenv("BING_U")
OPENAI_API_KEY = getenv("OPENAI_API_KEY")