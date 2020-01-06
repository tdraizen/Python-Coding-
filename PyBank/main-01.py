#  Your task is to create a Python script that analyzes the records to calculate each of the following:
#       1.	The total number of months included in the dataset
#       2.	The total net amount of "Profit/Losses" over the entire period
#       3.	The average change in "Profit/Losses" between months over the entire period
#       4.	The greatest increase in profits (date and amount) over the entire period
#       5.	The greatest decrease in losses (date and amount) over the entire period
#       6.  Data should look below once tabulated

  #Financial Analysis
  #----------------------------
  #Total Months: 86
  #Total: $38382578
  #Average  Change: $-2315.12
  #Greatest Increase in Profits: Feb-2012 ($1926159)
  #Greatest Decrease in Profits: Sep-2013 ($-2196167)
 
# Final Step Print to txt file



# Import Modules
import os
import csv

# Make Variables
total_months = 0
total_rev = 0
total_rev_change = 0

# Create lists to track Revenue Change
#rev_change = []

# Creat file path
csvpath = ('budget_data.csv')

#print(budget_csvpath) - Sanity Check

#Open and Reading CSV File
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(budget_csvreader)
    # Skip Header
    next(csvreader, None)

    calc = next(csvreader, None)
    max_month = calc[0]
    min_month = calc[0]
    revenue = float(calc[1])
    max_rev = revenue
    min_rev = revenue
    previous_rev = revenue
    total_month = 1
    total_rev = float(calc[1])
    total_rev_change = 0
    for calc in csvreader:
        # Count total months
        total_months = total_months + 1
        
        revenue = float(calc[1])

        # Sum total revenue in file
        total_rev = total_rev + revenue
        
        # Make new variable for revenue changes 
        
        revenue_change = revenue - previous_rev

        # Create a new list and append or add onto it
        total_rev_change = total_rev_change + revenue_change

        #Calculate the max and min 
        if revenue_change > max_rev:
            max_month = calc[0]
            max_rev = revenue_change
        
        if revenue_change < max_rev:
            min_month = calc[0]
            min_rev = revenue_change

        previous_rev = revenue
        
        # print(total_rev_change) 
# Finalize Data Set
average_revenue = total_rev_change / total_months
average_revenue_change = total_rev_change / (total_months - 1)

# Eliminate Strings to Int
total_rev = int(total_rev)
average_revenue_change = int(average_revenue_change)
max_rev = int(max_rev)
min_rev = int(min_rev) 
# Print your results \n is new line break

Results = (
f"Financial Results Analysis\n"
f"___________________________ \n"
f"Total Months: ${total_months} \n"
f"Total Revenue: ${total_rev} \n"
f"Average Revenue Change: ${average_revenue_change} \n"
f"Greatest Increase in Profits: {max_month} ${max_rev} \n"
f"Greatest Decrease in Profits: {min_month} ${min_rev} \n")
print(Results)

#Write to a text file
outputtxt = ('Analysis_Revised.txt')
with open(outputtxt, 'w') as txtfile:
    txtwriter = txtfile.write(Results)