import requests
from pyrogram import Client as Bot

from PrinceXmusic.config import API_HASH
from PrinceXmusic.config import API_ID
from PrinceXmusic.config import BG_IMAGE
from PrinceXmusic.config import BOT_TOKEN
from PrinceXmusic.services.callsmusic import run

response = requests.get(BG_IMAGE)
file = open("./etc/foreground.png", "wb")
file.write(response.content)
file.close()

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="PrinceXmusic.modules"),
)

bot.start()
run()
