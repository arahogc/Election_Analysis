#Data needed to retrieve 
#1. The total number of votes cast
#2. A complete list of candidates who received votes 
#3. The precentage of votes each candidate won 
#4. The total number of votes each candidate won 
#5. The winner of the election based on popular vote. 

#Add dependencies 
import csv 
import os

#Assign a variabe to load a file from a path 
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1 Initialize a total vote counter 
total_votes = 0 
#Candidate options and candidate votes 
candidate_options = []
#1. Declare the empty dictionary 
candidate_votes = {}
#Winning candidate and winning count tracker 
winning_candidate = " "
winning_count = 0 
winning_percentage = 0 
#Open the election results and read the file
with open(file_to_load) as election_data: 
    file_reader = csv.reader(election_data)
    
    #read the header row 
    headers = next(file_reader)
    #Print each row in the CSV File 
    for row in file_reader: 
        #2. Add to the total vote count. 
        total_votes +=1 
        #Print the candidate name from each row 
        candidate_name = row[2]
        #If the candidate does not match any existing candidate
        if candidate_name not in candidate_options: 
            #Add it to the list of candidates 
            candidate_options.append(candidate_name)
            #Begin tracking that candidates's vote count 
            candidate_votes[candidate_name] =0 
         #Add a vote for each candidate 
        candidate_votes[candidate_name] += 1
    #Determine the percentage of votes for each candidate by looping through the counts
    #Iterate through the candidate list 
    for candidate_name in candidate_votes: 
        #Retrieve vote count of a candidate 
        votes = candidate_votes[candidate_name]
        #Calculate the percentage of votes 
        voter_percentage = float(votes) / float(total_votes) * 100 
        rounded_vote = round(voter_percentage, 1)
        #Deterimine winning vote count and candidate 
        #Determine if the votes are greater than the winning count 
        #To do: print each candidate's name, vote count and percentage of vote to the terminal
        print(f"{candidate_name}: {voter_percentage:.1f}% ({votes:,})\n")
        if (votes > winning_count) and (voter_percentage > winning_percentage): 
            #IF the true then set winning_count = votes and winning percent = voter_percentage
            winning_count = votes
            winning_percentage = voter_percentage 
            #Set the winning_candidate equal to the candidate's name 
            winning_candidate = candidate_name
    winning_candidate_summary = ( 
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winniing Vote Counte: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n" 
        f"-------------------------\n")

    print(winning_candidate_summary)



