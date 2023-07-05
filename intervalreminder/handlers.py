from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

from intervalreminder.labels import BOT_DESCRIPTION

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text=BOT_DESCRIPTION
    )


handlers = [
    CommandHandler('start', start)
]