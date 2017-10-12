import os
import csv
import collections

#set path to pyboss data
election = os.path.join("election_data_2.csv")

#create variables
totalvotes = 0
candidates = []
votedict = {}

#open csv
with open(election, newline="") as csvfile:
    next(csvfile, None)
    csvreader = csv.reader(csvfile,delimiter=",")

#find the total number of votes cast
    for row in csvreader:
        row += 1
        print(row)

#create a dictionary that extracts all the candidates  
#reader = csv.reader(open(election))
#for row in reader:
 #       key = row[2]
  #      if key in votedict:
   #         pass
    #    votedict[key] = row[0]
     #   print(votedict)
    

#find the total number of votes cast
#create dictionary for voters

#find how many votes each candidate has in loop

#find the percentage of votes each candidate won by dividing candidate votes by 