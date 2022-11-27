<!-- -- # Analysis of Election Data in PyPoll.

RESULT:

The winner is Diana DeGette with 74 % of total votes or 272,892 votes.

First I set up the Challenge by importing dependencies.
    os, from os import path, import csv

THEN I set up my CONSTANTS.
    ELECTIONS_CSV_PATH = os.path.join("Resources" , "election_data.csv")
    CANDIDATE_INDEX = 2

THEN I made sure the file could be accessed from anywhere a terminal is opened.
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

THEN I set up the Path to open and read the elections csv data file, and read past and print out the header line.

with open(ELECTIONS_CSV_PATH) as elections_file:
    csv_reader = csv.reader(elections_file, delimiter = ",")

    # Read the header row first
    csv_header = next(csv_reader)
    print(f"Header:{ csv_header}

# set up an empty dictionary to gather the candidate names and the votes they receive, 
# and set the total votes value at 0.

    votes_per_candidate = {}
    total_votes = 0

# then read through each row of the file with a for loop with if/else to count the total votes, 
# tally the candidate names, and count the votes each candidate receives.

    for row in csv_reader:
        total_votes += 1
        candidate_name = row[CANDIDATE_INDEX]
        if candidate_name in votes_per_candidate:
            votes_per_candidate[candidate_name] += 1
        else:
            votes_per_candidate[candidate_name] = 1

# Using another for loop through the votes_per_candidate dictionary to get the final tally, and the percentage of votes each candidate has.

for key, votes  in votes_per_candidate.items():
        percentage = round((int(votes)/int(total_votes) * 100))
        finals = (key, percentage, votes)
        print(finals)
        print("-------------------------------------------------")

#Then I defined a function to call the winner of the election and print it. 

        x = int(votes_per_candidate["Charles Casper Stockham"])
        y = int(votes_per_candidate["Diana DeGette"])
        z = int(votes_per_candidate["Raymon Anthony Doane"])

#THen defined a function to call the winner       
    def winner():
        if x > y and x > z:
            print("The winner is Charles Casper Stockham")
        elif y > x and y > z:
            print("The winner is Diana DeGette")
        else:
            print("The winner is Raymon Anthony Doane")
winner()    

#END -->