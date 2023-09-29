from fastapi import FastAPI
import uvicorn
import telebot
import os
from dotenv import load_dotenv

load_dotenv(".env")
WEBHOOK_URL_BASE = os.getenv("WEBHOOK_URL_BASE")


bot = telebot.TeleBot(
    "6640408548:AAHND-JyRQEaRTsDu8Ge7bVJRnGQLHz-BzA", parse_mode=None)
secret = "unicorn"
app = FastAPI()


@app.post("/unicorn")
def process_webhook(update: dict):
    """
    Process webhook calls
    """
    if update:
        update = telebot.types.Update.de_json(update)
        bot.process_new_updates([update])
    else:
        return


@bot.message_handler(func=lambda message: True, content_types=['text'])
def send_welcome(message):

    bot.reply_to(message, message.text)


bot.remove_webhook()

# Set webhook
bot.set_webhook(
    url=WEBHOOK_URL_BASE + "unicorn"
)


uvicorn.run(
    app,
    host="0.0.0.0"
)
