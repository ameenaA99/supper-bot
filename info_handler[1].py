from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def info_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "🤖 **معلومات البوت**

"
        "🔹 اسم البوت: Supper Bot
"
        "🔹 مطور البوت: يونس العمراوي
"
        "🔹 للتواصل: +212770905027
"
        "🔹 إنستغرام: https://www.instagram.com/youness.amraoui01/
"
    )

info_handler = CommandHandler("info", info_command)
