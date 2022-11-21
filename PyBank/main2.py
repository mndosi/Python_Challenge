#import Dependencies

import os
import csv
from os import path
#import csv into a path
bank_csvpath = os.path.join("..", "PyBank", "Resources", "budget_data.csv")
# path C:\Users\MankweNdosi\ClassActivities\Python_Challenge\PyBank\Resources\budget_data.csv
#open and read csv
with open (bank_csvpath, 'r') as budget_file:
    csv_reader = csv.reader(budget_file, delimiter = ",")

    # Read the header row first
    csv_header = next(budget_file)
    print(f"Header:{ csv_header}")

#read the header row first, then read through each row of the file
    # csv_header2 = next(csv_reader)
    # result = [csv_reader(c) for c in row] for row in csv_reader]
    # #for i, header_name in enumerate(result):
    #     #print (csv_header2, [row[i] for row in result])

#Get the total number of months included in the dataset
    x = 0
    Ttl_mon = [x]
    for row in csv_reader:
        if row([1] != ""):
        x = x+1
        else:
            print("Total months= " & ((Ttl_mon)-1))

# Bank_budget = ["budget_file"]
# print (len(budget_file))



