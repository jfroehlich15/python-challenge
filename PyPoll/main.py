#import modules
import os
import csv

#create path
pypoll_csv = os.path.join("Resources", "election_data.csv")

print(pypoll_csv)
print("")


with open(pypoll_csv) as csvfile:
     # specify delimiter
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip header row
    csvheader = next(csvreader)

    #assign total votes variable
    totalvotes = 0

    #assign variables to each candidate
    Charles = 0
    Diana = 0
    Raymon = 0

    for row in csvreader:

        #add 1 to total votes for each row
        totalvotes += 1

        #add 1 to charles if voted for
        if row[2] == "Charles Casper Stockham":
            Charles += 1

        #add 1 to diana if voted for
        if row[2] == "Diana DeGette":
            Diana += 1

        #add 1 to raymon if voted for
        if row[2] == "Raymon Anthony Doane":
            Raymon += 1

    
    #calculate percentage of vote for each candidate
    charles_percent = round(((Charles / totalvotes) * 100), 3)
    diana_percent = round(((Diana / totalvotes) * 100), 3)
    raymon_percent = round(((Raymon / totalvotes) * 100), 3)


    #if statements to compare candidate variables and determine winner
    if Charles > Raymon and Charles > Diana:
        winner = "Charles Casper Stockham"

    elif Diana > Raymon and Diana > Charles:
        winner = "Diana DeGette"

    else:
        winner = "Raymon Anthony Doane"




#print analysis

print("Election Results")
print("")
print("----------------------------------")
print("")
print("Total Votes: " + str(totalvotes))
print("")
print("----------------------------------")
print("Charles Casper Stockham: " + str(charles_percent)+ "%" + " " + "(" +str(Charles) + ")")
print("")
print("Diana DeGette: " + str(diana_percent)+ "%" + " " + "(" +str(Diana) + ")")
print("")
print("Raymon Anthony Doane: " + str(raymon_percent)+ "%" + " " + "(" +str(Raymon) + ")")
print("")
print("----------------------------------")
print("")
print("Winner: " + winner)
print("")
print("----------------------------------")


#output file

#create output file path
output_file = os.path.join("Analysis", "PyPoll_final.csv")

#write output text file
with open(output_file, "w", encoding='utf-8') as datafile:
    writer = csv.writer(datafile)

    #write rows
    writer.writerow(["Election Results"])
    writer.writerow(["Total Votes: " + str(totalvotes)])
    writer.writerow(["Charles Casper Stockham: " + str(charles_percent)+ "%" + " " + "(" +str(Charles) + ")"])
    writer.writerow(["Diana DeGette: " + str(diana_percent)+ "%" + " " + "(" +str(Diana) + ")"])
    writer.writerow(["Raymon Anthony Doane: " + str(raymon_percent)+ "%" + " " + "(" +str(Raymon) + ")"])
    writer.writerow(["Winner: " + winner])


