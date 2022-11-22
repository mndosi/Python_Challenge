#set up the challenge
# import os module
#import module for reading csv files
#import path
from itertools import count
import os 
from os import path
import csv

elections_csv = os.path.join("Resources","election_data.csv")
def votes_tally(i, ballot_ID, Candidates):

    ballot_ID = (int(elections_csv[0]))
    Candidates = [str(elections_csv[2])]
    globaltotal_votes = (len(ballot_ID) - 1)
    cand_names = []
    Votes = {"Charles Casper Stockham": int(a)}
    percent_votes = Votes / total_votes
    winner = max([Votes])

with open(elections_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    print(count("Candidates"))

a = 0
for cand_name in "Candidates":
    if cand_name =="Charles Casper Stockham":
        Votes = {"Charles Casper Stockham":(a=(a+1))}
        elif cand_name != "Charles Casper Stockham"
        Votes.append(cand_name: (a=a+1))
        elif cand_name == ""
        break

    print ("Election Results")
    print ("------------------------------------------")
    print ("Total Votes: ", globaltotal_votes)
    print (Votes [0] + percent_votes[0])
    print (Votes[1] + percent_votes[1])
    print (Votes[2] + percente_votes[2])
    print ("The Winner is " = winner)

file = '../Python_Challenge/PyPoll/analysis.txt'






