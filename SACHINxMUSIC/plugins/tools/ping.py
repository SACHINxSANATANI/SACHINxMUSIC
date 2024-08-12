from datetime import datetime
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup
from SACHINxMUSIC import app
from SACHINxMUSIC.core.call import SACHINxMUSIC
from SACHINxMUSIC.utils import bot_sys_stats
from SACHINxMUSIC.utils.inline.extras import botplaylist_markup
from SACHINxMUSIC.utils.decorators.language import language
from config import BANNED_USERS, PING_IMG_URL
import aiohttp
import asyncio

 
@app.on_message(filters.command(["ping", "alive"]) & ~BANNED_USERS & filters.group)
@language
async def ping_com(client, message: Message, _):
    response = await message.reply_photo(
        photo=PING_IMG_URL,
        caption=_["ping_1"].format(app.mention),
    )
    start = datetime.now()
    pytgping = await RAUSHAN.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit(
        _["ping_2"].format(
            resp,
            app.mention,
            UP,
            RAM,
            CPU,
            DISK,
            pytgping,
        ),
        reply_markup=InlineKeyboardMarkup(botplaylist_markup(_)),
        )
