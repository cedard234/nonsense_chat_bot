import telebot
import random
import time
from info import BOT_TOKEN


class Freq:
    def __init__(self):
        self.response = 10
        self.sticker = 30
        self.bubbling = 50

    def gettrue(self, type):
        result = random.randint(1, 100)
        if type == "response":
            return result < freq.response
        if type == "sticker":
            return result < freq.sticker
        if type == "bubbling":
            return result < freq.bubbling


freq = Freq()


bot = telebot.TeleBot(BOT_TOKEN)
sticker_list = [
    "CAACAgUAAxkBAAECN7xggkVOWvhVSgkIAAGnFyc4Yyf4ZtcAAgkAA5vp8yZOw2NGK3TvFR8E",
    "CAACAgUAAxkBAAECOPVggrgb6JCJaAMlIVpoc-DPAAG4KEMAAhUAA5vp8ybQR1e_E0RRQh8E",
    "CAACAgUAAxkBAAECOPdggrgqlqr3r62w_3JXCqyeX44J9wACBgADm-nzJoYvUnAdpSOSHwQ",
    "CAACAgUAAxkBAAECOPlggrgz4EzcAd5cYhgOJ7-PCR0nAgACDgADm-nzJliy2zTOn4_vHwQ"
]
bubbling_list = ["草", "xswl", "绝了", "草生", "你书的队",
                 "真怪啊", "smjb", "太怪了我要死了", "麻了", "麻中麻", "全麻", "?"]


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "@cedar_234的bot一只")


@bot.message_handler(func=lambda message: True, content_types=['audio', 'photo', 'voice', 'video', 'document', 'text', 'location', 'contact', 'sticker'])
def echo_message(message):
    # time.sleep(3+random.randint(0, 10))
    if (freq.gettrue("response")):
        if freq.gettrue("bubbling"):
            bot.send_message(
                message.chat.id, bubbling_list[random.randint(0, len(bubbling_list)-1)])
        else:
            if message.text:
                bot.send_message(message.chat.id, message.text)
        if (freq.gettrue("sticker")):
            if (freq.gettrue("sticker")):
                bot.send_sticker(
                    message.chat.id, sticker_list[random.randint(0, len(sticker_list)-1)])


bot.polling()
