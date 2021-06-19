# -*- coding: UTF-8 -*-
import telebot
import random
import time
from info import BOT_TOKEN
import re


class Freq:
    def __init__(self):
        self.response = 10
        self.sticker = 30
        self.bubbling = 30

    def gettrue(self, type):
        result = random.randint(1, 100)
        if type == "response":
            return result < freq.response
        if type == "sticker":
            return result < freq.sticker
        if type == "bubbling":
            return result < freq.bubbling


def manipulate(text):
    result = random.randint(1, 100)
    if result < 10:
        text = text + "(确信)"
    elif result >= 10 and result < 20:
        text = text + "(恼)"
    elif result >= 20 and result < 40:
        if len(text) < 20:
            text_list = re.findall(".{1}", text)
            text = " ".join(text_list)

    return text


freq = Freq()


bot = telebot.TeleBot(BOT_TOKEN)
sticker_list = [
    "CAACAgUAAxkBAAECN7xggkVOWvhVSgkIAAGnFyc4Yyf4ZtcAAgkAA5vp8yZOw2NGK3TvFR8E",
    "CAACAgUAAxkBAAECOPVggrgb6JCJaAMlIVpoc-DPAAG4KEMAAhUAA5vp8ybQR1e_E0RRQh8E",
    "CAACAgUAAxkBAAECOPdggrgqlqr3r62w_3JXCqyeX44J9wACBgADm-nzJoYvUnAdpSOSHwQ",
    "CAACAgUAAxkBAAECOPlggrgz4EzcAd5cYhgOJ7-PCR0nAgACDgADm-nzJliy2zTOn4_vHwQ"
]
bubbling_list = ["草", "xswl", "绝了", "草生", "你书的队",
                 "真怪啊", "smjb", "太怪了我要死了", "麻了", "麻中麻", "全麻", "?", "差不多得了"]

reply_list = ["？", "¿"]


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "你倒是讲话啊（恼）")


@bot.message_handler(commands=['help'])
def send_reply(message):
    bot.reply_to(
        message, "@cedar_234 突发奇想写出来的一个bot。他的功能包括但不限于：时不时复读，时不时发怪图,etc")


message_prev = ""
has_replied = 0


@bot.message_handler(func=lambda message: True, content_types=['audio', 'photo', 'voice', 'video', 'document', 'text', 'location', 'contact', 'sticker'])
def echo_message(message):
    # time.sleep(3+random.randint(0, 10))
    global message_prev, has_replied
    if (message.text == message_prev and has_replied == 0):
        bot.send_message(message.chat.id, message.text)
        has_replied = 1

    if (message.text != message_prev):
        has_replied = 0

    if (has_replied == 0):
        if ("@cedar_234_bot" in message.text or "bot" in message.text):
            bot.send_message(
                message.chat.id, reply_list[random.randint(0, len(reply_list)-1)])
        else:
            if (freq.gettrue("response")):
                if freq.gettrue("bubbling"):
                    bot.send_message(
                        message.chat.id, bubbling_list[random.randint(0, len(bubbling_list)-1)])
                else:
                    if message.text:
                        bot.send_message(message.chat.id, manipulate(message.text))
                if (freq.gettrue("sticker")):
                    bot.send_sticker(
                        message.chat.id, sticker_list[random.randint(0, len(sticker_list)-1)])
        has_replied = 1

    message_prev = message.text


bot.infinity_polling()
