from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "📚 **دليل المساعدة**

"
        "🟢 /start - بدء البوت
"
        "🟢 /help - عرض قائمة الأوامر
"
        "🟢 /info - عرض معلومات البوت
"
    )

help_handler = CommandHandler("help", help_command)
