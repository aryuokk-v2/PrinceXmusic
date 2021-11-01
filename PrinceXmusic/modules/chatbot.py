import asyncio
import re

import aiohttp
import emoji
import requests
from coffeehouse.exception import CoffeeHouseError as CFError
from gpytranslate import Translator
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

url = "https://acobot-brainshop-ai-v1.p.rapidapi.com/get"

translator = Translator()
BOT_ID = 1939493494


def extract_emojis(s):
    return "".join(c for c in s if c in emoji.UNICODE_EMOJI)


en_chats = []


@Client.on_message(
    filters.text & filters.reply & ~filters.bot & ~filters.via_bot
    & ~filters.forwarded,
    group=2,
)
async def aryan(client, message):
    if message.reply_to_message.from_user.id != BOT_ID:
        message.continue_propagation()
    msg = message.text
    chat_id = message.chat.id
    if msg.startswith("/") or msg.startswith("@"):
        message.continue_propagation()
    if chat_id in en_chats:
        onik = msg
        querystring = {
            "bid": "159762",
            "key": "PG3sr9umeXqasKoD",
            "uid": "its_Prince",
            "msg": {test},
        }
        headers = {
            "x-rapidapi-key":"061e48f99amshddca9a1a170468bp15b84ejsn1e66f006ce01",
            "x-rapidapi-host": "acobot-brainshop-ai-v1.p.rapidapi.com",
        }
        response = requests.request("GET",
                                    url,
                                    headers=headers,
                                    params=querystring)
        result = response.text
        result = result.replace('{"cnt":"', "")
        result = result.replace('"}', "")
        result = result.replace("<a href=\\", "<a href =")
        result = result.replace("<\/a>", "</a>")
        saini = result
        try:
            await Client.send_chat_action(message.chat.id, "typing")
            await message.reply_text(saini)
        except CFError as e:
            print(e)
    else:
        u = msg.split()
        emj = extract_emojis(msg)
        msg = msg.replace(emj, "")
        if ([(k) for k in u if k.startswith("@")]
                and [(k) for k in u if k.startswith("#")]
                and [(k) for k in u if k.startswith("/")]
                and re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []):

            h = " ".join(filter(lambda x: x[0] != "@", u))
            km = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", h)
            tm = km.split()
            jm = " ".join(filter(lambda x: x[0] != "#", tm))
            hm = jm.split()
            rm = " ".join(filter(lambda x: x[0] != "/", hm))
        elif [(k) for k in u if k.startswith("@")]:

            rm = " ".join(filter(lambda x: x[0] != "@", u))
        elif [(k) for k in u if k.startswith("#")]:
            rm = " ".join(filter(lambda x: x[0] != "#", u))
        elif [(k) for k in u if k.startswith("/")]:
            rm = " ".join(filter(lambda x: x[0] != "/", u))
        elif re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []:
            rm = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", msg)
        else:
            rm = msg
            lan = await translator.detect(rm)
        onik = rm
        if not "en" in lan and not lan == "":
            onik = translator.translate(onik, targetlang="en")

        querystring = {
            "bid": "159762",
            "key": "PG3sr9umeXqasKoD",
            "uid": "its_Prince",
            "msg": {onik},
        }
        headers = {
            "x-rapidapi-key":"061e48f99amshddca9a1a170468bp15b84ejsn1e66f006ce01",
            "x-rapidapi-host": "acobot-brainshop-ai-v1.p.rapidapi.com",
        }
        response = requests.request("GET",
                                    url,
                                    headers=headers,
                                    params=querystring)
        result = response.text
        result = result.replace('{"cnt":"', "")
        result = result.replace('"}', "")
        result = result.replace("<a href=\\", "<a href =")
        result = result.replace("<\/a>", "</a>")
        saini = result
        if not "en" in lan and not lan == "":
            pro = translator.translate(saini, lang_tgt=lan[0])
        try:
            await Client.send_chat_action(message.chat.id, "typing")
            await message.reply_text(saini)
        except CFError as e:
            print(e)


@Client.on_message(filters.text & filters.private & ~filters.reply
                    & ~filters.bot)
