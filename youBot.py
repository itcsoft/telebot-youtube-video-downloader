import telebot
from pytube import YouTube
import os
import datetime
# url = input('Input url from youtube: ')
# YouTube(url).streams.first().download('vid')
# # video = YouTube(url)
# print(datetime.datetime.now())
current_path = os.path.abspath(os.getcwd())
token = '2039095102:AAFVPFbZ2cpxlng9RGSFYY7KPFbFD2Cc1qs'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'старт'])
def start_message(message):
    username = message.from_user.first_name
    mess  = 'Привет '+ username +', просто отправь мне ссылку на видео из Youtube и скачаю его!!!'
    bot.send_message(message.chat.id, mess)


@bot.message_handler(content_types='text')
def downloader(message):
    url_from_youtube = message.text
    down_path = current_path+'/videos/'
    filename = str(datetime.datetime.now())
    yout = YouTube(url_from_youtube)
    bot.send_message(message.chat.id, 'Пожалуйста подождите! \nВаше видео уже в пути...')
    YouTube(url_from_youtube).streams.filter(res="720p").first().download(filename=filename, output_path=down_path)
    path_url = down_path + filename
    vid = open(path_url, 'rb')
    bot.send_video(message.chat.id, vid)


print('Bot is working!')
bot.infinity_polling()
