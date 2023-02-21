# Write a program that receives a sequence of numbers (integers) separated by a single space. It should print the min and max values of the given numbers and the sum of all the numbers in the list. Use min(), max() and sum().
# The output should be as follows:
# •	On the first line: "The minimum number is {minimum number}"
# •	On the second line: "The maximum number is {maximum number}"
# •	On the third line: "The sum number is: {sum of all numbers}"
# Example
# Input
# 2 4 6
# Output
# The minimum number is 2
# The maximum number is 6
# The sum number is: 12
# Input
# 12 52 11 53 2 8 45
# Output
# The minimum number is 2
# The maximum number is 53
# The sum number is: 183

numbers = input().split(' ')
numbers_int = []
for number in numbers:
    numbers_int.append(int(number))
minimum_number = min(numbers_int)
maximum_number = max(numbers_int)
sum_of_all_numbers = sum(numbers_int)
print(f"The minimum number is {minimum_number}\nThe"
      f" maximum number is {maximum_number}\nThe sum number is: {sum_of_all_numbers}")
