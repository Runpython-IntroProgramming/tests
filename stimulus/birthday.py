# stimulus for birthday quiz
import random
from datetime import datetime
from calendar import month_name

trials = 10
random.seed()
trialversion = random.randint(1,3) # pick one of three...
name = random.choice(['Tom', 'Sue', 'Rob', 'Rebecca', 'William', 'Emma'])
year = random.randint(1970, 2014)
if trialversion == 1:
  date = 31
  month = 'October'
elif trialversion == 2:
  date = datetime.today().day
  month = month_name[datetime.today().month]
else:
  month = random.choice(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
  date = random.randint(1,31)
print("{}\n{}\n{}\n{}\n".format(name, month, year, date))
