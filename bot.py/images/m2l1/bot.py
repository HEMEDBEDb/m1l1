#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot,random,os,requests


API_TOKEN = '7719709512:AAENsOyztaT_gh7mPwc_THeBfn111UR7a4A'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']
    
    
@bot.message_handler(commands=['duck'])
def duck(message):
    '''По команде duck вызывает функцию get_duck_image_url и отправляет URL изображения утки'''
    image_url = get_duck_image_url()
    bot.reply_to(message, image_url)

def get_fox_image_url():    
        url = 'https://randomfox.ca/floof/'
        res = requests.get(url)
        data = res.json()
        return data['image']
    
@bot.message_handler(commands=['fox'])
def fox(message):
        '''По команде fox вызывает функцию get_fox_image_url и отправляет URL изображения лисы'''
        image_url = get_fox_image_url()
        bot.reply_to(message, image_url)

def get_dog_image_url():    
        url = 'https://random.dog/woof.json'
        res = requests.get(url)
        data = res.json()
        return data['url']
    
    
@bot.message_handler(commands=['dog'])
def dog(message):
        '''По команде dog вызывает функцию get_dog_image_url и отправляет URL изображения собаки'''
        image_url = get_dog_image_url()
        bot.reply_to(message, image_url)



def get_anime_image_url():    
        url = 'https://kitsu.io/api/edge/anime?filter[text]=tokio'
        res = requests.get(url)
        data = res.json()
        return data['self']
    
    
@bot.message_handler(commands=['anime'])
def anime(message):
        '''По команде anime вызывает функцию get_anime_image_url и отправляет URL изображения анимэ'''
        image_url = get_anime_image_url()
        bot.reply_to(message, image_url)



@bot.message_handler(commands=['mem'])
def send_mem(message):
    image_dir="images"
    image = random.choice(os.listdir(image_dir))
    with open(f'{image_dir}/{image}', 'rb') as f:
        bot.send_photo(message.chat.id, f)
# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
