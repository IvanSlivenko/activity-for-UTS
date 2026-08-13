from telegram.ext import ApplicationBuilder, MessageHandler, filters, CallbackQueryHandler, CommandHandler

from gpt import *
from util import *
# ------------------------------------------------------ telegramm
with open("pass.txt", "r", encoding="utf-8") as file:
    line = file.read().strip()

TELEGRAM_BOT_TOKEN = line.split("=", 1)[1]

TOKEN = TELEGRAM_BOT_TOKEN

# ---------------------------------------------------------- GPT
with open("GPT_KEY.txt", "r", encoding="utf-8") as file:
    line_2 = file.read().strip()

GPT_TOKEN = line_2.split("=", 1)[1]

TOKEN_GPT = GPT_TOKEN
# --------------------------------
async def start(update, context):

    msg = load_message("main")
    await send_photo(update, context, "main")
    await send_text(update, context, msg)
    await show_main_menu(update, context, {
        "start": "Головне меню ",
        "profile": "Генерація профіля\uD83D\uDE0E",
        "opener": "Повідомлення\uD83D\uDE08",
        "message": "Переписка від вашого імені\uD83D\uDE0E",
        "date": "Спілкування з зірками\uD83D\uDD25",
        "gpt": "Запитати у ChatGPT\uD83E\uDD0E",
    })

    await send_photo(update, context, "opener")
    await send_text(update, context,"Очікую повідомлень...")

async def gpt(update, context):
    dialog.mode = "gpt"
    await send_photo(update, context,"gpt")
    msg_gpt = load_message("gpt")
    await send_text(update, context, msg_gpt)

async def gpt_dialog(update, context):
    text = update.message.text
    prompt = load_prompt("gpt")
    answer = await chatgpt.send_question(prompt, text)
    await send_text(update, context, answer)


async def hello(update, context):
    if(dialog.mode == "gpt"):
        # await send_text(update, context, "GPT-mode")
        await gpt_dialog(update, context)
async def buttons_handler(update, context):
    query = update.callback_query.data
    if query == "start":
        await send_text(update, context, "Started")
    elif query == "stop":
        await send_text(update, context, "Stopped")

dialog = Dialog()
dialog.mode = None

chatgpt = ChatGptService(token=TOKEN_GPT)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("Start", start))
app.add_handler(CommandHandler("gpt", gpt))

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, hello ))
# app.add_handler(CallbackQueryHandler(buttons_handler))

app.run_polling()
