import logging
import os

from telegram.ext import ApplicationBuilder

from handlers import handlers


API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")
PROXY_URL = os.getenv("TELEGRAM_PROXY_URL")
PROXY_LOGIN=os.getenv("TELEGRAM_PROXY_LOGIN"),
PROXY_PASSWORD=os.getenv("TELEGRAM_PROXY_PASSWORD")
ACCESS_ID = os.getenv("TELEGRAM_ACCESS_ID")


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    handlers=[
        logging.FileHandler('output.log', mode='w'),
    ]
)


def main():
    app = ApplicationBuilder().token(API_TOKEN).proxy_url(PROXY_URL).build()
    app.add_handlers(handlers)

    app.run_polling()