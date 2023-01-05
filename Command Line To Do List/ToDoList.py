def addTask(task, taskList):
    extraValue = task.split(" ")[0]
    taskName = task.replace(extraValue, "")

    taskName = taskName.replace("add ", "")

    if (taskName == ""):
        print("type 'exit' if you'd like to exit")
        while (taskName == ""):
            addedTask = input("please enter todo item: ")

            if(addedTask.__contains__("exit")):
                break

            addedTask = str(len(taskList) + 1) + " " + addedTask
            taskList.append(addedTask)

    else:
        appendValue = str(len(taskList) + 1) + " " + taskName
        taskList.append(appendValue)

    #adds item in own line
    with open("data.txt", "w") as file:
        for item in taskList:
            todos = file.writelines(item + "\n")


def showTask():
    if (len(taskList) == 0):
        print('your list is empty! Use "add" to add to it')
    else:
        for item in taskList:
            strippedItem = item.strip("\n")
            print(strippedItem)


def completeTask(task):
    taskNum = task.split()[1] - 1
    del taskList[taskNum]

    for item in taskList:
        print(item)
        
    file.close()


#start of main

print("Welcome to the todo app!")

task = ""
taskList =[]

print("type 'exit' to exit\nif you would like to add multiple to-do's, simply enter 'add'")

while (True):
    task = input("enter a task: add, show, complete, or exit: ")
    
    with open("data.txt", "r") as file:
        taskList = file.readlines()
    
    file.close()

    if (task.__contains__("add")):
        addTask(task, taskList)
    if (task.__contains__("exit")):
        break
    if(task.__contains__("show")):
        showTask()
    if(task.__contains__("complete")):
        completeTask(task)
    if(task.__contains__("exit")):
        print("thank you for using the to-do list app!")
        break
