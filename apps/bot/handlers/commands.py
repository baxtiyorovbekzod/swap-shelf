from telegram import Update
from telegram.ext import CallbackContext

def start(update: Update, context: CallbackContext):
    update.message.reply_text('Salom, botga xush kelibsiz!')
    

def help(update: Update, context: CallbackContext):
    update.message.reply_text('Yordam uchun /help buyrug\'ini bering.')
    