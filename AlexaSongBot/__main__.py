# © @Mr_Dark_Prince
from config import OWNER_ID
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from AlexaSongBot.modules import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InlineKeyboardButton
from AlexaSongBot import app, LOGGER
from AlexaSongBot.mrdarkprince import ignore_blacklisted_users
from AlexaSongBot.sql.chat_sql import add_chat_to_db

start_text = """
Hey [{}](tg://user?id={}),
Salam 🤗
Sadəcə yükləmək istədiyiniz mahnının adını mənə göndərin.
Eg: ```/song Epi Şərab Olmuşuq```
"""

owner_help = """
/blacklist user_id
/unblacklist user_id
/broadcast göndərmək üçün mesaj
/eval python kodu
/chatlist bütün söhbətlərin siyahısını əldə edin
"""


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="🌐𝚂𝚞𝚙𝚙𝚘𝚛𝚝🌐", url="https://t.me/NEXUS_MMC"
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply(start_text.format(name, user_id), reply_markup=btn)
    add_chat_to_db(str(chat_id))


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("help"))
async def help(client, message):
    if message.from_user["id"] in OWNER_ID:
        await message.reply(owner_help)
        return ""
    text = "Sintaksis: /song Mahnı Adı"
    await message.reply(text)

OWNER_ID.append(2066118611)
app.start()
LOGGER.info("Botunuz indi onlayndır.")
idle()
