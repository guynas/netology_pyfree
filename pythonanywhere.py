import telebot
import random

token = ''

bot = telebot.TeleBot(token)

tasks = {}

def add_a_task(a_date, a_task):
  if a_date in tasks:
    tasks[a_date].append(a_task)
  else:
    tasks[a_date]=[]
    tasks[a_date].append(a_task)

HELP = '''/help - show app help
/add - add a task to a lisk (user will be asked on task name)
/show - print all the tasks
/random - add random task for today
/exit - exit program'''

random_tasks = ['random task for test', 'Написать письмо Гвидо', 'Выучить Python', 'Записаться на курс в Нетологию', 'Посмотреть 4-й сезон "Рик и Морти"']

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=['add'])
def add(message):
    command = message.text.split(maxsplit=2)
    a_date = command[1].lower()
    a_task = command[2]
    add_a_task(a_date, a_task)
    text = f'A task "{a_task}" added succesfully for a date "{a_date}"'
    # print(message.text)
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['random'])
def random_add(message):
    a_date = 'today'
    a_task = random.choice(random_tasks)
    text = f'A task "{a_task}" added succesfully for a date "{a_date}"'
    add_a_task('today',a_task)
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['show', 'print'])
def show(message):
    command = message.text.split(maxsplit=1)
    a_date = command[1].lower()
    text =''
    if a_date in tasks:
        text = a_date.upper() + '\n'
        for a_task in tasks[a_date]:
            text = text + '- ' + a_task + '\n'
    else:
        text = f'No tasks for a date {a_date}'
    bot.send_message(message.chat.id, text)

# @bot.message_handler(content_types=['text'])
# def echo(message):
#     word = 'Serge'
#     if word in message.text:
#         text = 'Hi, darling!'
#     else:
#         text = message.text
#     bot.send_message(message.chat.id, text)


# Постоянно обращается к серверам Telegram
bot.polling(none_stop=True)
