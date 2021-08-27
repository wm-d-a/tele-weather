import telebot
from weather import *
from tokens import token
import datetime

bot = telebot.TeleBot(token)


def log(user, command, *args):  # Logging by template: <date an time> <chat id> <command> <other options>
    now = datetime.datetime.now()
    logs = open('log.txt', 'a')
    log_message = f'[{str(now)}] id: {user}, {command}, {"; ".join(args)}'
    logs.writelines(log_message + '\n')
    logs.close()
    print(log_message)


def main():
    @bot.message_handler(commands=['start', 'help'])
    def send_welcome(message):
        bot.reply_to(message,
                     f"Hello {message.from_user.first_name}, "
                     f"this is a simple bot for receiving current weather information. \nTo start entering /weather")
        log(message.from_user.id, '/start')

    @bot.message_handler(func=lambda m: True)
    def main_func(message):  # Здесь пишется логика
        if message.text == '/weather':
            try:
                log(message.from_user.id, '/weather')
                bot.send_message(message.from_user.id, 'Enter the name of the city')
                bot.register_next_step_handler(message, weather)

            except Exception:
                bot.send_message(message.from_user.id, 'There was a sudden error, take a try again later')
                log(message.from_user.id, '/weather', 'Error in : /weather')
        else:
            log(message.from_user.id, "announced user message", message.text)

    def weather(message):
        try:
            log(message.from_user.id, '/weather', message.text)
            bot.send_message(message.from_user.id,
                             f'Today in {message.text.capitalize()}: {current_weather(message.text)}')
            log(message.from_user.id, '/weather', 'send_message')
        except Exception:
            bot.send_message(message.from_user.id, 'There was a sudden error, take a try again later')
            log(message.from_user.id, '/weather',
                'Error in : There was a sudden mistake, check the name of the city or try again later (/weather)')

    bot.polling()


try:
    main()
except Exception:
    log(user='', command='\nREBOOT\n')
    main()
