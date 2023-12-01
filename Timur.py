import telebot
import psycopg2
from telebot import types
from datetime import *

dt = datetime.strptime(str(datetime.today())[2:-7], "%y-%m-%d %H:%M:%S")
week = dt.isocalendar()[1]

conn = psycopg2.connect(database="schedule_db",
                        user="postgres",
                        password="1234",
                        host="localhost",
                        port="5432")

cursor = conn.cursor()

token = "6979924108:AAFfjcD4urKPiVDEU_D_m87zwxnk16-arcQ"
bot = telebot.TeleBot(token)

def weekday(day: str, message):
    cursor.execute(
        f"SELECT * FROM days_table WHERE day='{day}{week % 2}'"
    )
    records = list(cursor.fetchall())
    raspis = []
    for i in records:
        for g in i:
            raspis.append(g)

    strok = ''
    g = 1
    for i in range(0, len(raspis), 6):
        strok += f'{g}. {raspis[i + 2]}\n    {raspis[i + 3]}\n    {raspis[i + 4]}\n    {raspis[i + 5]}\n\n'
        g += 1

    bot.send_message(message.chat.id, f'Рассписание на {week - 34}-ую неделю. {"Чётная" if week % 2 == 0 else "Нечётная"}')
    bot.send_message(message.chat.id, f'{day}\n____________\n\n{strok}\r____________')


def weekdaynext(day: str, message):
    cursor.execute(
        f"SELECT * FROM days_table WHERE day='{day}{(week+1) % 2}'"
    )
    records = list(cursor.fetchall())
    raspis = []
    for i in records:
        for g in i:
            raspis.append(g)

    strok = ''
    g = 1
    for i in range(0, len(raspis), 6):
        strok += f'{g}. {raspis[i + 2]}\n    {raspis[i + 3]}\n    {raspis[i + 4]}\n    {raspis[i + 5]}\n\n'
        g += 1

    bot.send_message(message.chat.id, f'{day}\n____________\n\n{strok}\r____________')


def weekday2(day: str, message):
    cursor.execute(
        f"SELECT * FROM days_table WHERE day='{day}{week % 2}'"
    )
    records = list(cursor.fetchall())
    raspis = []
    for i in records:
        for g in i:
            raspis.append(g)

    strok = ''
    g = 1
    for i in range(0, len(raspis), 6):
        strok += f'{g}. {raspis[i + 2]}\n    {raspis[i + 3]}\n    {raspis[i + 4]}\n    {raspis[i + 5]}\n\n'
        g += 1

    bot.send_message(message.chat.id, f'{day}\n____________\n\n{strok}\r____________')



@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("Хочу в МТУСИ", "Расписание", "/help")
    bot.send_message(message.chat.id, f'Здравствуйте {message.from_user.username}!',
                     reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я умею...')


@bot.message_handler(commands=['week'])
def start_message(message):
    if week % 2 == 0:
        bot.send_message(message.chat.id, 'Сейчас определённо ЧЁТНАЯ неделя')
    elif week % 2 != 0:
        bot.send_message(message.chat.id, 'Сейчас определённо НЕЧЁТНАЯ неделя')



@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "хочу в мтуси":
        bot.send_message(message.chat.id, 'Тогда тебе сюда - https://mtuci.ru/')
    elif message.text.lower() == "ghghgh":
        bot.send_message(message.chat.id, 'Тогда ghghgh')
    elif message.text.lower() == "расписание":
        global keyboard_schedule
        keyboard_schedule = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_monday = telebot.types.KeyboardButton('Понедельник')
        button_tuesday = telebot.types.KeyboardButton('Вторник')
        button_wednesday = telebot.types.KeyboardButton('Среда')
        button_thursday = telebot.types.KeyboardButton('Четверг')
        button_friday = telebot.types.KeyboardButton('Пятница')
        button_saturday = telebot.types.KeyboardButton('Суббота')
        button_now_week = telebot.types.KeyboardButton('Расписание на текущую неделю')
        button_next_week = telebot.types.KeyboardButton('Расписание на следующую неделю')
        keyboard_schedule.add(button_monday, button_tuesday, button_wednesday,
                          button_thursday, button_friday, button_saturday,
                          button_now_week, button_next_week)
        bot.send_message(message.chat.id, 'Меню с днями и не только', reply_markup=keyboard_schedule)


    if message.text.lower() == 'понедельник':
        weekday('Понедельник', message)

    elif message.text.lower() == 'вторник':
        weekday('Вторник', message)

    elif message.text.lower() == 'среда':
        weekday('Среда', message)

    elif message.text.lower() == 'четверг':
        weekday('Четверг', message)

    elif message.text.lower() == 'пятница':
        weekday('Пятница', message)

    elif message.text.lower() == 'суббота':
        weekday('Суббота', message)


    elif message.text.lower() == 'расписание на текущую неделю':
        bot.send_message(message.chat.id, f'Расписание на текущую {week - 34}-ую неделю. {"Чётная" if week % 2 == 0 else "Нечётная"}')
        weekday2('Понедельник', message)
        weekday2('Вторник', message)
        weekday2('Среда', message)
        weekday2('Четверг', message)
        weekday2('Пятница', message)
        weekday2('Суббота', message)


    elif message.text.lower() == 'расписание на следующую неделю':
        bot.send_message(message.chat.id, f'Расписание на следующую {week - 33}-ую неделю. {"Чётная" if week % 2 == 0 else "Нечётная"}')
        weekdaynext('Понедельник', message)
        weekdaynext('Вторник', message)
        weekdaynext('Среда', message)
        weekdaynext('Четверг', message)
        weekdaynext('Пятница', message)
        weekdaynext('Суббота', message)


    elif message.text.lower() != 'расписание' and message.text.lower() != 'хочу в мтуси' and message.text.lower() != '':
        bot.send_message(message.chat.id, 'Извените, я Вас не понял. Кратко ознакомиться с ботом вы можете при помощи команды /help')


bot.infinity_polling()