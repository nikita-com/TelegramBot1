import telebot

bot = telebot.TeleBot('5803491014:AAGP1Fc4g1k_dcyhYYIL9EReGr6xVLstmpY')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'привет, ты написал мне /start')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Я вас приведствую')
    elif message.text == 'Пока':
        bot.send_message(message.chat.id, 'Увидимся')

bot.polling()
