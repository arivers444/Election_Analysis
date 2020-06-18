# Add our dependencies.
import csv
import os

# Assign a variable to load a file from path.
file_to_load = os.path.join("Resources/election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Initialize candidate list.
candidate_options = []

# Declare empty dictionary.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count by setting to zero.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the candidate list.
for candidate in candidate_votes:

    # Retrieve vote count of a candidate.
    votes = candidate_votes[candidate]

    # Calculate the percentage of votes.
    vote_percentage = int(votes) / int(total_votes) * 100

    # Print each candidate's name, vote count, and percentage of votes.
    print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")


    # Determine winning vote count and candidate
    # Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):

        # If True then set winning_count = votes and winning_percent = vote percentage
        winning_count = votes
        winning_percentage = vote_percentage

        # Set the winning_candidate equal to candidate's name.
        winning_candidate = candidate

# Print the Winning Candidate Summary
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)



# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A couplete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote
