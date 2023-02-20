# Write a program that reads an integer number of centuries and converts it to years, days, hours, and minutes.
# Examples
# Input	    Output
# 1	        1 centuries = 100 years = 36524 days = 876576 hours = 52594560 minutes
# 5	        5 centuries = 500 years = 182621 days = 4382904 hours = 262974240 minutes


centuries = int(input())
years = centuries * 100
days = int(years * 365.242)
hours = 24 * days
minutes = 60 * hours
seconds = 60 * minutes
print(f"{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")