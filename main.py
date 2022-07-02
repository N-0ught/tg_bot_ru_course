from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import logging
import os

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)
TOKEN = os.getenv('TOKEN')
PORT = os.getenv('PORT')
updater = Updater(TOKEN, use_context=True)


def start(update: Update, context: CallbackContext):
    with open('pagman/day1/intro.mp4', 'rb') as intro:
        intro = intro.read()
    update.message.reply_video(intro)
    update.message.reply_text("""Привéт! (Hi!) Добрó пожáловать на курс! 🙋🏻‍♀️

Welcome to the course where you will learn all the basics of Russian phonetics, grammar, and vocabulary 🇷🇺

The course will teach you how to hold basic conversations on topics such as acquaintance, family, weather, hobbies, in the shop, at the restaurant, etc.

So please stay tuned and let’s get it started! 🚀

Please, enter the /help command to start the course and get more info!""")


def helpers(update: Update, context: CallbackContext):
    update.message.reply_text("""
Here begins your journey on our course, dear foreigner! To get the daily doze of info, please, write:

/day1 - To get the first day's materials
/day2 - To get the second day's materials
And so on till the /day60!

We wish you good luck!""")


def day_one(update: Update, context: CallbackContext):
    with open('pagman/day1/day1.1.jpg', 'rb') as pic:
        pic = pic.read()
    update.message.reply_photo(pic)
    update.message.reply_text("""1️⃣ Privét! Welcome to the first day of your Russian journey! 👋

This week you will learn how to read and write Russian letters.

By the end of the week you will be able to write this ⬇️

Russian alphabet is based on the Cyrillic script. Here you can see the letters with their Latin transcriptions ⬆️""")
    with open('pagman/day1/day1.1.MP4', 'rb') as vid1:
        vid1 = vid1.read()
    update.message.reply_video(vid1)
    update.message.reply_text("""We can divide all the letters into 4 smaller groups:

True friends: Aa, Kк, Мм, Oo, Tт (look and sound like English letters) 
False friends: Bв, Ee, Hн, Pp, Cc, Уy, Xx (look like English letters but sound different) 
New friends: Бб, Гг, Дд, 3з, Ии, Лл, Пп, Фф, Ээ (look different but sound like English letters) 
Strangers: Её, Жж, Ий, Цц, Чч, Шш, Щщ, Ыы, Юю, Яя (look and sound different)

+ Ъъ (твёрдый знак [tvyordyj znak] - hard sign), Ьь (мягкий знак [myahkij znak] - soft sign) that don't produce any sound! You will learn about their functions later.

Today you will learn more about true friends.


Do the tasks and send your results to our teacher Ainur @N_0ught if you have a premium subscription 🧑🏻‍🏫""")
    update.message.reply_text("""🗣Task 1 

Watch the video and repeat the sounds after me:

For premium subscribers: Record an audio of you pronouncing the sounds and send it to Ainur @N_0ught. You can also ask him any questions, and he will be happy to answer them.""")
    with open('pagman/day1/day1.2.mp4', 'rb') as vid2:
        vid2 = vid2.read()
    update.message.reply_video(vid2)
    update.message.reply_text("""✍️ Task 2


Grab a pen and a piece of paper and try to write the letters in cursive:

https://www.notion.so/True-friends-b85b1f6e02ab4f2d935a237b3d225f92

You can take a picture of your handwriting and send it to our group chat.

For premium subscribers: send the picture of your handwriting to our teacher @N_0ught to receive additional feedback from him.""")


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
updater.dispatcher.add_handler(MessageHandler(Filters.command, invalid_command))
updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))


# updater.start_polling()
updater.start_webhook(listen="0.0.0.0",
                      port=int(PORT),
                      url_path=TOKEN,
                      webhook_url='https://russian-course-tg-bot.herokuapp.com/' + TOKEN)

