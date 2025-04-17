import csv
import pandas as pd
df = pd.read_csv (r'C:\Users\rache\python-challenge-1\PyBank\Resources\budget_data.csv')

#Load the CSV File
import os
file_path = os.path.join 
"('C:''Users','rache','python-challenge-1',PyBank','Resources','budget_data.csv')"

#Total number of months
total_months = df.shape[0]

print(f"Total Months:{total_months}")

#Net total amount of Profit/Losses
net_total = df['Profit/Losses'].sum()
print(f"Net Totat: ${net_total}")

#Calculate month-month changes
df['Change'] = df['Profit/Losses'].diff()
#Compute the average of those changes(skin the first Nan)
average_change = df['Change'].mean()

print(f"Average Change: ${average_change:.2f}")

#Greatest Increase in Profits
max_change = df['Change'].max()
max_change_month = df.loc[df['Change'].idxmin(),'Date']

#Greatest Decrease in Profits
min_change = df['Change'].min()
min_change_month = df.loc[df['Change'].idxmin(),'Date']

#Print the analysis
print('Financial Analysis')
print('________________________')
print(f'Total Months:{total_months}')
print(f'Total:${net_total}')
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits:{max_change_month} (${int(max_change)})")
print(f'Greatest Decrease in Profits: {min_change_month} (${int(min_change)})')

#Buld output lines
lines = [
    "Financial Analysis",
    "__________________________"
     f"Total Months:{total_months}"
     f"Total: ${net_total}",
     f"Average Change: ${average_change:.2f}"
     f"Greatest Increase in Profits:{max_change_month} (${int(max_change)})"
    f'Greatest Decrease in Profits: {min_change_month} (${int(min_change)})'
]

# Write to text file
out_path = os.path.join (r'c:\Users\rache\python-challenge-1\PyBank\analysis', 'budget_analysis.txt')
os.makedirs(os.path.dirname(out_path), exist_ok=True)

#   Write to text file
with open(out_path, 'w') as f:
    for line in lines:
        f.write(line + '\n')
print(f'Results written to {out_path}')