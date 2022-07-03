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
    with open('pagman/day1/intro.MOV', 'rb') as intro:
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
And so on till the /day30

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

Watch the video and repeat the sounds after me.

For premium subscribers: Record an audio of you pronouncing the words from the video (IN RED) and send it to Ainur @N_0ught. You can also ask him any questions, and he will be happy to answer them.""")
    with open('pagman/day1/day1.2.MOV', 'rb') as vid2:
        vid2 = vid2.read()
    update.message.reply_video(vid2)
    update.message.reply_text("""✍️ Task 2


Grab a pen and a piece of paper and try to write the letters in cursive:

https://www.notion.so/True-friends-b85b1f6e02ab4f2d935a237b3d225f92

You can take a picture of your handwriting and send it to our group chat.

For premium subscribers: send the picture of your handwriting to our teacher @N_0ught to receive additional feedback from him.""")


def day_two(update: Update, context: CallbackContext):
    update.message.reply_text("""2️⃣ Hey! How are you doing?

Today you will learn how to read and write False friends letters:


Bв, Ee, Hн, Pp, Cc, Уy, Xx 

They look like English letters but sound different

🗣Task 1 

Watch the video and repeat the sounds after me.

For premium subscribers: Record an audio of you pronouncing the words from the video (IN RED) and send it to Ainur @N_0ught. You can also ask him any questions, and he will be happy to answer them.""")
    with open('pagman/day2/day2.1.MOV', 'rb') as vid1:
        vid1 = vid1.read()
    update.message.reply_video(vid1)
    update.message.reply_text("""✍️ Task 2


Write the letters in cursive:

https://www.notion.so/False-friends-113023a91f5f4fb2971eaadfe6b6c381

You can take a picture of your handwriting and send it to our group chat.

For premium subscribers: send the picture of your handwriting to our teacher @N_0ught to receive additional feedback from him.""")


def day_three(update: Update, context: CallbackContext):
    update.message.reply_text("""3️⃣ Hey there! How are you today?

Today we will meet “New friends letters”:


Бб, Гг, Дд, 3з, Ии, Лл, Пп, Фф, Ээ

They look different but sound like English letters.

🗣Task 1 

Watch the video and repeat the sounds after me.

For premium subscribers: Record an audio of you pronouncing the words from the video (IN RED) and send it to Ainur @N_0ught. You can also ask him any questions, and he will be happy to answer them.""")
    with open('pagman/day3/day3.1.MOV', 'rb') as vid1:
        vid1 = vid1.read()
    update.message.reply_video(vid1)
    update.message.reply_text("""✍️ Task 2


Write the letters in cursive:

https://www.notion.so/New-friends-d37d29c1b8764547b9b79411d5a424b7

You can take a picture of your handwriting and send it to our group chat.

For premium subscribers: send the picture of your handwriting to our teacher @N_0ught to receive additional feedback from him.""")


def day_four(update: Update, context: CallbackContext):
    update.message.reply_text("""4️⃣ Privet! What’s up?

Our today’s topic is “Stranger letters”. They look and sound different from English letters. These are:

Её, Жж, Ий, Цц, Чч, Шш, Щщ, Ыы, Юю, Яя 

+ letters that don’t produce a sound: + Ъъ (твёрдый знак [tvyordyj znak] - hard sign), Ьь (мягкий знак [myahkij znak] - soft sign).

They are applied to separate the two sounds that precede and follow these letters or make a preceding consonant softer (ь). Watch the videos 3 and 4 to see the examples ⬇️

🗣Task 1 

Watch the videos and repeat the sounds after me.

For premium subscribers: Record an audio of you pronouncing the sounds and the words (videos 2,3 and 4) and send it to Ainur @N_0ught. You can also ask him any questions, and he will be happy to answer them.""")
    with open('pagman/day4/day4.1.MOV', 'rb') as vid1:
        vid1 = vid1.read()
    update.message.reply_video(vid1)
    with open('pagman/day3/day4.2.MOV', 'rb') as vid2:
        vid2 = vid2.read()
    update.message.reply_video(vid2)
    with open('pagman/day3/day4.3.MOV', 'rb') as vid3:
        vid3 = vid3.read()
    update.message.reply_video(vid3)
    with open('pagman/day3/day4.4.MOV', 'rb') as vid4:
        vid4 = vid4.read()
    update.message.reply_video(vid4)
    update.message.reply_text("""✍️ Task 2


Write the letters in cursive:

https://www.notion.so/Strangers-bba5af8f0fc94ea48247554c1edab72b

You can take a picture of your handwriting and send it to our group chat.

For premium subscribers: send the picture of your handwriting to our teacher @N_0ught to receive additional feedback from him.""")


def day_five(update: Update, context: CallbackContext):
    update.message.reply_text("""5️⃣ Hey! So now know all the letters and it’s time to learn more about the rules of words pronunciation.

The Russian alphabet makes pronouncing the Russian language quite easy. Russian words almost always sound exactly as they are written. That means your Russian pronunciation will likely be much more advanced than if you were speaking another foreign language.

There are 10 vowels and 21 consonants in Russian:

Гласные буквы (vowels): а, я, о, е, у, ю, ы, и, э, е. 

Согласные буквы (consonants): б, п, в, ф, г, к, д, т, з, с, ж, ш, щ, ч, х, л, м, н, р, ц. й. 

*Буква (pl. буквы) - a letter(s)

