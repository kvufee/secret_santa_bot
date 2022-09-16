import telebot
import numpy as np
from config import api

bot = telebot.TeleBot(api)

@bot.message_handler(func=lambda message: True, content_types['text'])
def info(message):
    bot.send_message(message.chat.id,
                     'sosi')

dataset_unsh = [
    //paste data here
]
dataset_sh = {
    //shuffled data data here
}


def dataset_shuffle(dataset):
    return np.random.shuffle(dataset)

dataset_shuffle(dataset_unsh)

def correctivity_check(dataset_unshuffled, dataset_shuffled):
    for i in range(len(dataset_unshuffled)):
        if dataset_shuffled[i]== dataset_unshuffled[i]:
            return False
    return True

while not correctivity_check(dataset_unsh, [*dataset_sh.keys()]):
    dataset_shuffle(dataset_sh)

dict_of_members = {first:second for first, second in zip(dataset_unsh, dataset_sh)}

bot.polling()
