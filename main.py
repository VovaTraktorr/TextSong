import lyricsgenius
import telebot
import flask
import os

server = flask.Flask(__name__)
app_name = 'textsong'

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


@server.route('/' + token, methods=['POST'])
def get_message():
      bot.process_new_updates([types.Update.de_json(flask.request.stream.read().decode("utf-8"))])
      return "!", 200

@server.route('/', methods=["GET"])
def index():
    print("hello webhook!")
    bot.remove_webhook()
    bot.set_webhook(url=f"https://{app_name}.herokuapp.com/{token}")
    return "Hello from Heroku!", 200


if __name__ == '__main__':
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))


