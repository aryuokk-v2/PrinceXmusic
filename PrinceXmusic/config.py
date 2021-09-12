import os
from os import path
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "BQDFoyIjZBbQJnYi_urPH3dSmYa0Pt9c-vYPgBYqFyiPeTvaqjCEkuEnFt6j-_oAYHaIs5o8w7NBx8gjiaB7y_RZe9st7sgYCv9Fcx0utRgxnMD3-A8uONaAZBW1_3T62FutX-D4Ya1R8JlhAouQZfujWpe6kBHuGFYJ9nlUQWcYdH3NI1PEUwN3zIPwnUd0IaFfy02tnXkz6g6BKHj_da7zo4ovBC4iBaPuR9dJDw0_5by9bEqYP3Z_0pCu1smqU5yRswSp2qH8QmADgexCYv7eoDWbUZVsmmItM5V32aB-Vj_4DP-s_nC6Bar1EK_PClY7W_UyfxRjiezFw2mQvMcpI6aAA")
BOT_TOKEN = getenv("BOT_TOKEN", "1995648542:AAEFMUfZbUZiXzoXwmVTF1b7Qg_KHl_vtoQ")
BOT_NAME = getenv("BOT_NAME", "PrinceXmusic")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "roBots_Hub")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/e447cc7fcb5fbfee866bf.png")
admins = {}
API_ID = int(getenv("API_ID", "7371425"))
API_HASH = getenv("API_HASH", "b569b2b80efd25a4f112a4d14bd2ec2e")
BOT_USERNAME = getenv("BOT_USERNAME", "PrinceX_MusicBot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "PrinceX Music Assistant")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "roBots_HubSupport")
PROJECT_NAME = getenv("PROJECT_NAME", "PrinceX Music")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/stark-Prince/PrinceXmusic")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "20"))
ARQ_API_KEY = getenv("ARQ_API_KEY", "VHWWWU-MDKTOL-KYXSYQ-VAVSPS-ARQ")
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1994755645").split()))
