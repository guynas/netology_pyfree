import random

HELP = """/help - show app help
/add - add a task to a lisk (user will be asked on task name)
/show - print all the tasks
/random - add random task for today
/exit - exit program"""

# random_task = 'random task for test'
random_tasks = ['random task for test', 'Написать письмо Гвидо', 'Выучить Python', 'Записаться на курс в Нетологию', 'Посмотреть 4-й сезон "Рик и Морти"']

tasks = {}

def add_a_task(a_date, a_task):
  if a_date in tasks:
    tasks[a_date].append(a_task)
  else:
    tasks[a_date]=[]
    tasks[a_date].append(a_task)
  print(f'A task "{a_task}" added succesfully for a date "{a_date}"')
  # print('A task', a_task, 'added for a date:', a_date)

while True:
  command = input('Enter a command: ')
  
  if command == 'help':
    print(HELP)
  
  elif command == 'show':
    a_date = input ('Type a date for printing: ')
    if a_date in tasks:
        for a_task in tasks[a_date]:
          print ('- ', a_task)
    else:
      print(f'No tasks for a date "{a_date}"')
    # print(tasks)
  
  elif command == 'add':
    a_date = input ('Type a date: ')
    a_task = input('Type a task: ')
    add_a_task(a_date, a_task)
    # if a_date in tasks:
    #   tasks[a_date].append(a_task)
    # else:
    #   tasks[a_date]=[]
    #   tasks[a_date].append(a_task)
    # or
    # tasks[a_date] = [a_task]
    # print(f'A task "{a_task}" added succesfully on a date "{a_date}"')
  
  elif command == 'exit':
    break
  
  elif command == 'random':
    a_task = random.choice(random_tasks)
    add_a_task('today', a_task)
    # if 'today' in tasks:
    #   tasks['today'].append(random_task)
    # else:
    #   tasks['today']=[]
    #   tasks['today'].append(random_task)
    #   print(f'Random task added succesfully for today')

  else:
    print("Unknown command")

print("Thanks fot using! Bye!")
