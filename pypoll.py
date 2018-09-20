import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources','election_data.csv')

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    total_vote_count = 0
    votes_won = 0
    candidates = ['Khan','Correy','Li',]
    # set varaible for cand
    candidate_index = csvreader[2]

    for vote in csvreader:
        total_vote_count += 1
        current_candidate = vote[2]
        #if candidate is already in there list, add vote to total
        if current_candidate in candidates:
            candidate_index = candidates.index(current_candidate)
            votes_won[candidate_index] += 1
        #if they are not give them a vote 
        else:
            candidates.append(current_candidate)
            votes_won.append(1)
        