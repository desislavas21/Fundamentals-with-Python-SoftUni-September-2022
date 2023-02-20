# Calculate how many courses will be needed to elevate N persons by using an elevator with a capacity of P persons.
# The input holds two lines: the number of people N and the capacity P of the elevator.
# Input	    Output      Comments
# 17                    5 courses * 3 people
# 3	        6           + 1 course * 2 persons
# Input	    Output
# 4                     All the persons fit inside the elevator.
# 5	        1           Only one course is needed.
# Input	    Output
# 10                    2 courses * 5 people
# 5	        2

import math
people = int(input())
capcity = int(input())
full_cources = math.ceil(people // capcity)
left_people = people - full_cources * capcity

if people <= capcity:
    print("All the persons fit inside the elevator. Only one course is needed")
elif people % capcity == 0:
    print(f"{full_cources} courses * {capcity} people")
else:
    print(f"{full_cources} courses * {capcity} people + 1 course * {left_people} persons")