# On the first line, you will receive n – the number of lines, which will follow. On the following n lines, you will receive one of the following:
# •	Opening bracket – "(",
# •	Closing bracket – ")" or
# •	Random string
# Your task is to find out if the brackets are balanced.
# That means after every opening bracket should follow a closing one.
# Nested parentheses are not valid, and if, for example, two consecutive opening brackets exist,
# the expression should be marked as unbalanced.
# You should print "BALANCED" if the parentheses are balanced and "UNBALANCED" otherwise.
# Example
# Input	        Output
# 8
# (
# 5 + 10
# )             BALANCED
# * 2 +
# (
# 5
# )
# -12
# Input	        Output
# 6
# 12 *
# )             UNBALANCED
# 10 + 2 -
# (
# 5 + 10
# )

n = int(input())
balanced = True
for i in range(n):
    command = input()
    if command == '(' or command == ')':
        balanced = False
    if command == ')':
        balanced = True

if balanced:
    print('BALANCED')
else:
    print('UNBALANCED')
