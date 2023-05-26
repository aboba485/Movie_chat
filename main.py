import telebot 
import sqlite3 as sq
from datetime import datetime, timedelta

bot = telebot.TeleBot("5944168958:AAFEijWVNH4iS3r5e27AL5klXTVoV28EroU")

#кнопки для старта
start = telebot.types.ReplyKeyboardMarkup(True,True)
start.row('Начать генерацию идеального фильма или сериала','Показать результаты последней генерации')

#кнопки для жанра 
genre = telebot.types.ReplyKeyboardMarkup(True,True)
genre.row('приключения','триллеры','боевик','фантастика','драма','комедия','ужасы','фэнтези','семейный','по профессиям')

#кнопки для возрастной группы
age_group = telebot.types.ReplyKeyboardMarkup(True,True)
age_group.row('0-7','7-12','12-15','15-18','18-30','30-50')

#команда для картинки
def send_photo(message):
    photo = open('movie_logo.png', 'rb')
    bot.send_photo(message.chat.id, photo)

#стартовая команда
@bot.message_handler(commands=['start','bazium'])
def start(message):
    #подключение к базе данных (main) и создание курсора
    db = sq.connect("main.db")
    cursor = db.cursor()
    #получение ника пользователя
    nickname = message.from_user.username
    #проверка наличия пользователя в базе данных
    cursor.execute("SELECT user_name FROM users WHERE user_name=?", (nickname,))
    # if cursor.fetchone is None:
    send_photo(message)
    bot.send_message(message.chat.id, f"""Привет! Ты зашел в <strong>Movie Chat</strong>.
    Тут мы поможем тебе подобрать идеальный фильм на вечер.
                            <strong>Инструкция</strong>""",parse_mode='HTML',reply_markup=genre)
@bot.message_handler(content_types=['text'])
def send_text(message):
        #если юзер нажал кнопку 'приключения'
        if message.text == 'приключения': 
             
        elif message.text == 'триллеры':
             
        elif message.text == 'триллеры':

        elif message.text == 'триллеры':

        elif message.text == 'триллеры':

        elif message.text == 'триллеры':

        elif message.text == 'триллеры':

        elif message.text == 'триллеры':

0       
#бесконечное обновление бота
bot.infinity_polling() 