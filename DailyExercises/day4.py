"""
Exercise 1:
1. Prompts the user to input a (dollar) amount.
2. Calculates the corresponding amount in euros, given an exchange rate of 0.95.

Exercise 2:
ranking = ['John', 'Sen', 'Lisa']
Create a program that:
1. Contains the above list.
2. Prompts the user to input a rank number.
3. Returns the person who has the given rank.

Exercise 3:
This time you need to create a program that:
1. Contains the above list.
2 Prompts the user to input the person's name.
3. Returns the rank that person has.
"""

def exercise1():
    print(int(input("please enter $$: ")) * 0.95)


def exercise2():
    ranking = ['John', 'Sen', 'Lisa']
    print(ranking[int(input("please enter rank number: ")) - 1])


def exercise3():
    ranking = ['John', 'Sen', 'Lisa']
    print(int(ranking.index(input("please enter the name: "))) + 1)



exercise1()
exercise2()
exercise3()