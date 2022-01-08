#Data Needed
# 1. Total number of votes
# 2. List of all candidates who received votes
# 3. Percent of votes each candidate won
# 4. Total number of votes each candidate won
# 5. Winner of election based on popular vote

import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1. Initialize voter counter
total_votes = 0

#candidate options list
candidate_options = []

#candidates votes dictionary
candidate_votes = {}

#winning candidate and winning tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    #print each row in csv
    


    for row in file_reader:
        total_votes +=1

        #print candidates name for each row
        candidate_name = row[2]
        # if candidate does not match existing candidate
        if candidate_name not in candidate_options:
            #add candidate name to candidate list
            candidate_options.append(candidate_name)
            # track votes for each candidate
            candidate_votes[candidate_name] = 0
            #add votes to each candidates
        candidate_votes[candidate_name] = candidate_votes[candidate_name]+1





#determine percent of voters for each candidate

    for candidate_name in candidate_votes:
        #get vote count for each candidate
        votes = candidate_votes[candidate_name]
        #calculate percentage
        vote_percentage = float(votes) / float(total_votes) * 100
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        #determine winning vote count and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
        
        winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)






   







