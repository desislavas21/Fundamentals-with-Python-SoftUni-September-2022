# Write a function that receives a string and a counter n.
# The function should return a new string – the result of repeating the old string n times.
# Print the result of the function. Try using lambda.
# Examples
# Input	    Output
# abc
# 3	        abcabcabc
# String
# 2	        StringString

word = input()
n = int(input())
repeat = lambda a, b: a * b
result = repeat(word, n)
print(result)