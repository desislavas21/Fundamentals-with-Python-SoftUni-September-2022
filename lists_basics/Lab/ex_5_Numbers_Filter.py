# On the first line, you will receive a single number n. On the following n lines, you will receive integers.
# After that, you will be given one of the following commands:
# •	even
# •	odd
# •	negative
# •	positive
# Filter all the numbers that fit in the category (0 counts as a positive and even). Finally, print the result.
# Example
# Input	        Output
# 5
# 33
# 19
# -2
# 18
# 998
# even	        [-2, 18, 998]
# Input	        Output
# 3
# 111
# -4
# 0
# negative	    [-4]

n = int(input())
all_n = []
filtered = []

for _ in range(n):
    current_number = int(input())
    all_n.append(current_number)

command = input()

for i in range(len(all_n)-1, -1, -1):
    element = all_n[i]
    if command == 'even':
        if element % 2 == 0 or element == 0:
            filtered.append(element)
    elif command == 'odd':
        if element % 2 != 0:
            filtered.append(element)
    elif command == 'negative':
        if element < 0:
            filtered.append(element)
    elif command == 'positive':
        if element >= 0:
            filtered.append(element)
filtered.reverse()
print(filtered)