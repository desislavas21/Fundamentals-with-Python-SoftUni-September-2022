# Write a program that receives a list of integer numbers (separated by a single space) and a number n. The number n represents the count of numbers to remove from the list. You should remove the smallest ones, and then, you should print all the numbers that are left in the list, separated by a comma and a space ", ".
# Example
# Input	            Output
# 10 9 8 7 6 5
# 3	                10, 9, 8
# Input	            Output
# 1 10 2 9 3 8
# 2	                10, 9, 3, 8

numbers = input().split(' ')
n = int(input())
number_digit = []
for item in numbers:
    number_digit.append(int(item))

for i in range(n):
    number_digit.remove(min(number_digit))
final = []
for number in number_digit:
    final.append(str(number))

print(', '.join(final))