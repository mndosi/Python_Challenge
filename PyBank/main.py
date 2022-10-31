
from logging import logProcesses
import os 
from os import path
import csv
bank_csvpath = os.path.join('Resources', 'budget_data.csv')
#C:\Users\MankweNdosi\ClassActivities\Python_Challenge\PyBank\Resources\budget_data.csv

#open and read csv
with open (bank_csvpath, 'r') as budget_file:
    csvreader = csv.reader(budget_file, delimiter = ",")
    #read the header row first, then read through each row of the file
    csv_headers = next(csvreader)
    result = [[list(c) for c in row] for row in csvreader]
    for i, header_name in enumerate(result)
        print (header_name, [row[i] for row in result])

row_count = len(result)
x = 0
net_total = []
def net_total(Profit/Losses)

for p_l in Profit/Losses
    net_total.append(net_total[x + (x+1)]

 # get total number of months
while x < row_count:
    x = 0
    total_months = row_count - 1 
    net_total += int(result[1,x])
    net_change = row[x - (x-1)]:
    avg_change = net_change / total_months
    max_increase = max.int(net_change)
    max_decrease = min.int(net_change)

print("Financial Analysis")
print("------------------------------------------------")
print("Total Months: ", total_months)
print("Total Change: ", net_Total)
print("Average Change: " ,avg_change)
print("Maximum increase in Profits: ", max_increase)
print("Maximum decrease in Profits: ", max_decrease)


file = '../Python_Challenge/PyBank/analysis.txt'


# alternate routes
# #set path for file
# csvpath = os.path.join('..', "Python_Challenge","PyBank","Resources",'budget_data.csv')
# with open(csvpath) as csvfile
#     csvreader = csv.reader(csvfile; delimeter=',')
#     print(csvreader)
# csv_header = next (csvreader)
# # Create variables
# x=1
# Total_Profit=(B,x).sum
# for months.count=(a,x).value<>""=TRUE
# x=x+1
# next x
# Else
# print ("`````text ")
# print ("Financial Analysis")
# print (--------------------------------)
# print ("Total Months: "(x-1))
# end




