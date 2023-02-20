# Write a program that reads four integer numbers. It should add the first to the second number,
# integer divide the sum by the third number, and multiply the result by the fourth number. Print the final result.
# Examples
# Input	Output
# 10
# 20      30
# 3
# 3
# Input	Output
# 15
# 14      42
# 2
# 3

first, second, third, fourth = int(input()), int(input()), int(input()), int(input())
step_one = first + second
step_two = int(step_one/third)
step_three = step_two * fourth
print(step_three)