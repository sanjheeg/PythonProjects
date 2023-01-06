"""
Exercise 1:
names = ["john smith", "jay santi", "eva kuki"]
Extend the code above so the code capitalizes all the names and the surnames of the list
and then prints the new list.

Exercise 2:
usernames = ["john 1990", "alberta1970", "magnola2000"]
Extend the code above so the code prints out a list containing the number of characters for each username.

Exercise 3:
user_entries = ['10', '19.1', '20']
Extend the code above so the code prints out a list containing the same items as floats.

Exercise 4:
user_entries = ['10', '19.1', '20']
Extend the code above so the code prints out the sum of the numbers.
"""

def exercise1():
    namesOld = ["john smith", "jay santi", "eva kuki"]
    namesNew = [names.title() for names in namesOld]
    print(namesNew)


def exercise2():
    usernames = ["john 1990", "alberta1970", "magnola2000"]
    charNum = [len(name) for name in usernames]
    print(charNum)


def exercise3():
    user_entries = ['10', '19.1', '20']
    floatEntries = [float(num) for num in user_entries]
    print(floatEntries)


def exercise4():
    user_entries = ['10', '19.1', '20']
    sum = 0
    floatEntries = [float(num) for num in user_entries]
    for item in floatEntries:
        sum += item
    print(sum)


exercise1()
exercise2()
exercise3()
exercise4()
