import os
from telegram.ext import ApplicationBuilder

from handlers.start_handler import start_handler
from handlers.help_handler import help_handler
from handlers.info_handler import info_handler
from handlers.button_handler import button_callback

from utils.config import BOT_TOKEN

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(start_handler)
app.add_handler(help_handler)
app.add_handler(info_handler)
app.add_handler(button_callback)

if __name__ == '__main__':
    print("🚀 البوت شغال الآن!")
    app.run_polling()
