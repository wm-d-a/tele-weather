import telebot
from weather import *
from tokens import token

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello, I'm your first bot :D")


@bot.message_handler(func=lambda m: True)
def echo_all(message):  # Здесь пишется логика
    if message.text == '/weather':
        bot.send_message(message.from_user.id, 'Введи название города')
        bot.register_next_step_handler(message, weather)


def weather(message):
    bot.send_message(message.from_user.id, f'Сегодня в {message.text}: {current_weather(message.text)}')


bot.polling()
