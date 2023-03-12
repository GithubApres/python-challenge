import os
import csv

# create path where csv data file is found
budget_path = os.path.join("Resources","budget_data.csv")

  
# open csv data file budget_data.csv
with open (budget_path) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    
    header = next (csvreader)       # successfully stores header row

    num_months = 0      # number of months in the dataset
    total_PL = 0        # the net total amount of "Profit/Losses"over entire period
    max_PL = 0          # the greatest increase in profits over entire period
    min_PL = 0          # the greatest decrease in profits over entire period

    # go through each row in csv data file
    for row in csvreader:
        
        num_months += 1
        total_PL += int(row[1]  )

        # track minimum amount
        if ( int(row[1]) <= min_PL ):
            min_PL = int(row[1])
            min_month = row[0]
        
        # track maximum amount
        if ( int(row[1]) >= max_PL ):
            max_PL = int(row[1])
            max_month = row[0]
        
    # save printout to output list
    output = ["Financial Analysis",
            "-----------------------------",
            "Total Months: "+ str(num_months),
            "Total: $"+ str(total_PL),
            "Average Change: $"+ str(total_PL/num_months),
            "Greatest Increase in Profits: "+ str(max_month) + " $ "+ str(max_PL),
            "Greatest Decrease in Profits: "+ str(min_month) + " $"+ str(min_PL) ]
    
    # print to screen
    print (" ")
    print(*output , sep ="\n")
    print (" ")
    
    # print to output.txt file
    with open ('analysis\output.txt', 'w' ) as f:
        for line in output:
            f.write(line)
            f.write('\n')