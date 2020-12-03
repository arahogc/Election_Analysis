
import csv 
import os

file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

total_votes = 0 

candidate_options = []
candidate_votes = {}
winning_candidate = " "
winning_count = 0 
winning_percentage = 0 

county_options = []
county_votes = {}
largest_county_turnout = " "
largest_vote = 0

with open(file_to_load) as election_data: 
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    for row in file_reader: 
        total_votes +=1 
        candidate_name = row[2]

        if candidate_name not in candidate_options: 
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] =0 
        candidate_votes[candidate_name] += 1

        county_name = row[1]

        if county_name not in county_options: 
            county_options.append(county_name)
            county_votes[county_name] = 0 
        county_votes[county_name] += 1

with open(file_to_save, "w") as txt_file: 
    election_results = ( 
        f"\nElection Results\n"
        f"----------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"----------------------\n")
    print(election_results, end= " ")
    txt_file.write(election_results)

    for county_name in county_votes: 
        c_votes = county_votes[county_name]
        county_percentage = float(c_votes) / float(total_votes) * 100 
        county_results = (
            f"\n County Votes: \n"
            f"{county_name}: {county_percentage:.1f}$ ({c_votes:,})\n")
        print(county_results)
        txt_file.write(county_results)
        
        if (c_votes > largest_vote): 
            largest_vote = c_votes 
            largest_county_turnout = county_name 
            county_summary =( 
                f"\n------------------\n"
                f"Largest County Turnout: {largest_county_turnout}\n"
                f"------------------\n")
    print(county_summary)
    txt_file.write(county_summary)

    for candidate_name in candidate_votes: 
        votes = candidate_votes[candidate_name]
        voter_percentage = float(votes) / float(total_votes) * 100 
        candidate_results = (
            f"{candidate_name}: {voter_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)

        if (votes > winning_count) and (voter_percentage > winning_percentage): 
            winning_count = votes
            winning_percentage = voter_percentage 
            winning_candidate = candidate_name
            winning_candidate_summary =( 
                f"----------------------\n"
                f"Winner: {winning_candidate}\n"
                f"Winniing Vote Count: {winning_count:,}\n"
                f"Winning Percentage: {winning_percentage:.1f}%\n" 
                f"----------------------\n")
            
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)



