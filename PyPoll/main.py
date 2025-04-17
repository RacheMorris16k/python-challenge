#import os module to create file paths
import os

#import module for reading csv files
import csv

import pandas as pd
df = pd.read_csv (r'C:\Users\rache\python-challenge-1\PyPoll\Resources\election_data.csv')

#Load the CSV File
file_path = os.path.join
"('C:''Users','rache','python-challenge-1',PyPoll','Resources','election_data.csv')"

#Total number of votes
total_votes = df.shape[0]
print(f"Total Votes: {total_votes}")

#Vote counts per candidate
candidates_counts = df['Candidate'].value_counts()

#List of all candidates who recieved votes
candidates = candidates_counts.index.tolist()

print("Candidates:",candidates)
print("\nVote counts:\n", candidates_counts)

#Calculate Vote Percentages
vote_percentages = (candidates_counts / total_votes) * 100

#Print results
for cand in candidates_counts.index:
    print(f"{cand}: {vote_percentages[cand]:.3f}% ({candidates_counts[cand]})")

#Determine the winner(candidate with the most votes)
winner = candidates_counts.idxmax()

print(f"Winner: {winner}")

#Output lines
lines = [
    "Election Results",
    "_________________________", 
    f"Total Votes: {total_votes}",
    "_________________________",
]
for cand in candidates_counts.index:
    lines.append(f"{cand}: {vote_percentages[cand]:.3f}% ({candidates_counts[cand]})")
    lines +=[
        "_______________________",
        f"Winner:{winner}",
        "________________________"
    ]

    #Write to text file
    out_path = os.path.join(r'C:\Users\rache\python-challenge-1\PyPoll\analysis', 'election_analysis.txt')
    os.makedirs(os.path.dirname(out_path),exist_ok=True)

    with open(out_path, 'w') as f:
        f.write('\n'.join(lines))

print(f"Results written to {out_path}")