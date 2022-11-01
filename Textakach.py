import lyricsgenius
import telebot

token_bot = '5730187466:AAFnMBPmpjTaSsDUETk-Ek9rCEV5e5NvCzg'
bot = telebot.TeleBot(token_bot)

token = 'oqQOQ34HAOM0Q3UBUFFyjtWCfbUFO-43Lk5xwjrm7novrV8a6M1lBiH7Xx5Mvxgh'
genius = lyricsgenius.Genius(token)

@bot.message_handler(commands = ['start'])
def start(msg):
    bot.send_message(msg.chat.id, 'Введи название своей артиста/групы и трек через пробел.')

@bot.message_handler(content_types=['text'])
def lyrics (msg):
    result = msg.text.split('-')

    song = genius.search_song(result[1], result[0])
    bot.send_message(msg.chat.id, song.lyrics)


bot.polling()
