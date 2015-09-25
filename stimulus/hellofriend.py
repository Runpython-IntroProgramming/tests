import random

random.seed()
name = random.choice(['Tom', 'Sue', 'Rob', 'Rebecca', 'William', 'Emma'])
age = random.randint(10,18)
print("{}\n{}\n".format(name, age))
