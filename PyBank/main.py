#import modules
import os
import csv

#create path
pybank_csv = os.path.join("Resources", "budget_data.csv")

print(pybank_csv)
print("")



#set variables to store data in for loop

previous_value = 0
change = 0
total_changes = 0
greatest_increase = 0
greatest_decrease = 0



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
        
        #set beginning previous value to first row value
        if previous_value == 0:
            previous_value = int(row[1])

        #add one to total months for each row
        totalmonths += 1

        #add each value in column 2 to the total volume
        totalvolume += int(row[1])

        #calculate changes in values of column 2
        current_value = int(row[1])
        change = current_value - previous_value

        previous_value = int(row[1])

        total_changes += change

        #determine greatest increase/decrease and add months
        if change > greatest_increase:
            greatest_increase = change
            greatest_increase_month = row[0]

        if change < greatest_decrease:
            greatest_decrease = change
            greatest_decrease_month = row[0]


    #calculate average change

    average_change = total_changes / (totalmonths - 1)






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
print("Greast Increase in Profits: " + str(greatest_increase_month) + " ($" + str(greatest_increase) + ")")
print("")
print("Greast Decrease in Profits: " + str(greatest_decrease_month) + " ($" + str(greatest_decrease) + ")")

#create output file path
output_file = os.path.join("Analysis", "PyBank_final.csv")

#write output text file
with open(output_file, "w", encoding='utf-8') as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Financial Analysis"])
    writer.writerow(["Total Months: " + str(totalmonths)])
    writer.writerow(["Total: $" + str(totalvolume)])
    writer.writerow(["Average Change: $" + str(round(average_change, 2))])
    writer.writerow(["Greast Increase in Profits: " + str(greatest_increase_month) + " ($" + str(greatest_increase) + ")"])
    writer.writerow(["Greast Decrease in Profits: " + str(greatest_decrease_month) + " ($" + str(greatest_decrease) + ")"])


  


    


