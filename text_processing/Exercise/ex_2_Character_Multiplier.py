# Create a program that receives two strings on a single line separated by a single space. Then, it
# prints the sum of their multiplied character codes as follows: multiply str1[0] with str2[0] and
# add the result to the total sum, then continue with the next two characters. If one of the strings is
# longer than the other, add the remaining character codes to the total sum without multiplication.
# Input	        Output
# George Peter	52114
# 123 522	    7647
# a aaaa	    9700
long, short = input().split(" ")
long = [ord(x) for x in long]
short = [ord(x) for x in short]
total = 0
should_be_removed = []
if len(long) == len(short):
    for index in range(0, len(short)):
        total += (long[index] * short[index])
else:
    if len(long) < len(short):
        long, short = short, long
    for index in range(len(short)):
        total += (long[index] * short[index])
        should_be_removed.append(long[index])
    for item in should_be_removed:
        long.remove(item)
    for last in long:
        total += last
print(total)