from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("💡 معلومات", callback_data='info')],
        [InlineKeyboardButton("⚙️ الإعدادات", callback_data='settings')],
        [InlineKeyboardButton("📞 تواصل معنا", callback_data='contact')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "🎉 أهلا بك في **Supper Bot**!

🚀 اختر خيارًا من الأزرار أدناه:", 
        reply_markup=reply_markup
    )

start_handler = CommandHandler("start", start)
