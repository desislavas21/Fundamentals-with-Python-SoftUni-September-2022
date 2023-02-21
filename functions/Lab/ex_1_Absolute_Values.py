# Write a program that receives a sequence of numbers, separated by a single space, and prints their absolute value as a
# list. Use abs().
# Example
# Input	            Output
# 1 2.5 -3 -4.5	    [1.0, 2.5, 3.0, 4.5]
# -0 1 10 -6.66	    [0.0, 1.0, 10.0, 6.66]

numbers = input().split(' ')


def programme(numbers_list: list):
    absolute_values = []

    for number in numbers_list:
        absolute_values.append(abs(float(number)))

    return absolute_values


print(programme(numbers))
