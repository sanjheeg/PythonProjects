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

            #addedTask = str(len(taskList) + 1) + ". " + addedTask + "\n"
            addedTask = addedTask + "\n"
            taskList.append(addedTask)

    else:
        #appendValue = str(len(taskList) + 1) + ". " + taskName + "\n"
        appendValue = taskName + "\n"
        taskList.append(appendValue)


def showTask():
    if (len(taskList) == 0):
        print('your list is empty! Use "add" to add to it')
    else:
        for index, item in enumerate(taskList):
            strippedItem = item.strip("\n")
            #print(strippedItem)
            print(str(index + 1) + ". " + strippedItem)


def completeTask(task):
    taskNum = int(task.split()[1]) - 1
    #del taskList[taskNum]
    taskList.pop(taskNum)

    showTask()


def editTask():
    showTask()
    taskIndex = int(input("which task number would you like to edit? ")) - 1
    newTask = input("please enter new task: ")
    #taskList[taskIndex] = str(taskIndex + 1) + ". " + newTask + "\n"
    taskList[taskIndex] = newTask + "\n"

    
# start of main
print("Welcome to the todo app!")

task = ""
taskList =[]

print("type 'exit' to exit\nif you would like to add multiple to-do's, simply enter 'add'")

while (True):
    with open("data.txt", "r") as file:
        taskList = file.readlines()

    task = input("enter a task: add, show, complete, edit, or exit: ")

    if (task.__contains__("add")):
        addTask(task, taskList)
    elif (task.__contains__("exit")):
        break
    elif (task.__contains__("show")):
        showTask()
    elif (task.__contains__("complete")):
        completeTask(task)
    elif (task.__contains__("edit")):
        editTask()
    elif (task.__contains__("exit")):
        print("thank you for using the to-do list app!")
        break
    else:
        print("your input was invalid, please try again.")

    i = 0
    while ( i < len(taskList)):
        if len(taskList[i]) == 1:
            del taskList[i]
        i+=1

    print(taskList)
    with open("data.txt", "w") as file:
        for item in taskList:
            file.writelines(item)
