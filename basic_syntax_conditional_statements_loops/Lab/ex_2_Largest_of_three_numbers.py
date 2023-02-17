# Write a program that receives three whole numbers and prints the largest one.
# Example
# Input             Output
#  3
# -1                  5
#  5
#
#  0
# -1                  0
# -1

first, second, third = int(input()), int(input()), int(input())
# 1
print(max(first, second, third))
# 2
if first > second and first > third:
    print(first)
elif second > first and second > third:
    print(second)
elif third > first and third > second:
    print(third)