# Write a program that converts British pounds (integer) to US dollars formatted to the 3rd decimal point.
# 1 British Pound = 1.31 Dollars.
# Input	    Output
# 80	    104.800
# 39	    51.090

pounds = int(input())
dollars = pounds * 1.31

print(f"{dollars:.3f}")