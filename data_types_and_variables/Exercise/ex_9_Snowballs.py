# Tony and Andi love playing in the snow and having snowball fights, but they always argue about who makes the best snowballs. They have decided to involve you in their fray by writing a program that calculates snowball data and outputs the best snowball value.
# You will receive N – an integer, the number of snowballs being made by Tony and Andi.
# On the following lines, you will receive 3 inputs for each snowball:
# •	The weight of the snowball (integer).
# •	The time needed for the snowball to get to its target (integer).
# •	The quality of the snowball (integer).
# For each snowball, you must calculate its value by the following formula:
# (snowball_weight / snowball_time) ** snowball_quality
# In the end, you must print the highest calculated value of a snowball.
# Example
# Input	    Output
# 2
# 10
# 2         10 : 2 = 125 (3)
# 3
# 5
# 5
# 5
# Input	    Output
# 3
# 10
# 5
# 7
# 16        10 : 5 = 128 (7)
# 4
# 2
# 20
# 2
# 2


number_of_snowballs = int(input())
best_snowball = 0
best_weight = 0
best_time = 0
best_quality = 0
if number_of_snowballs >= 0 and number_of_snowballs <= 100:
    for i in range(number_of_snowballs):
        weight, time, quality = int(input()), int(input()), int(input())
        if weight >=0 and weight <= 1000 and time >= 1 and time <= 500 and quality >= 0 and quality <= 100:
            formula = int((weight / time) ** quality)
            if formula > best_snowball:
                best_snowball = formula
                best_weight = weight
                best_time = time
                best_quality = quality
            else:
                continue
    print(f"{best_weight}:{best_time} = {best_snowball} ({best_quality})")