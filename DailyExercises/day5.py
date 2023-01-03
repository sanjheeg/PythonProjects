"""
Exercise1:
filenames = ['document', 'report', 'presentation']
Copy-paste the above list in a .py file and extend the code, so it prints out the output below:
    0-Document.txt
    1-Report.txt
    2-Presentation.txt

Exercise2:
ips = ['100.122.133.105', '100.122.133.111']
Copy-paste the ips list in a .py file and extend the program so it:
1. Prompts the user to input an index (e.g, 0 or 1).
2. Returns the IP address that has that index.
"""

def exercise1():
    filenames = ['document', 'report', 'presentation']
    for index, item in enumerate(filenames):
        phrase = f"{index}-{item.title()}.txt"
        print(phrase)


def exercise2():
    ips = ['100.122.133.105', '100.122.133.111']
    print(ips[int(input("enter index: "))])

exercise1()
exercise2()