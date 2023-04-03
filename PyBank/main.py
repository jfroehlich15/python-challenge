#import modules
import os
import csv

#create path
pybank_csv = os.path.join("Resources", "budget_data.csv")

print(pybank_csv)


#lists to store data

all_volumes = []
changes = []
months = []


with open(pybank_csv) as csvfile:
     # specify delimiter
    csvreader = csv.reader(csvfile, delimiter=',')
    #skip header row
    csvheader = next(csvreader)

    #create variable to count months in the budget sheet
    totalmonths = 0

    #create variable to count the total of each row
    totalvolume = 0


    for row in csvreader:
        
        #add each month to months list
        months.append(row[0])

        #add one to total months for each row
        totalmonths += 1

        #add each value in column 2 to the total volume
        totalvolume += int(row[1])

        #Add volumes to all volumes list to calculate for changes
        all_volumes.append(int(row[1]))



    #loop to track each change in volume
    for x1, x2 in zip(all_volumes[:-1], all_volumes[1:]):

        #subtract new change from old change and append to changes list
        change = x2 - x1
        changes.append(change)
     
        #calculate average change
        average_change = sum(changes) / (totalmonths - 1)

        #find max and min values in changes list
        increase = max(changes)
        decrease = min(changes)

        #call month for max
        month_increase = changes.index(increase)
        greatest_month = months[month_increase + 1]

        #call month for min
        month_decrease = changes.index(decrease)
        worst_month = months[month_decrease + 1]

    #print analysis


    print("Financial Analysis")
    print("")
    print("----------------------------------")
    print("")
    print("Total Months: " + str(totalmonths))
    print("")
    print("Total: $" + str(totalvolume))
    print("")
    print("Average Change: $" + str(round(average_change, 2)))
    print("")
    print("Greast Increase in Profits: " + str(greatest_month) + " ($" + str(increase) + ")")
    print("")
    print("Greast Decrease in Profits: " + str(worst_month) + " ($" + str(decrease) + ")")

#create output file path
output_file = os.path.join("Analysis", "PyBank_final.csv")

#write output text file
with open(output_file, "w", encoding='utf-8') as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Financial Analysis"])
    writer.writerow(["Total Months: " + str(totalmonths)])
    writer.writerow(["Total: $" + str(totalvolume)])
    writer.writerow(["Average Change: $" + str(round(average_change, 2))])
    writer.writerow(["Greast Increase in Profits: " + str(greatest_month) + " ($" + str(increase) + ")"])
    writer.writerow(["Greast Decrease in Profits: " + str(worst_month) + " ($" + str(decrease) + ")"])


  


    


