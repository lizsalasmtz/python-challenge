import os
import csv
import pandas as pd

# path to collect date from the resources folder
curr_dir = os.path.dirname(os.path.realpath(__file__))

# path to budget csv file
budget_csv = os.path.join(curr_dir, "Resources", "budget_data.csv")

# create a pandas dataframe   
df = pd.read_csv(budget_csv) 

# the total number of months included in the dataset
month_count = df["Date"].count()

# the net total amount of profit/losses over the entire period
net_profit = df["Profit/Losses"].sum()

# the average of the changes in profit/losses over the entire period
df_chg = df.set_index("Date").diff()
avg_change = round(df_chg["Profit/Losses"].mean(), 2)

# the greatest increase in profits (date and amount) over the entire period
max_change = df_chg["Profit/Losses"].max()
max_change_date = df_chg["Profit/Losses"].idxmax()

# the greatest decrease in losses (date and amount) over the entire period
min_change = df_chg["Profit/Losses"].min()
min_change_date = df_chg["Profit/Losses"].idxmin()

# generate a summary string
summary = "Financial Analysis\n" + "----------------------------\nTotal Months: " + str(month_count) + "\nTotal: $" + str(net_profit) + "\nAverage Change: $" + str(avg_change) + "\nGreatest Increase in Profits: $" + str(max_change) + " " + str(max_change_date) + "\nGreatest Decrease in Profits: $" + str(min_change) + " " + str(min_change_date)

# set the location of the output file
outfile = os.path.join(curr_dir, "Analysis", "financial_analysis.txt")

# write the output file
with open(outfile, 'w') as file:
    file.write(summary)

# display the results
print(summary)