🗣 Task 1

Record yourself pronouncing the words and sentences and send your audio to the teacher if you have a premium subscription:

Том, Инна и Áнна, мáма, пáпа, дом, он, она, это, тут, там, банáн, батóн, нóта. Это банáн (this is a banana). Это мáма и пáпа (these are a mother and a father). Тут Том (Tom is here). Там дом (the house is there). 

Pay attention to the stress of the words!

✍️ Task 2

Try to write the words and sentences above using Russian cursive ⬆️

For premium subscribers: take a picture of your writings and send it to the teacher.""")


def day_six(update: Update, context: CallbackContext):
    update.message.reply_text("""6️⃣ Hello-hello! Hopefully you’re doing fine and you’re ready to continue learning more about Russian phonetics.

As you’ve probably noticed, reading in Russian is not that tough. However there are some rules to keep in mind:

1. O is pronounced like “a” in case it’s not stressed (онА, овАл, хорошО* [а])
2. Voiced letters (б, г, д, з, в, ж) are pronounced like their breath couples (п, к, т, с, ф, ш) if they are at the very end of a word (год [т] (even before ь – любовь [фь]) or if preceded by another breath letter (ex. лодка [тк]) Watch the video with examples ⬇️""")
    with open('pagman/day6/day6.1.MOV', 'rb') as vid1:
        vid1 = vid1.read()
    update.message.reply_video(vid1)
    update.message.reply_text("""3. The letter ё is always stressed. Ex. ёршик, ёжик, ёлка
4. After consonants г, к, х, ж, ш, щ, ч  do NOT! write the letter ы. Whenever an [ы] or [и] sound follows one of these letters, it is spelled и. This is called 7-letter spelling rule.
ex. жир, цирк, шить, чипсы [ы]

* Stressed letters are in capitals

The interesting fact about Russian Russian stress is unpredictable as it's not fixed and may change in different forms of a word. Therefore, one needs to memorize every single word with its stress.

🗣 Task 
Read the following words out loud (the stressed letters are written in capitals) and record yourself:

ты, юг, яд, сон, сын, вор, дуб, зол, лоб, нож, ров, рёв, нет, парк, пруд, дождь, гость, груз, столб, друг, порОг, оврАг, брошь, дрожь, вещь, вЕщи, фОрум, Арка, бИрка, рЫнок, абрикОс, ананАс, апельсИн, боЮсь, бьюсь, востОк, ворОна, вЕшалка, вИдишь, вЫберешь, вьЮга, гАлка, глЯнец, говорИть, дьяк, енОт, ЕлЕна (name), есть, ёж, ёлка, котёнок, ножИ, жизнь, женА, жрИца, зарЯ, знать, игрА, йод, йОгурт, конь, кость, копАть, капюшОн, ломАть, лЯмка, морОз, норА, Остров, овАл, огорОд, пЕчка, тёмный, Утка, Умный, фен, фамИлия, цАпля, цОкать, цИркуль, цыплёнок, чАща, чУдо, шАрка, шОрох, щи, щЁтка, Эра, Южный, Ярко, ядрО, Ясень, бАнщик.

Send the audio to the teacher if you have a premium subscription.""")


def day_seven(update: Update, context: CallbackContext):
    update.message.reply_text("""7️⃣ Hey! Congrats! You’re already 1 week through and you are able to read and write in Russian 👍

Today is a chill day for you. Play a fun game where you have to match Russian words with the imagies that they depict using your gut feeling (you know, there are plenty of words that derive from English and other languages, so it will be easy to guess the meaning of the vocabulary).

👾Task 1 


Play the game, take a screenshot upon the completion, and send it to the teacher (if you have a premium subscription):
https://wordwall.net/resource/18103040

✍️Task 2

Remember that Tiktok video that we showed you at the beginning of the course? Now you can write the sentence «Шиншилла лишилась мишки» (chinchilla lost her bear addition) yourself! 

You can practice by using these propisi first:
shorturl.at/dnATV

Take a picture of your handwriting and share it in the chat!""")


def booba(update: Update, context: CallbackContext):
    with open('pagman/secret_booba.jpg', 'rb') as pict:
        f = pict.read()
    update.message.reply_text("Oh, you've discovered the secret command! Congratulations! Enjoy your bonus ;)")
    update.message.reply_photo(f)


def echo(update, context):
    update.message.reply_text(update.message.text)


def invalid_command(update, context):
    update.message.reply_text('Invalid command. Please, check if you typed it correctly.')


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', helpers))
updater.dispatcher.add_handler(CommandHandler('day1', day_one))
updater.dispatcher.add_handler(CommandHandler('day2', day_two))
updater.dispatcher.add_handler(CommandHandler('day3', day_three))
updater.dispatcher.add_handler(CommandHandler('day4', day_four))
updater.dispatcher.add_handler(CommandHandler('day5', day_five))
updater.dispatcher.add_handler(CommandHandler('day6', day_six))
updater.dispatcher.add_handler(CommandHandler('day7', day_seven))
updater.dispatcher.add_handler(CommandHandler('secret', booba))
updater.dispatcher.add_handler(MessageHandler(Filters.command, invalid_command))
updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))


# updater.start_polling()
updater.start_webhook(listen="0.0.0.0",
                      port=int(PORT),
                      url_path=TOKEN,
                      webhook_url='https://russian-course-tg-bot.herokuapp.com/' + TOKEN)

