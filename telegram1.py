import telebot
import datetime

bot = telebot.TeleBot('5803491014:AAGP1Fc4g1k_dcyhYYIL9EReGr6xVLstmpY')

keybord1 = telebot.types.ReplyKeyboardMarkup(True)
keybord1.row('Привет', 'Пока', 'какое число?', 'сколко времени?')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'привет, ты написал мне /start', reply_markup=keybord1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Я вас приведствую')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Увидимся')
    elif message.text.lower() == 'какое число?':
        bot.send_message(message.chat.id, datetime.date.today().strftime('%y, %b., %d'))
    elif message.text.lower() == 'сколко времени?':
        bot.send_message(message.chat.id, datetime.datetime.today().strftime('%H:%M'))

bot.polling()
