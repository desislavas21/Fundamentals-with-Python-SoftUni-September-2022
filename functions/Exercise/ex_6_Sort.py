# Write a program that receives a sequence of numbers (integers) separated by a single space.
# It should print a sorted list of numbers in ascending order. Use sorted().
# Input	                Output
# 6 2 4	                [2, 4, 6]
# 12 52 11 53 2 8 45	[2, 8, 11, 12, 45, 52, 53]

numbers = list(map(int, input().split(" ")))
final = sorted(numbers)
print(final)