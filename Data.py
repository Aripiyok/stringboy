from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
**__Hey__** {}
**__Selamat Datang di__** {}

**__Jika Anda tidak mempercayai bot ini !!__**
**__1) Berhenti membaca pesan ini__**
**__2) Hapus obrolan ini__**

**__Masih membaca?__**
**__Anda dapat menggunakan saya untuk menghasilkan sesi pyrogram dan string telethon.Gunakan tombol di bawah ini untuk mempelajari lebih lanjut!__**

**__By__** @fl0werboy
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("⚡ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ ", callback_data="generate")],
        [InlineKeyboardButton(text="🏠 ʀᴇᴛᴜʀɴ ʜᴏᴍᴇ ", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("⚡ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ ", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("⚡ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ ", callback_data="generate")],
        [
            InlineKeyboardButton("ʜᴏᴡ ᴛᴏ ᴜsᴇ ❔", callback_data="help"),
            InlineKeyboardButton("✨ ᴀʙᴏᴜᴛ ✨", callback_data="about")
        ],
        [InlineKeyboardButton("✅ ᴍᴏʀᴇ ᴀᴍᴀᴢɪɴɢ ʙᴏᴛs", url="https://t.me/SharingUserbot")],
    ]

    # Help Message
    HELP = """
✨ **Available Commands** ✨

/about - About The Bot
/help - This Message
/start - Start the Bot
/generate - Start Generating Session
/cancel - Cancel the process
/restart - Cancel the process
"""

    # About Message
    ABOUT = """
**About This Bot** 

**__A telegram bot to generate pyrogram and telethon string session by__** @fl0werboy
    """
