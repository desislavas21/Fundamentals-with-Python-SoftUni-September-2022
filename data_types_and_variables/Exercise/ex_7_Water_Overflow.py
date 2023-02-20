# You have a water tank with a capacity of 255 liters. On the first line,
# you will receive n – the number of lines, which will follow.
# On the following n lines, you will receive liters of water (integers),
# which you should pour into your tank. If the capacity is not enough,
# print "Insufficient capacity!" and continue reading the next line. On the last line, print the liters in the tank.
# Example
# Input	    Output
# 5
# 20
# 100       Insufficient capacity!
# 100
# 100
# 20
# 240
# Input	    Output
# 7
# 10
# 20
# 30        105
# 10
# 5
# 10
# 20
# Input	    Output
# 1
# 1000      Insufficient capacity!
# 0
# Input	    Output
# 4
# 250       Insufficient capacity!
# 10        Insufficient capacity!
# 20        Insufficient capacity!
# 40        250

n = int(input())
poured = 0

for i in range(n):
    liters = int(input())
    if liters < 255 and poured <= 255:
        poured += liters
    if liters > 255 or poured > 255:
        print("Insufficient capacity!")
        if poured > 255:
            poured -= liters
        continue
print(poured)
