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
        [InlineKeyboardButton("⚡ Start Generating Session ", callback_data="generate")],
        [InlineKeyboardButton(text="🏠 Return Home ", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("⚡ Start Generating Session ", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("⚡ Start Generating Session ⚡ ", callback_data="generate")],
        [InlineKeyboardButton("✨ Bot Status and More Bots ✨", url="https://t.me/fl0werboy")],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("✨ About ✨", callback_data="about")
        ],
        [InlineKeyboardButton("✅ More Amazing bots", url="https://t.me/fl0werboy")],
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

A telegram bot to generate pyrogram and telethon string session by @fl0werboy
    """
