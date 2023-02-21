# You will receive three integer numbers.
# Write functions named:
# •	sum_numbers() that returns the sum of the first two integers
# •	subtract() that returns the difference between the returned result of the first function and the third integer
# Wrap the two functions in a function named add_and_subtract() which will receive the three numbers as parameters. Print the result of the subtract() function on the console.
# Examples
# Input	    Output
# 23
# 6
# 10	    19
# Input	    Output
# 1
# 17
# 30	    -12
# Input	    Output
# 42
# 58
# 100	    0

def sum_numbers(a: int, b: int):
    c = a + b
    return c


def subtract(c: int, d: int):
    q = c - d
    return q


def add_and_subtract(a: int, b: int, d: int):
    c = sum_numbers(a, b)
    return subtract(c, d)


a_example = int(input())
b_example = int(input())
d_example = int(input())

print(add_and_subtract(a_example, b_example, d_example))