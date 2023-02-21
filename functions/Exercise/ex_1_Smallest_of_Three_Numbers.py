# Write a function that receives three integer numbers and returns the smallest. Print the result on the console.
# Use an appropriate name for the function.
# Examples
# Input	    Output
# 2
# 5
# 3	        2
#
# 600
# 342
# 123	    123
#
# 25
# 21
# 4	        4

first = int(input())
second = int(input())
third = int(input())


def smallest_number(a, b, c):
    return min(a, b, c)


print(smallest_number(first, second, third))