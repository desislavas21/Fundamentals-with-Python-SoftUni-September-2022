# Create a function that receives three parameters, calculates a result depending on the given operator, and returns it.
# Print the result of the function.
# The input comes as three parameters – an operator as a string and two integer numbers.
# The operator can be one of the following:  "multiply", "divide", "add", "subtract".
# Example
# Input	        Output
# subtract
# 5
# 4             1
# divide
# 8
# 4	            2

input_operator = input()
first_number = int(input())
second_number = int(input())


def solve(a, b, operator):
    result = None
    if operator == "multiply":
        result = a * b
    elif operator == "divide":
        result = int(a / b)
    elif operator == "add":
        result = a + b
    elif operator == "subtract":
        result = a - b
    return result


print(solve(first_number, second_number, input_operator))