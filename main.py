import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    stik = open('stickers/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, stik)

    bot.send_message(message.chat.id, "Hello user!")


@bot.message_handler(content_types=['text'])
def lalala(message):
    bot.send_message(message.chat.id, message.text)

#run
bot.polling(none_stop=True)