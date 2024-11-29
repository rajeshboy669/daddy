#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
#from config import OWNER_ID , LINK , CHAT , CHANNEL
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from database import get_config  # Function to fetch dynamic variables

async def cb_handler(client, query: CallbackQuery):
    data = query.data
    
    # Fetch dynamic variables
    OWNER_ID = get_config("OWNER_ID")
    LINK = get_config("LINK")
    CHANNEL = get_config("CHANNEL")
    CHAT = get_config("CHAT")
    
    if data == "about":
        await query.message.edit_text(
            text=(
                f"<b>○ Creator : <a href='tg://user?id={OWNER_ID}'>This Person</a>\n"
                f"○ Language : <code>Python3</code>\n"
                f"○ Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio</a>\n"
                f"○ Source Code : <a href='{LINK}'>Click here</a>\n"
                f"○ Channel : @{CHANNEL}\n"
                f"○ Support Group : @{CHAT}</b>"
            ),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("🔒 Close", callback_data="close")]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except Exception:
            pass

    
