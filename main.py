import telebot
from config import api
from script import who_is_your_goal

bot = telebot.TeleBot(api)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def info(message):
    bot.send_message(
        message.chat.id,
        who_is_your_goal(message.from_user.username)
    )


bot.polling()
