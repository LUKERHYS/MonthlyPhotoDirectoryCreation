#Import Modules Here
import os
import datetime
import calendar

#My Functions
##Pulling in current Month as a number
now = datetime.date.today().year
month = datetime.datetime.now().strftime("%m")
monthDigit = month.strip("0")


#Set Parent Location
os.chdir(input("Where would you like to create the directories?: "))


#Create Month Directory + Card Sub-Directories + Batch Sub-Directories
cardNums = ['Card_1', 'Card_2', 'Card_3']
for cardNum in cardNums:
    for f in range(1, 21, 1):
        batchNum = "Batch" + "_" + str(f)
        os.makedirs(os.path.join(calendar.month_name[int(monthDigit)] + "_" + str(now), cardNum, batchNum))

       
#/Users/lukerhys/Desktop/Test

#int(output), cardNum, batchNum
