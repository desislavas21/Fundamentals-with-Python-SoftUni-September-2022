# Write a function that receives 3 characters.
# Concatenate all the characters into one string and print it on the console.
# Example
# Input	Output
# a
# b       abc
# c
# Input	Output
# %
# 2       %2o
# o
# Input	Output
# 1
# 5       15p
# p

first, second, third = input(), input(), input()
new = first + second + third
print(new)