#import Dependencies

import os
import csv
from os import path
#import csv into a path
bank_csvpath = os.path.join("Resources", "budget_data.csv")

#open and read csv
with open (bank_csvpath) as budget_file:
    csv_reader = csv.reader(budget_file, delimiter = ",")

    # Read the header row first
    csv_header = next(csv_reader)
    print(f"Header:{ csv_header}")

#read the header row first, then read through each row of the file
    csv_header2 = next(csv_reader)
    result = [row for row in csv_reader]
    list_month = []
    for i, header_name in enumerate(result):
        list_month.append(header_name[0])
    print("Total months = " + str(len(list_month)))

#Get the total number of months included in the dataset
    
    result = [row for row in csv_reader]
    prof_loss = ['Profit/Losses'[i]]
    total = 0
    for i in range(0, len(result)):
        prof_loss.append('Profit/Losses'[i])
        #Iterate each element in list
# and add them in variable total
        total = total + prof_loss[i]
    print("Total Profit = " + str(total))
 
# printing total value

    


# Bank_budget = ["budget_file"]
# print (len(budget_file))



