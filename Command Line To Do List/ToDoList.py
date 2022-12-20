
def addTask(task, taskList):
    extraValue = task.split(" ")[0]
    taskName = task.replace(extraValue, "")
    taskNum = len(taskList) + 1
    appendValue = str(taskNum) + " " + taskName

    if(appendValue.__contains__("add")):
        print("contains value")
        appendValue = appendValue.replace("add ", "")

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
