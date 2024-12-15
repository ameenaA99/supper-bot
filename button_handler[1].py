from telegram import Update
from telegram.ext import CallbackQueryHandler, ContextTypes

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == 'info':
        await query.edit_message_text(
            text="🤖 **معلومات البوت**

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
    elif query.data == 'settings':
        await query.edit_message_text(
            text="⚙️ **إعدادات البوت**

"
            "1️⃣ تعديل الإشعارات
"
            "2️⃣ إدارة الحساب
"
            "3️⃣ تفعيل الوضع الليلي
"
        )
    elif query.data == 'contact':
        await query.edit_message_text(
            text="📞 **تواصل معنا**

"
            "🔹 واتساب: +212770905027
"
            "🔹 إنستغرام: https://www.instagram.com/youness.amraoui01/
"
        )

button_callback = CallbackQueryHandler(button_callback)
