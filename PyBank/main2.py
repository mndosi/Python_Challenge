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
    prof_loss = []
    changes = []
    p = 0
    n = 0
    for row in csv_reader:
        prof_loss.append(int(row[1]))
        n = int(row[1])
        changes.append(n-p)
        p = int(row[1])
    Total = sum(prof_loss)
    changes = changes[1:]
    average = sum(changes) / len(changes)
    greatest_increase = max(changes)
    greatest_decrease = min(changes)


print("Financial Analysis")        
print("-------------------------------------------------")
print(f"Total months = {len(prof_loss)}")
print(f"Total Profit =  ${Total}")
print(f"Average Change = ${average}")
print(f"Greatest Increase = ${greatest_increase}")
print(f"Greatest Decrease = ${greatest_decrease}")





