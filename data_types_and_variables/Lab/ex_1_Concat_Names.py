# Write a program that reads two names and a delimiter. It should print the names joined by the delimiter.
# Examples
# Input	    Output
# John
# Smith     John->Smith
# ->

# Jan
# White     Jan<->White
# <->

# Linda
# Terry     Linda=>Terry
# =>

name_1, name_2, delimiter = input(), input(), input()
print(f"{name_1}{delimiter}{name_2}")