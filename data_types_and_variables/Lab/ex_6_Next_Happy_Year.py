# You are saying goodbye to your best friend: "See you next happy year". Happy Year is the year with only
# distinct digits, for example, 2018. Write a program that receives an integer number and finds the next happy year.
# Example
# Input	    Output
# 8989	    9012
# 1001	    1023


year = int(input())

happy_year_condition = False

while not happy_year_condition:
    year += 1
    year_set = set()

    for i in range(len(str(year))):
        year_set.add(str(year)[i])

    happy_year_condition = len(year_set) == len(str(year))

print(year)