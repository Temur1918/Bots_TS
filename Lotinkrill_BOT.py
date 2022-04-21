# Temurbek Yorkulov

# 21.04.2022

"""So'zlarni Lotin Alifbosidan Krill Alifbosiga O'tkazadi"""

from transliterate import to_cyrillic , to_latin
import telebot

bot = telebot.TeleBot("5392121450:AAH9_4Etekb9zlWnfb5eEWuprPOPf5JKo8A", parse_mode=None)

@bot.message_handler(commands = ['start'])
def send_welcome(message):
    javob = "Assalomu Alaykum \nBotimizga Xush Kelibsiz!"
    javob += "\nMatn Kiriting:"
    bot.reply_to(message, javob)

@bot.message_handler(func = lambda message: True)
def echo_all(message):
    msg = message.text
    javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    
    # if msg.isascii():
    #     javob = to_cyrillic(msg)
    # else:
  
    bot.reply_to(message, javob(msg))


bot.polling()

