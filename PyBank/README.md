PYBANK FINANCIAL ANALYSIS

This is a Simple Financial Analysis Python Script to analyze PyBank.

First import the dependencies: os, csv, path from os.

Next import the budget_data.csv file into an ospath.

Then open the csv file to a reader and read in the header line.

Next set up lists: 
    Profit/Losses as prof_loss
    Monthly changes as changes

and Then set up variables prev as p; and next as n

Next using a for loop, populate the prof_loss and changes lists as the loop iterates through the rows.

Then Calculate:
    Total Profit / Loss for the period using the sum function on the list prof_loss
    Average change by dividing changes by the length of prof_loss
    Greatest increase by using max(changes)
    Greatst decreast by using min(changes)

Then print them all out under the header "Financial Analysis", using fstrings to print out the numbers as strings.

