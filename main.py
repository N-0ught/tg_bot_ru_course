from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from telegram import Message
import os

BOT_API = os.environ.get('BOT_API')
PORT = os.getenv('PORT')
updater = Updater(BOT_API, use_context=True)


def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello, dear foreigner! Please, enter the /help command to "
                              "start the course and get more info!")


def helpers(update: Update, context: CallbackContext):
    update.message.reply_text("""
Here begins your journey on our course, dear foreigner! To get the daily doze of info, please, write:
/day1 - To get the first day's materials
/day2 - To get the second day's materials
And so on till the /day60!
We wish you good luck!""")


def day_one(update: Update, context: CallbackContext):
    update.message.reply_text('Welcome to the first day! To begin with, open the link and watch the video: '
                              'https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    update.message.reply_text('Ha-ha! Just kidding =)')


def day_two(update: Update, context: CallbackContext):
    update.message.reply_text('Ya, this is the content of Day 2: error:empty...')


def day_three(update: Update, context: CallbackContext):
    update.message.reply_text('Ya, this is the content of Day 3: error:empty...')


def booba(update: Update, context: CallbackContext):
    with open('pagman/ahegao.jpg', 'rb') as pict:
        f = pict.read()
    update.message.reply_text("Oh, you've discovered the secret command! Congratulations! Enjoy your bonus ;)")
    update.message.reply_photo(f)


def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def invalid_command(update, context):
    update.message.reply_text('Invalid command. Please, check if you typed it correctly.')


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', helpers))
updater.dispatcher.add_handler(CommandHandler('day1', day_one))
updater.dispatcher.add_handler(CommandHandler('day2', day_two))
updater.dispatcher.add_handler(CommandHandler('day3', day_three))
updater.dispatcher.add_handler(CommandHandler('secret', booba))
updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))
updater.dispatcher.add_handler(MessageHandler(Filters.command, invalid_command))

# updater.start_polling()
updater.start_webhook(listen="0.0.0.0",
                      port=int(PORT),
                      url_path=BOT_API)
updater.bot.setWebhook('https://yourherokuappname.herokuapp.com/' + BOT_API)
