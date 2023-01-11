from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, ConversationHandler
from bot_commands import * 
import logging

app = ApplicationBuilder().token("5958633509:AAGYmrrD4zqGGWcIrFYFBmCX1lA0g5MitY4").build()

app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("rational", rational_command))
app.add_handler(CommandHandler("complex", complex_command))

app.run_polling()