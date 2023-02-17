# Write a program that receives a number n on the first line.
# On the following n lines, it receives different integer numbers.
# If the program receives an odd number,
# print "{num} is odd!" and end the program.
# Otherwise, if all numbers given are even, print "All numbers are even.".
# Example
# Input             Output
# 2
# 12                All numbers are even.
# 286
#
# 5
# 2                 9 is odd!
# 9

n = int(input())
for _ in range(n):
    current = int(input())
    if current % 2 != 0:
        print(f"{current} is odd!")
        break
else:
    print("All numbers are even.")