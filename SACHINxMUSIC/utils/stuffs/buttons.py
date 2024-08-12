from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

class BUTTONS(object):
    MBUTTON = [[InlineKeyboardButton("ᴄʜᴀᴛɢᴘᴛ", callback_data="mplus HELP_ChatGPT"),InlineKeyboardButton("ɢʀᴘs", callback_data="mplus HELP_Group"),InlineKeyboardButton("sᴛᴄᴋʀs", callback_data="mplus HELP_Sticker")],
    [InlineKeyboardButton("ᴛᴀɢᴀʟʟ", callback_data="mplus HELP_TagAll"),
    InlineKeyboardButton("ɪɴꜰᴏ", callback_data="mplus HELP_Info"),InlineKeyboardButton("ᴇxᴛʀᴀ", callback_data="mplus HELP_Extra")],
    [InlineKeyboardButton("ɪᴍᴀɢᴇ", callback_data="mplus HELP_Image"),
    InlineKeyboardButton("ᴀᴄᴛɪᴏɴ", callback_data="mplus HELP_Action"),InlineKeyboardButton("sʀᴄʜ", callback_data="mplus HELP_Search")],    
    [InlineKeyboardButton("ғᴏɴᴛ", callback_data="mplus HELP_Font"),
    InlineKeyboardButton("ɢᴀᴍᴇ", callback_data="mplus HELP_Game"),InlineKeyboardButton("ɢʀᴘʜ", callback_data="mplus HELP_TG")],
    [InlineKeyboardButton("ɪᴍᴘsᴛʀ", callback_data="mplus HELP_Imposter"),
    InlineKeyboardButton("ᴛ-ᴅ", callback_data="mplus HELP_TD"),InlineKeyboardButton("ʜsᴛɢ", callback_data="mplus HELP_HT")], 
    [InlineKeyboardButton("ᴛᴛs", callback_data="mplus HELP_TTS"),
    InlineKeyboardButton("ғᴜɴ", callback_data="mplus HELP_Fun"),InlineKeyboardButton("ǫᴜᴏᴛʟʏ", callback_data="mplus HELP_Q")],          
    [InlineKeyboardButton("⩤", callback_data=f"settings_back_helper"), 
    InlineKeyboardButton("⩥", callback_data=f"managebot123 settings_back_helper"),
    ]]
