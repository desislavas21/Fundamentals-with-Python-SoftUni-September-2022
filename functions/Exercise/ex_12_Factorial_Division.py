# Write a function that receives two integer numbers. Calculate the factorial of each number.
# Divide the first result by the second and print the division formatted to the second decimal point.
# Examples
# Input	    Output
# 5
# 2	        60.00
# Input	    Output
# 6
# 2	        360.00

def factorial(a: int, b: int):
    a_factorial = 1
    b_factorial = 1
    for number in range(a, 0, -1):
        a_factorial *= number
    for number in range(b, 0, -1):
        b_factorial *= number
    final = a_factorial / b_factorial
    return f"{final:.2f}"


a_example = int(input())
b_example = int(input())
print(factorial(a_example, b_example))