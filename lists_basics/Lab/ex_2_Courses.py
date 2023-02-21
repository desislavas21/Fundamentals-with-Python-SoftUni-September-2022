# On the first line, you will receive a single number n. On the following n lines, you will receive names of courses.
# You should create a list of courses and print it.
# Example
# Input	                        Output
# 2
# PB Python
# PF Python	                    ['PB Python', 'PF Python']
# Input	                        Output
# 4
# Front-End
# C# Web
# JS Core
# Programming Fundamentals	    ['Front-End', 'C# Web', 'JS Core', 'Programming Fundamentals']

n = int(input())
courses = []
for _ in range(n):
    names = input()
    courses.append(names)

print(courses)