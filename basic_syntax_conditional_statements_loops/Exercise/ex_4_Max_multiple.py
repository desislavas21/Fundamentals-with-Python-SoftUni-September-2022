# On the first line, you will be given a positive number, which will serve as a divisor.
# On the second line, you will receive a positive number that will be the boundary.
# You should find the largest integer N, that is:
# · divisible by the given divisor
# · less than or equal to the given bound
# · greater than 0
# Note: it is guaranteed that N is found.
# Examples
# Input     Output
# 2
# 7         6

# 10
# 50        50

# 37
# 200       185

divisor, boundary = int(input()), int(input())

for current in range(boundary, divisor, -1):
    if current % divisor == 0:
        print(current)
        break