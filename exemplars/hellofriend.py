import datetime

year = datetime.datetime.now().year

name = input("Please tell me your name: ")
age = int(input("Please tell me your age: "))
pythonage = year - 1991
print("Hello, {0}. Python is {1} years older than you are!".format(name, pythonage-age))
