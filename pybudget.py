import os
import csv

#set path to the file
financialdata= os.path.join("budget_data_1.csv")

#create variables
months = 0
rev = 0
totalrev = 0
maxrev = 0
lowrev = 0
lowmonth = None
highmonth = None

#open csv
with open(financialdata, newline="") as csvfile:
    next(csvfile, None)
    csvreader = csv.reader(csvfile,delimiter=",")
        
#find the total number of months in dataset
    for row in csvreader:
        months += 1

#count total amount of revenue generated
        rev += int(row[1])

#find the average change in revenue between months
        totalrev = rev / months

#find the greatest increase in revenue between data and months
        if int(row[1])>maxrev:
            maxrev = int(row[1])
            highmonth = row[0]
#find the greatest decrease in revenue betwen data and months
        if int(row[1])<lowrev:
            lowrev = int(row[1])
            lowmonth =row[0]

#export printed function as a txt file
output_path = os.path.join('pybankfinal.txt')

#write text file
with open(output_path,"w", newline="") as text_file:

    text_file.write("Financial Analysis")
    text_file.write("----------------------------")
    text_file.write("Total Months: " + str(months))
    text_file.write("Total Revenue:  $" + str(rev))
    text_file.write("Average Revenue Change:  $" + str(totalrev))
    text_file.write("Greatest Increase in Revenue: " + str(highmonth) + "$" +str(maxrev))
    text_file.write("Greatest Decrease in Revenue: " + str(lowmonth) +"$" + str(lowrev))
#print results
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(months))
print("Total Revenue:  $" + str(rev))
print("Average Revenue Change:  $" + str(totalrev))
print("Greatest Increase in Revenue:  $" + str(highmonth) + "$" +str(maxrev))
print("Greatest Decrease in Revenue:  $" + str(lowmonth) +"$" + str((lowrev))