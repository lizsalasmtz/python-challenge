import os
import csv
import pandas as pd

# path of current python file
curr_dir = os.path.dirname(os.path.realpath(__file__))

# path to collect data from the resources folder 
election_csv = os.path.join(curr_dir, "Resources", "election_data.csv")

# create a pandas dataframe with election data
df = pd.read_csv(election_csv) 
# df.head()

# the total number of votes cast
votes_count = df["Voter ID"].count()
#print(votes_count)

# create a dataframe summary of the candidates who received votes
candidate_grouped_df = df.groupby("Candidate")["Candidate"]

# the total number of votes each candidate won
candidate_grouped_df = candidate_grouped_df.count().to_frame("Votes")

# the percentage of votes each candidate won
candidate_grouped_df["Percent"] = (100 * candidate_grouped_df["Votes"] / votes_count).round(2).astype(str) + "%"    

# sort ascending
candidate2_df = candidate_grouped_df.sort_values(["Votes"], ascending=False) 
# candidate2_df.head()

winner = candidate_grouped_df["Votes"].idxmax()

# create a string of the election result summary
summary = "Election Results\n" + "------------------------\nTotal Votes: " + str(votes_count) + "\n" + "------------------------\n" + str(candidate2_df) + "\n" + "-------------------------\n" + "Winner:" + str(winner) + "\n" + "-------------------------"

# set the location of the output file
outfile = os.path.join(curr_dir, "Analysis", "election_analysis.txt")

# write the output file
with open(outfile, 'w') as file:
    file.write(summary)

print(summary)