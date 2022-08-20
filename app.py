import telebot


TOKEN = '5714731812:AAGDG6nJWBrGXyFxjWH2T8p4Uh3wrvE4j0s'


bot = telebot.TeleBot(TOKEN)

keys = {
    'рубрь': 'RUB',
    'доллар': 'USD',
    'евро': 'EUR',
}


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'чтобы начать работу введите команду боту в следующем формате: \n<имя валюты> \
<валюту в которую перевести> \
<количество переводимой валюты> \nУвидеть список всех доступных валют: /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)


bot.polling()
