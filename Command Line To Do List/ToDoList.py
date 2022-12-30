
def addTask(task, taskList):
    extraValue = task.split(" ")[0]
    taskName = task.replace(extraValue, "")

    taskName = taskName.replace("add ", "")


    if (taskName == ""):
        print("type 'exit' if you'd like to exit")
        while (taskName == ""):
            addedTask = input("please enter todo item: ")


            if(addedTask.__contains__("exit")):
                break;


            addedTask = str(len(taskList) + 1) + " " + addedTask
            taskList.append(addedTask)

    else:
        appendValue = str(len(taskList) + 1) + " " + taskName
        taskList.append(appendValue)


def showTask():
    if (len(taskList) == 0):
        print('your list is empty! Use "add" to add to it')
    else:
        for item in taskList:
            print(item)


def completeTask(task):
    taskNum = task.split()[1] - 1
    del taskList[taskNum]

    for item in taskList:
        print(item)


#start of main

print("Welcome to the todo app!")

task = ""
taskList =[]

while (True):
    task = input("enter a task: add, show, complete, or exit:")
    if (task.__contains__("add")):
        addTask(task, taskList)
    if (task.__contains__("exit")):
        break
    if(task.__contains__("show")):
        showTask()
    if(task.__contains__("complete")):
        completeTask(task)
