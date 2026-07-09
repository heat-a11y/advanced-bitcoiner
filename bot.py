from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

TOKEN = "8367515812:AAFOpypv7Ko7FmsqbtBPH76fuZspbY3297A"

async def start(update: Update, _):
    await update.message.reply_text("Hello! I'm alive and responding.")

async def echo(update: Update, _):
    await update.message.reply_text(f"You said: {update.message.text}")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

print("Bot is polling... Send /start to @clawdy9876bot")
app.run_polling(allowed_updates=Update.ALL_TYPES)
