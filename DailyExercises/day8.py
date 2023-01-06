"""
A client wants to buy a coin-flip probability program from you.

The programs should work like this:
1. The user runs the program. The program asks the user to enter "head" or "tail".
The user flips a coin on their desk, table, floor, etc., and then enters "head" or "tail".
The user does the same over and over again.
"""


def exercise1():
    with open("headsTails.txt", "r") as file:
        headsTails = file.readlines()
    totalHeads = 0
    percentage = 0

    while True:
        play = input("please enter heads or tails: ")
        headsTails.append(play + "\n")

        totalHeads = headsTails.count("heads\n")
        numofvalues = len(headsTails)
        percentage = float(totalHeads / numofvalues) * 100
        print(f"percentage is: {percentage}%")

        if play == "exit":
            break

    with open("headsTails.txt", "w") as file:
        file.writelines(headsTails)


exercise1()
