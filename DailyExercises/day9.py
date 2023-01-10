"""
Exercise 1:
Create a program to check if the password is strong
1. at least 8 characters
2. at least 1 digit
3. at least 1 uppercase letter

Exercise 2:
Write a program that asks users to enter a password.
Then, it checks if the password length is greater than 7 and returns "Great password there!".
If the password has 7 or fewer characters, the program returns, "Your password is weak".


Exercise 3:
Extend the program we built in Coding Exercise 1 by adding a new feature.
The new feature should allow the program to return "Password is OK, but not
too strong" when the password is exactly seven characters long.
"""

def exercise1():
    condition1 = False
    condition2 = False
    condition3 = False
    password = input("please enter a password: ")

    if len(password) >= 8:
        condition1 = True
        for letter in password:
            if letter.isdigit():
                print(letter)
                condition2 = True

            if letter.isupper():
                print(letter)
                condition3 = True

    if condition1 and condition2 and condition3:
        print("the password is strong!")
    else:
        print("sorry the password is not strong!")


def exercise2():
    password = input("please enter a password: ")
    if len(password) >= 7:
        print("the password is strong")
    else:
        print("the password is weak")


def exercise3():
    password = input("please enter a password: ")
    if len(password) > 7:
        print("the password is strong")
    elif len(password == 7):
        print("the password is OK")
    else:
        print("the password is weak")

# exercise1()
exercise2()
exercise3()