async def papiya(client, message):
    msg = message.text
    if msg.startswith("/") or msg.startswith("@"):
        message.continue_propagation()
    u = msg.split()
    emj = extract_emojis(msg)
    msg = msg.replace(emj, "")
    if ([(k) for k in u if k.startswith("@")]
            and [(k) for k in u if k.startswith("#")]
            and [(k) for k in u if k.startswith("/")]
            and re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []):

        h = " ".join(filter(lambda x: x[0] != "@", u))
        km = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", h)
        tm = km.split()
        jm = " ".join(filter(lambda x: x[0] != "#", tm))
        hm = jm.split()
        rm = " ".join(filter(lambda x: x[0] != "/", hm))
    elif [(k) for k in u if k.startswith("@")]:

        rm = " ".join(filter(lambda x: x[0] != "@", u))
    elif [(k) for k in u if k.startswith("#")]:
        rm = " ".join(filter(lambda x: x[0] != "#", u))
    elif [(k) for k in u if k.startswith("/")]:
        rm = " ".join(filter(lambda x: x[0] != "/", u))
    elif re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []:
        rm = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", msg)
    else:
        rm = msg
        lan = await translator.detect(rm)
    onik = rm
    if not "en" in lan and not lan == "":
        onik = translator.translate(onik, targetlang="en")

    querystring = {
        "bid": "159762",
        "key": "PG3sr9umeXqasKoD",
        "uid": "its_Prince",
        "msg": {onik},
    }
    headers = {
        "x-rapidapi-key": "061e48f99amshddca9a1a170468bp15b84ejsn1e66f006ce01",
        "x-rapidapi-host": "acobot-brainshop-ai-v1.p.rapidapi.com",
    }
    response = requests.request("GET",
                                url,
                                headers=headers,
                                params=querystring)
    result = response.text
    result = result.replace('{"cnt":"', "")
    result = result.replace('"}', "")
    result = result.replace("<a href=\\", "<a href =")
    result = result.replace("<\/a>", "</a>")
    saini = result
    if not "en" in lan and not lan == "":
        saini = translator.translate(saini, targetlang=lan[0])
    try:
        await Client.send_chat_action(message.chat.id, "typing")
        await message.reply_text(saini)
    except CFError as e:
        print(e)


@Client.on_message(
    filters.regex("Nobita|nobita|NOBITA|prince||Prince")
    & ~filters.bot
    & ~filters.via_bot
    & ~filters.forwarded
    & ~filters.reply
    & ~filters.channel)
async def papiya(client, message):
    msg = message.text
    if msg.startswith("/") or msg.startswith("@"):
        message.continue_propagation()
    u = msg.split()
    emj = extract_emojis(msg)
    msg = msg.replace(emj, "")
    if ([(k) for k in u if k.startswith("@")]
            and [(k) for k in u if k.startswith("#")]
            and [(k) for k in u if k.startswith("/")]
            and re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []):

        h = " ".join(filter(lambda x: x[0] != "@", u))
        km = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", h)
        tm = km.split()
        jm = " ".join(filter(lambda x: x[0] != "#", tm))
        hm = jm.split()
        rm = " ".join(filter(lambda x: x[0] != "/", hm))
    elif [(k) for k in u if k.startswith("@")]:

        rm = " ".join(filter(lambda x: x[0] != "@", u))
    elif [(k) for k in u if k.startswith("#")]:
        rm = " ".join(filter(lambda x: x[0] != "#", u))
    elif [(k) for k in u if k.startswith("/")]:
        rm = " ".join(filter(lambda x: x[0] != "/", u))
    elif re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []:
        rm = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", msg)
    else:
        rm = msg
        lan = translator.detect(rm)
    onik = rm
    if not "en" in lan and not lan == "":
        onik = await translator.translate(onik, targetlang="en")
    querystring = {
        "bid": "159762",
        "key": "PG3sr9umeXqasKoD",
        "uid": "its_Prince",
        "msg": {onik},
    }
    headers = {
        "x-rapidapi-key": "061e48f99amshddca9a1a170468bp15b84ejsn1e66f006ce01",
        "x-rapidapi-host": "acobot-brainshop-ai-v1.p.rapidapi.com",
    }
    response = requests.request("GET",
                                url,
                                headers=headers,
                                params=querystring)
    result = response.text
    result = result.replace('{"cnt":"', "")
    result = result.replace('"}', "")
    result = result.replace("<a href=\\", "<a href =")
    result = result.replace("<\/a>", "</a>")
    pro = result
    if not "en" in lan and not lan == "":
        saini = translator.translate(saini, targetlang=lan[0])
    try:
        await Client.send_chat_action(message.chat.id, "typing")
        await message.reply_text(saini)
    except CFError as e:
        print(e)
