# stimulus for birthday quiz
import random

trials = 10
random.seed()
halloweentrial = random.randint(0, 8)
birthdaytrial = halloweentrial+1
name = random.choice(['Tom', 'Sue', 'Rob', 'Rebecca', 'William', 'Emma'])month = random.choice(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
year = random.randint(1970, 2014)
date = random.randint(1,31)
print("{}\n{}\n".format(name, age))
