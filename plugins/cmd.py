
"""
from bot import Bot
from pyrogram import filters
from config import OWNER_ID, PAYMENT_QR, PAYMENT_TEXT, config_collection, DEFAULT_CONFIG
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ParseMode

# HELP Command
@Bot.on_message(filters.command("help") & filters.private)
async def help_command(bot: Bot, message: Message):
    try:
        help_text = 
📖 <b>Available Commands:</b>
- /start: Start the bot
- /help: Show help message
- /upi: Show UPI payment details
- /view_config: View bot configuration (Owner only)
- /edit_config <key> <value>: Edit configuration (Owner only)
- /reset_config <key>: Reset configuration to default (Owner only)

        await message.reply(help_text, parse_mode=ParseMode.HTML)
    except Exception as e:
        await message.reply(f"❌ Error displaying help: {str(e)}")


# UPI Command
@Bot.on_message(filters.command("upi") & filters.private)
async def upi_info(bot: Bot, message: Message):
    try:
        await bot.send_photo(
            chat_id=message.chat.id,
            photo=PAYMENT_QR,
            caption=PAYMENT_TEXT,
            parse_mode=ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("Contact Owner", url=f"https://t.me/{OWNER_ID}")]]
            )
        )
    except Exception as e:
        await message.reply(f"❌ Error displaying UPI details: {str(e)}")


# View Config (Owner only)
@Bot.on_message(filters.command("view_config") & filters.private & filters.user(OWNER_ID))
async def view_config(bot: Bot, message: Message):
    try:
        configs = config_collection.find()
        if configs.count() == 0:
            await message.reply("⚙️ No custom configurations found.")
        else:
            config_text = "<b>Current Configuration:</b>\n\n"
            for config in configs:
                config_text += f"<b>{config['key']}:</b> {config['value']}\n"
            await message.reply(config_text, parse_mode=ParseMode.HTML)
    except Exception as e:
        await message.reply(f"❌ Error fetching configurations: {str(e)}")


# Edit Config (Owner only)
@Bot.on_message(filters.command("edit_config") & filters.private & filters.user(OWNER_ID))
async def edit_config(bot: Bot, message: Message):
    try:
        _, key, value = message.text.split(maxsplit=2)
        if key not in DEFAULT_CONFIG:
            return await message.reply(f"❌ Invalid configuration key: {key}")
        config_collection.update_one({"key": key}, {"$set": {"value": value}}, upsert=True)
        await message.reply(f"✅ Configuration updated: <b>{key}</b> = {value}", parse_mode=ParseMode.HTML)
    except ValueError:
        await message.reply("Usage: /edit_config <key> <value>")
    except Exception as e:
        await message.reply(f"❌ Error updating configuration: {str(e)}")


# Reset Config (Owner only)
@Bot.on_message(filters.command("reset_config") & filters.private & filters.user(OWNER_ID))
async def reset_config(bot: Bot, message: Message):
    try:
        _, key = message.text.split(maxsplit=1)
        if key in DEFAULT_CONFIG:
            config_collection.update_one({"key": key}, {"$set": {"value": DEFAULT_CONFIG[key]}}, upsert=True)
            await message.reply(f"✅ Configuration reset: <b>{key}</b> = {DEFAULT_CONFIG[key]}", parse_mode=ParseMode.HTML)
        else:
            await message.reply(f"❌ Invalid configuration key: <b>{key}</b>", parse_mode=ParseMode.HTML)
    except ValueError:
        await message.reply("Usage: /reset_config <key>")
    except Exception as e:
        await message.reply(f"❌ Error resetting configuration: {str(e)}")
"""
