# Write a program that rounds all the given numbers, separated by a single space, and prints the result as a list. Use round().
# Example
# Input	                Output
# 1.0 2.5 3.0 4.5	    [1, 2, 3, 4]
# 2.56 1.9 -3.4 8.1	    [3, 2, -3, 8]

numbers = input().split(' ')


def programme(numbers_list: list):
    final = []
    for number in numbers_list:
        final.append(round(float(number)))
    return final


print(programme(numbers))