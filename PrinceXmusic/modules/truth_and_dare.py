import requests
from pyrogram import Client

from PrinceXmusic.config import BOT_USERNAME
from helpers.filters import command

@Client.on_message(command(["truth", f"truth@{BOT_USERNAME}"]))
async def truth(_, message):
    try:
        resp = requests.get("https://api-tede.herokuapp.com/api/truth-en").json()
        results = f"{resp['message']}"
        return await message.reply_text(results)
    except Exception as ex:
        print(ex)
        await message.reply_text("Can't fetch truth from database of @its_Prince")


@Client.on_message(command(["dare", f"dare@{BOT_USERNAME}"]))
async def dare(_, message):
    try:
        resp = requests.get("https://api-tede.herokuapp.com/api/dare-en").json()
        results = f"{resp['message']}"
        return await message.reply_text(results)
    except Exception as ex:
        print(ex)
        await message.reply_text("Can't fetch dare from database of @its_Prince")
