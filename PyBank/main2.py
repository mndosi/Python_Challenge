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
    csv_header2 = next(csv_reader)
    result = [row for row in csv_reader]
    list_month = []
    for i, header_name in enumerate(result):
        #print([row[i] for row in result])
        #print(header_name)
        list_month.append(header_name[0])
    print("Total months= " + str(len(list_month)))

#Get the total number of months included in the dataset

    list_profloss = []
    for i, header_name in enumerate(result):
        list_profloss.append(header_name[1])
        def total_prof(list_profloss):
            final_prof = sum(list_profloss)
            return total_prof
    print("Total profit for the period was " + (final_prof.str))


# Bank_budget = ["budget_file"]
# print (len(budget_file))



