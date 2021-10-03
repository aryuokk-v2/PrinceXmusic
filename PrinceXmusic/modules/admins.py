from asyncio import QueueEmpty
from pyrogram import Client 
from pyrogram import filters
from pyrogram.types import Message

from PrinceXmusic.config import que
from PrinceXmusic.function.admins import set
from PrinceXmusic.helpers.channelmusic import get_chat_id
from PrinceXmusic.helpers.decorators import authorized_users_only
from PrinceXmusic.helpers.decorators import errors
from PrinceXmusic.helpers.filters import command
from PrinceXmusic.helpers.filters import other_filters
from PrinceXmusic.services.callsmusic import callsmusic
from PrinceXmusic.services.queues import queues


@Client.on_message(filters.command("adminreset"))
async def update_admin(client, message: Message):
    chat_id = get_chat_id(message.chat)
    set(
        chat_id,
        [
            member.user
            for member in await message.chat.get_members(filter="administrators")
        ],
    )
    await message.reply_text("❇️ Admin cache refreshed!")


@Client.on_message(command("pause") & other_filters)
@errors
@authorized_users_only
async def pause(_, message: Message):
    chat_id = get_chat_id(message.chat)
    (
      await message.reply_text("▶️ Paused!")
    ) if (
        callsmusic.pause(chat_id)
    ) else (
        await message.reply_text("❗ Nothing is playing!")
    )
        


@Client.on_message(command("resume") & other_filters)
@errors
@authorized_users_only
async def resume(_, message: Message):
    chat_id = get_chat_id(message.chat)
    (
        await message.reply_text("⏸ Resumed!")
    ) if (
        callsmusic.resume(chat_id)
    ) else (
        await message.reply_text("❗ Nothing is paused!")
    )
        


@Client.on_message(command("end") & other_filters)
@errors
@authorized_users_only
async def stop(_, message: Message):
    chat_id = get_chat_id(message.chat)
    if chat_id not in callsmusic.active_chats:
        await message.reply_text("❗ Nothing is streaming!")
    else:
        try:
            queues.clear(chat_id)
        except QueueEmpty:
            pass

        await callsmusic.stop(chat_id)
        await message.reply_text("❌ Stopped streaming!")


@Client.on_message(command("skip") & other_filters)
@errors
@authorized_users_only
async def skip(_, message: Message):
    global que
    chat_id = get_chat_id(message.chat)
    if chat_id not in callsmusic.active_chats:
        await message.reply_text("❗ Nothing is playing to skip!")
    else:
        queues.task_done(chat_id)
        if queues.is_empty(chat_id):
            await callsmusic.stop(chat_id)
        else:
            await callsmusic.set_stream(chat_id, queues.get(chat_id)["file"])

    qeue = que.get(chat_id)
    if qeue:
        skip = qeue.pop(0)
    if not qeue:
        return
    await message.reply_text(f"- Skipped **{skip[0]}**\n- Now Playing **{qeue[0][0]}**")
    

@Client.on_message(command('mute') & other_filters)
@errors
@authorized_users_only
async def mute(_, message: Message):
    chat_id = get_chat_id(message.chat)
    result = await callsmusic.mute(chat_id)
    (
        await message.reply_text("✅ Muted")
    ) if (
        result == 0
    ) else (
        await message.reply_text("❌ Already muted")
    ) if (
        result == 1
    ) else (
        await message.reply_text("❌ Not in call")
    )

        
@Client.on_message(command('unmute') & other_filters)
@errors
@authorized_users_only
async def unmute(_, message: Message):
    chat_id = get_chat_id(message.chat)
    result = await callsmusic.unmute(chat_id)
    (
        await message.reply_text("✅ Unmuted")
    ) if (
        result == 0
    ) else (
        await message.reply_text("❌ Not muted")
    ) if (
        result == 1
    ) else (
        await message.reply_text("❌ Not in call")
    )


@Client.on_message(filters.command("admincache"))
@errors
async def admincache(client, message: Message):
    set(
        message.chat.id,
        [
            member.user
            for member in await message.chat.get_members(filter="administrators")
        ],
    )
    await message.reply_text("❇️ Admin cache refreshed!")
