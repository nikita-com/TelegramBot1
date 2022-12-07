import telebot

bot = telebot.TeleBot('5803491014:AAGP1Fc4g1k_dcyhYYIL9EReGr6xVLstmpY')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '<b>привет<b>, ты написал мне /start', parse_mode="HTML")


bot.polling()
