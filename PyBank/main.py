import csv
import os

import pandas as pd


#capture path in variable

budget_csv=os.path.join('..','PyBank','Resources','budget_data.csv')


#use pandas to read data

df=pd.read_csv(budget_csv)

#Count number of months

number_of_months=len(df)

print("Total months: ",number_of_months)


#Get total amount of profit/losses

total_amount=sum(df["Profit/Losses"])

print("Total: ",total_amount)


#Calculate avg change profit/losses

average_change=total_amount/number_of_months

print("Average Change: ",average_change)


#Calculate avg change profit/losses

greatest_increase=max(df["Profit/Losses"])

print("Greatest Increase in Profit: ",greatest_increase)


#Calculate avg change profit/losses

greatest_decrease=min(df["Profit/Losses"])

print("Greatest Decrease in Profit: ",greatest_decrease)
