from telegram import Bot, Update
from telegram.ext import CommandHandler, Dispatcher
from django.conf import settings

from .handlers.commands import start

bot = Bot(settings.TOKEN)
dispatcher = Dispatcher(bot, None, workers=4, use_context=True)

dispatcher.add_handler(CommandHandler('start', start))



def hendle_update(data: dict):
    update = Update.de_json(data, bot)
    dispatcher.process_update(update)