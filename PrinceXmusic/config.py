import os
from os import path
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", None)
BOT_TOKEN = getenv("BOT_TOKEN", None)
BOT_NAME = getenv("BOT_NAME", "PrinceXmusic")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "roBots_Hub")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/e447cc7fcb5fbfee866bf.png")
admins = {}
API_ID = int(getenv("API_ID", None))
API_HASH = getenv("API_HASH", None)
BOT_USERNAME = getenv("BOT_USERNAME", "PrinceX_MusicBot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "PrinceX Music Assistant")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "roBots_HubSupport")
PROJECT_NAME = getenv("PROJECT_NAME", "PrinceX Music")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/stark-Prince/PrinceXmusic")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "20"))
ARQ_API_KEY = getenv("ARQ_API_KEY", "YJOLHJ-TAHPTA-KDQXTV-DYCNHF-ARQ")
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1994755645").split()))
