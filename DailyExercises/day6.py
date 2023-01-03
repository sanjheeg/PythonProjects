"""
Exercise 1:
Please download the essay.txt file from the resources of this article.
Then, create a program that reads that file and prints out its text.
The first letter of each word in the output should be uppercase.

Exercise 2:
Write a program that reads the essay.txt file and returns the number of
characters contained in the file.

Exercise 3:
Please download the members.txt file from the resources of this article.
Then, create a program that, whenever executed, asks the user to enter a
new member in the command line. Then, the member is added to members.txt.

Exercise 4:
Create a program that generates multiple text files by iterating over the
filenames list. The text Hello should be written inside each generated text file.
Then, the member is added to members.txt.

Exercise 5:
Please download the three text files a.txt, b.txt, and c.txt from the resources.
Then, create a program that reads each text file and prints out the content of
each in the command line.
"""


def exercise1():
    dataFile = open("essays.txt", "r")
    lines = dataFile.read()
    linesList = lines.split()
    newList = []
    for item in linesList[:]:
        item = item.capitalize()
        newList.append(item)

    newList = " ".join(newList)
    print(newList)


def exercise2():
    dataFile = open("essays.txt", "r")
    lines = dataFile.read()
    print(len(lines))


def exercise3():
    readFile = open("members.txt", "r")
    users = readFile.readlines()
    writeFile = open("members.txt", "w")
    newName = input("add a new member: ")
    users.append(newName)

    writeFile.writelines(users)


def exercise4():
    filenames = ['doc.txt', 'report.txt', 'presentation.txt']
    for name in filenames:
        file = open(name, "w")
        file.write("hello")


def exercise5():
    fileNames = ["a.txt", "b.txt", "c.txt"]
    for name in fileNames:
        file = open(name, "r")
        line = file.read()
        print(line)



exercise1()
exercise2()
exercise3()
exercise4()
exercise5()

