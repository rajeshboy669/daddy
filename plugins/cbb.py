from pyrogram import __version__, Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.enums import ParseMode
from database.database import full_userbase
from bot import Bot
from config import *
from plugins.cmd import *

# Callback query handler
@Bot.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data

    try:
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
                    [[InlineKeyboardButton("🔒 Close", callback_data="close")]]
                )
            )
        elif data == "close":
            await query.message.delete()
            try:
                await query.message.reply_to_message.delete()
            except Exception as e:
                await query.message.reply(f"❌ Error deleting message: {str(e)}")
    except Exception as e:
        await query.answer(f"❌ Error: {str(e)}", show_alert=True)
