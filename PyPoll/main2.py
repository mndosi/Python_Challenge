#set up the challenge
# import os module
#import module for reading csv files
#import path

from itertools import count
import os 
from os import path
import csv

elections_csv = os.path.join("Resources","election_data.csv")
with open (elections_csv) as elections_file:
    csv_reader = csv.reader(elections_file, delimiter = ",")

    # Read the header row first
    csv_header = next(csv_reader)
    print(f"Header:{ csv_header}")

    #read the header row first, then read through each row of the file
    ballots = []
    candidates = [row[2]]
    #votes_per_candidate = []
    for row in csv_reader:
        ballots.append(row[0])
        if row[2] != candidates:
            candidates.append((row[2]))
        
    
        
    total_votes = count(ballots - 1)
    percent_votes_c = [votes_per_c / total_votes]
    winner = max(votes_per_candidate)


print("Election Analysis")        
print("-------------------------------------------------")
print(f"Total votes = {[total_votes]}")
print("-------------------------------------------------")
print(f"({[candidates][i]}): ({[percent_votes_c][i]})%  ({([votes_per_c][i])})) /n
print("-------------------------------------------------")
print(f"Winner: )