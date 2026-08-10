from telegram.ext import ApplicationBuilder, MessageHandler, filters, CallbackQueryHandler, CommandHandler

from gpt import *
from util import *

with open("pass.txt", "r", encoding="utf-8") as file:
    line = file.read().strip()

TELEGRAM_BOT_TOKEN = line.split("=", 1)[1]

TOKEN = TELEGRAM_BOT_TOKEN

async def start(update, context):

    msg = load_message("main")
    await send_text(update, context, msg)

    await send_photo(update, context, "opener")
    await send_text(update, context,"Очікую повідомлень...")

async def hello(update, context):
    # await send_text(update, context, "Доброго дня " + update.message.text)
    await send_text_buttons(update, context, "Доброго дня " + update.message.text, {
        "start": "START",
        "stop": "STOP"
    })
async def buttons_handler(update, context):
    query = update.callback_query.data
    if query == "start":
        await send_text(update, context, "Started")
    elif query == "stop":
        await send_text(update, context, "Stopped")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("Start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, hello ))
app.add_handler(CallbackQueryHandler(buttons_handler))

app.run_polling()
