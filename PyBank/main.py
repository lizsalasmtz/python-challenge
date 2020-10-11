import os
import csv

# Path to collect data from the Resources folder
PyBank_budget_data_csv = os.path.join('..', 'Resources', 'PyBank_budget_data.csv')

# Define the function and have it accept the PyBank_data as its sole parameter
def print_percentages(PyBank_data):
    # For readability, it can help to assign your values to variables with descriptive names
    date = str(PyBank_data[0])
    profit_losses = int(PyBank_data[1])

    # the total number of months included in the dataset
    # the net total amount of "Profit/Losses" over the entire period
    total_matches = profit_losses
    # the average of the changes in "Profit/Losses" over the entire period
    # the greatest increase in profits (date and amount) over the entire period
    # the greatest decrease in losses (date and amount) over the entire period