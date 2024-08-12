import asyncio
import importlib

from pyrogram import idle

import config
from SACHINxMUSIC import LOGGER, app, userbot
from SACHINxMUSIC.core.call import RAUSHAN
from SACHINxMUSIC.misc import sudo
from SACHINxMUSIC.plugins import ALL_MODULES
from SACHINxMUSIC.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error(
            "sᴛʀɪɴɢ sᴇssɪᴏɴ ɴᴏᴛ ғɪʟʟᴇᴅ, ᴘʟᴇᴀsᴇ ғɪʟʟ ᴀ ᴘʏʀᴏɢʀᴀᴍ ᴠ2 sᴇssɪᴏɴ......💙"
        )

    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("SACHINxMUSIC.plugins" + all_module)
    LOGGER("SACHINxMUSIC.plugins").info("ᴀʟʟ ғᴇᴀᴛᴜʀᴇs ʟᴏᴀᴅᴇᴅ ᴅᴏɴᴇ......💛")
    await userbot.start()
    await RAUSHAN.start()
    await RAUSHAN.decorators()
    LOGGER("SACHINxMUSIC").info("ᴀʟʟ ᴅᴏɴᴇ ʏᴏᴜʀ ʙᴏᴛ ɪᴅ ʀᴜɴ......🤍")
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("SACHINxMUSIC").info("ᴀʟʟ ᴅᴏɴᴇ ʏᴏᴜʀ ʙᴏᴛ ɪᴅ ʀᴜɴ......🤍")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
