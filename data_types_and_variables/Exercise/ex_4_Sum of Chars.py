# Write a program, which sums the ASCII codes of N characters and prints the sum on the console.
# On the first line, you will receive N – the number of lines.
# On the following N lines – you will receive a letter per line.
# Print the total sum in the following format: "The sum equals: {total_sum}".
# Note: n will be in the interval [1…20].
# Examples
# Input	Output
# 5
# A
# b       The sum equals: 399
# C
# d
# E
# Input	Output
# 12
# S
# o
# f
# t       The sum equals: 1263
# U
# n
# i
# R
# u
# l
# z
# z

n = int(input())
total = 0

for i in range(n):
    current_char = input()
    total += ord(current_char)

print(f"The sum equals: {total}")
