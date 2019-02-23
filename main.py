# Import Modules Here
import os
import datetime
import calendar


# Cleansing of date feilds to generate
# a single digit to represent 
# the current month 
now = datetime.date.today().year                # Reutrns the full date time
month = datetime.datetime.now().strftime("%m")  # Strips the above down to current month as int. i.e. February is 02 
monthDigit = month.strip("0")                   # Strips the 0 from the above 2 digit month reference


# Set Parent Location
os.chdir(input("Where would you like to create the directories?: "))


# Nested For loops to generate directory structure and naming 
cardNums = ['Card_1', 'Card_2', 'Card_3']
for cardNum in cardNums:
        for f in range(1, 21, 1):
                batchNum = "Batch" + "_" + str(f)
                for d in range(1, 32, 1):
                        day = "Day" + "_" + str(d)
                        os.makedirs(os.path.join(calendar.month_name[int(monthDigit)] + "_" + str(now), str(day), cardNum, batchNum))