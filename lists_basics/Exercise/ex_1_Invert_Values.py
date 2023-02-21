# Write a program that receives a single string containing positive and negative numbers separated by a single space.
# Print a list containing the opposite of each number.
# Example
# Input	            Output
# 1 2 -3 -3 5	    [-1, -2, 3, 3, -5]
# -4 0 2 57 -101	[4, 0, -2, -57, 101]

numbers = list(map(int, input().split(" ")))
opposite_numbers = []
for number in numbers:
    if number < 0:
        opposite_numbers.append(abs(number))
    elif number == 0:
        opposite_numbers.append(number)
    elif number > 0:
        opposite_numbers.append(-number)

print(opposite_numbers)