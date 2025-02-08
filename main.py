#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot, time, threading, schedule
from bot_logic import gen_pass, dice
from time import sleep, time
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = '7719709512:AAENsOyztaT_gh7mPwc_THeBfn111UR7a4A'
Group_ID = -7719709512

bot = telebot.TeleBot(API_TOKEN)

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, f"Привет! Меня заовут {bot.get_me().first_name}")

# Handle '/hi'
@bot.message_handler(commands=['hi'])
def send_hi(message):
    bot.reply_to(message, """\
hello
""")

# Handle '/pass' and '/genpass'
@bot.message_handler(commands=['pass', 'genpass'])
def send_password(message):
    count = int(message.text.split()[1]) if len(message.text.split())>1 else 10
    password = gen_pass(count)  # Устанавливаем длину пароля, например, 10 символов
    bot.reply_to(message, f"Вот твой сгенерированный пароль: {password}")    

@bot.message_handler(commands=['dice'])
def dice_d6(message):
    count = int(message.text.split()[1]) if len(message.text.split())>1 else 6
    dice_roll = dice(count)
    bot.reply_to(message, f"Вот твой бросок кубика({count}): {dice_roll}")

@bot.message_handler(commands=['id'])
def send_welcome(message):
    bot_id =bot.get_me().id
    bot.reply_to(message, f"ID: {bot_id}")


#КОД ДОБАВЛЯТЬ ВЫШЕ

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()
