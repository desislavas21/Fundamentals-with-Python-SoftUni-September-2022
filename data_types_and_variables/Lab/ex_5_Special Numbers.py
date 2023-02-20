# Write a program that reads an integer n. Then, for all numbers in the range [1, n], prints the number
# and if it is special or not (True / False). A number is special when the sum of its digits is 5, 7, or 11.
# Example
# Input
# 15
# Output
# 1 -> False
# 2 -> False
# 3 -> False
# 4 -> False
# 5 -> True
# 6 -> False
# 7 -> True
# 8 -> False
# 9 -> False
# 10 -> False
# 11 -> False
# 12 -> False
# 13 -> False
# 14 -> True
# 15 -> False

n = int(input())

for i in range(1, n+1):
    number_s = 0
    digits = i
    while digits > 0:
        number_s += digits % 10
        digits = int(digits/10)
    if number_s == 5 or number_s == 7 or number_s == 11:
        print(f"{i} -> True")
    else:
        print(f'{i} -> False')
