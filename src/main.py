from task import Task
from taskbase import Taskbase


taskbase = Taskbase()
print("TaskManager by amig2004")

# check if taskbase exist
if Taskbase.checkBaseExist():
    # if yes -> load all of them from file
    taskbase.loadTasksFromFile()

while True:
    #set pointer position to 0,0
    print("\033[0;0H")
    # render tasks
    taskbase.printTasks()
    print()
    # render short summary (active, done today etc.)

    # display notifications here if necessary
    if not taskbase.saved:
        print("INFO: Tasks not saved")

    print()
    # display possible options to operate
    print("What do you want to do?")
    print("[1] - Add task")
    print("[2] - Switch task state")
    print("[3] - Delete task")
    print("...")
    print("[5] - Save task base")
    print("...")
    print("[0] - Quit")
    # handle user input

    try:
        action = int(input("(action) "))

    except ValueError:
        continue

    if action == 0:
        break 

    if action == 1:
        taskname = input('(New Task)')
        taskbase.addTask(taskname)

    if action == 2:
        tid = int(input('(Task ID)'))
        taskbase.switchState(tid)

    if action == 3:
        tid = int(input('(Task ID)'))
        taskbase.deleteTask(tid)1



print('Goodbye.')
