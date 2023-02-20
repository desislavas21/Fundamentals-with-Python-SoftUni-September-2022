# You will be given an integer that represents a distance in meters.
# Write a program that converts meters to kilometers formatted to the second decimal point.
# Examples
# Input	    Output
# 1852	    1.85
# 798	    0.80

meters = int(input())
kilometres = meters / 1000
print(f"{kilometres:.2f}")