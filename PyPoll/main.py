import os
import csv

# create path where csv data file is found
election_path = os.path.join("Resources","election_data.csv")

# declare variabes & key-paired dictionary

# create a dictionary with candidate name as a key, and number of votes as element
candidate = {}

# declare variables
search_can = " "        # represents candidate name used for tabulating votes
num_votes = 0           # the total number of votes
percent_vote = 0.000    # percentage of the popular vote for each candidate
winner_count = 0        # is the winning number of votes
winner = " "            # is the name of the winner candidate
output_hdr = []         # list of output to screen and txt file of header info
output_ftr = []         # list of output to screen and txt file of footer info

  
# open csv data file budget_data.csv
with open (election_path) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next (csvreader)
            
    # go through each row in csv data file
    for row in csvreader:
        
        # summing the total number of votes
        num_votes += 1
        search_can = row[2]


        # testing for unique candidate name &
        # storing it in the dictionary
        if not search_can in candidate:
            candidate[search_can] = 0
        
        # assigning vote to correct candidate
        candidate[search_can] += 1

    # store & print header info to screen
    output_hdr = ["Election Results",
                  "-------------------------",
                  "Total Votes:  "+str(num_votes),
                  "-------------------------"]
    print(" ")
    print(*output_hdr , sep ="\n")

    winner_count = max(candidate.values())
    
    # iterate through candidates and print summary stats
    for key in candidate.keys():
        
        # finding the winner of the election
        if candidate[key] == winner_count:
            winner = key
        
        # calculate percentage of votes
        percent_vote = round((candidate[key]/num_votes)*100,3)

        print(f"{key}: {percent_vote}% ({candidate[key]})")
        
    # store & print footer info to screen
    output_ftr = ["-------------------------", 
                 "Winner:  " + winner,
                 "-------------------------" ]
    print(*output_ftr , sep ="\n")
    

    # create output.txt file in \analysis directory for election results
    with open ('analysis\output.txt', 'w') as outpt:
        
        # write header info to ..\analysis\output.txt file
        for line in output_hdr:
            outpt.write(line)
            outpt.write('\n')

        # write summary candidate stats to ..\analysis\output.txt file
        for key in candidate.keys():
            percent_vote = round((candidate[key]/num_votes)*100,3)

            outpt.write((key) +": " +str(percent_vote)+"% (" + str(candidate[key])+ ")")
            outpt.write('\n')

        # write footer info to ..\analysis\output.txt file
        for line in output_ftr:
            outpt.write(line)
            outpt.write('\n')


            