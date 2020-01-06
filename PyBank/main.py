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
past_rev = 0
highest_increase = 0
lowest_increase = 0

# Create lists to track Revenue Change
rev_change = []

# Creat file path
csvpath = ('budget_data.csv')

#print(budget_csvpath) - Sanity Check

#Open and Reading CSV File
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(budget_csvreader)
    next(csvreader, None)
    for row in csvreader:
        # Count total months
        total_months = total_months + 1
        
        # Sum total revenue in file
        total_rev = total_rev + (int(row[1]))
        
        # Make new variable for revenue changes
        
        monthly_rev_change = int(row[1]) - past_rev
        past_rev = int(row[1])

        # Create a new list and append to it
        rev_change.append(monthly_rev_change)

        #Calculate average change in revenue
        avg_rev_change = round(sum(rev_change) / total_months)
        
        # print(avg_rev_change) 

        # Find the greatest increase in revenue month over month
        if (monthly_rev_change > highest_increase):
            highest_inc_month = row[0]
            highest_inc_rev = monthly_rev_change 

        # Find the greatest decrease in revenue month over month
        if (monthly_rev_change < lowest_increase):
            lowest_dec_month = row[0]
            lowest_dec_rev = monthly_rev_change

# Print your results \n is new line break

Results = (
f"     Financial Analysis \n"
f"---------------------------- \n"
f"Total Months: {total_months} \n"
f"Total Revenue: ${total_rev} \n"
f"Average Revenue Change: ${avg_rev_change} \n"
f"Greatest Increase in Revenue: {highest_increase} (${highest_inc_rev}) \n"
f"Greatest Decrease in Revenue: {lowest_increase} (${lowest_dec_rev}) \n")
print(Results)

#Write to a text file
outputtxt = ('Analysis.txt')
with open(outputtxt, 'w') as txtfile:
    txtwriter = txtfile.write(Results)