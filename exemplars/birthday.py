from datetime import datetime
todaydate = datetime.today().day
todaymonth = datetime.today().month
from calendar import month_name

name = input("Hello, what is your name? ")
month = input("Hi {0}, what was the name of the month you were born in? ".format(name))
year = int(input("And what year were you born in, {0}? ".format(name)))
date = int(input("And the day? "))

if month == "October" and date == 31:
    print ("You were born on Halloween!")
elif month == month_name[todaymonth] and todaydate == date:
    print("Happy birthday!")
else:
    decade = "Stone Age"
    if year >= 2000:
        decade = "two thousands"
    elif year >= 1990:
        decade = "nineties"
    elif year >= 1980:
        decade = "eighties"
    if month in ["January", "February", "December"]:
        season = "winter"
    elif month in ["March", "April", "May"]:
        season = "spring"
    elif month in ["June", "July", "August"]:
        season = "summer"
    else:
        season = "fall"
    print("{0}, you are a {1} baby of the {2}.".format(name, season, decade))
