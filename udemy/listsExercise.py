todo_list = []
finished = False

while not finished:
  task = input('Enter a task for your to-do list. Press <enter> when done: ')
  if len(task) == 0:
    finished = True
  else:
    todo_list.append(task)
    print('Task added.')

print()
print('Todo List:')
print('-' * 16)
for task in todo_list:
  print(task)