"""
Exercise 1:
Create a program that does the following:
1. Prompts the user to input the country they are from.
2. If the user enters the word USA, the program prints out Hello.
3. If the user enters the word  India, the program prints out Namaste.
4. If the user enters the word Germany, the program prints out Hallo.


Exercise 2:
ingredients = ["john smith", "sen plakay", "dora ngacely"]
Copy-paste the above line into your IDE and write a for-loop below that line that
makes the program produce the first letter of each word capitalized.
"""

def exercise1():
    country = input("please enter what country you're from: ")
    match country:
        case "USA":
            print("Hello")
        case "India":
            print("Namaste")
        case "Germany":
            print("Hallo")


def exercise2():
    ingredients = ["john smith", "sen plakay", "dora ngacely"]
    for item in ingredients:
        print(item.title())


exercise1()
exercise2()
