# Write a program that receives strings on different lines and extracts only the numbers. Print all extracted numbers on a single line, separated by a single space.
# Examples
# Input	                            Output
# The300
# What is that?
# I think it's the 3rd movie
# Let's watch it at 22:45	        300 3 22 45
# Input	                            Output
# 123a456
# 789b987
# 654c321
# 0	                                123 456 789 987 654 321 0
# Input	                            Output
# Let's go11!!!11!
# Okey!1!	                        11 11 1
import re
pattern = '\d+'
line = input()

while line:
    matches = re.findall(pattern, line)
    if matches:
        print(' '.join(matches), end=" ")
    line = input()
