#(©)CodeXBotz

import os
import logging
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler
import pymongo

load_dotenv()

# MongoDB Connection
DB_URI = os.getenv("DATABASE_URL", "mongodb+srv://ultroidxTeam:ultroidxTeam@cluster0.gabxs6m.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.getenv("DATABASE_NAME", "config_database")
client = pymongo.MongoClient(DB_URI)
db = client[DB_NAME]
config_collection = db["bot_config"]

DEFAULT_CONFIG = {
    "TG_BOT_TOKEN": "default_bot_token",
    "APP_ID": 12345,
    "API_HASH": "default_api_hash",
    "DELETE_AFTER": 60,
    "OWNER_ID": 123456789,  # Replace with your ID
}

def get_config(key):
    config = config_collection.find_one({"key": key})
    return config["value"] if config else DEFAULT_CONFIG.get(key)

# Fetching variables dynamically
TG_BOT_TOKEN = get_config("TG_BOT_TOKEN")
APP_ID = int(get_config("APP_ID"))
API_HASH = get_config("API_HASH")
DELETE_AFTER = int(get_config("DELETE_AFTER"))
OWNER_ID = int(get_config("OWNER_ID"))

LINK = get_config("LINK")
CHAT = get_config("CHAT")
CHANNEL = get_config("CHANNEL")

#TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

CHANNEL_ID = int(get_config("CHANNEL_ID"))
PAYMENT_QR = get_config("PAYMENT_QR")
PAYMENT_TEXT = get_config("PAYMENT_TEXT")
                   
PORT = os.environ.get("PORT", "8080")
 
DB_URI = get_config("DATABASE_URL") #, "mongodb+srv://ultroidxTeam:ultroidxTeam@cluster0.gabxs6m.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = get_config("DATABASE_NAME")#, "nothingbot")

FORCE_SUB_CHANNEL = int(get_config("FORCE_SUB_CHANNEL"))

TG_BOT_WORKERS = int(get_config()("TG_BOT_WORKERS", "4"))

START_PIC = get_config("START_PIC")
START_MSG = get_config("START_MESSAGE") #, "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link.")
try:
    ADMINS=[]
    for x in (get_config("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

FORCE_MSG = get_config("FORCE_SUB_MESSAGE")  #, "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

CUSTOM_CAPTION = get_config("CUSTOM_CAPTION") #, None)

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

AUTO_DELETE_TIME = int(get_config("AUTO_DELETE_TIME")) #, "600"))
AUTO_DELETE_MSG = get_config("AUTO_DELETE_MSG") #, "This file will be automatically deleted in {time} seconds. Please ensure you have saved any necessary content before this time.")
AUTO_DEL_SUCCESS_MSG = get_config("AUTO_DEL_SUCCESS_MSG") #, "Your file has been successfully deleted. Thank you for using our service. ✅")

DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
