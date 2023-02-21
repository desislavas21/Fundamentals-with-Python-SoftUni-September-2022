# The group of adventurists has gone on their first task. Now they should walk through fire - literally. They should use all the water they have left. Your task is to help them survive.
# Create a program that calculates the water needed to put out a "fire cell", based on the given information about its "fire level" and how much it gets affected by water.
# First, you will be given the level of fire inside the cell with the integer value of the cell, which represents the needed water to put out the fire.  They will be given in the following format:
# "{typeOfFire} = {valueOfCell}#{typeOfFire} = {valueOfCell}# … {typeOfFire} = {valueOfCell}"
# Afterward you will receive the amount of water you have for putting out the fires. There is a range of fire for each fire type, and if a cell's value is below or exceeds it, it is invalid, and you do not need to put it out.
# Type of Fire	    Range
# High	            81 - 125
# Medium	        51 - 80
# Low	            1 - 50
# If a cell is valid, you should put it out by reducing the water with its value. Putting out fire also takes effort, and you need to calculate it. Its value is equal to 25% of the cell's value. In the end, you will have to print the total effort. Keep putting out cells until you run out of water. Skip it and try the next one if you do not have enough water to put out a given cell. In the end, print the cells you have put out in the following format:
# "Cells:
#  - {cell1}
#  - {cell2}
#  …
#  - {cellN}"
# "Effort: {effort}"
# The effort should be formatted to the second decimal place.
# In the end, print the total fire you have put out from all the cells in the following format:
# "Total Fire: {total_fire}"
# Example
# Input
# High = 89#Low = 28#Medium = 77#Low = 23
# 1250
# Output
# Cells:
#  - 89
#  - 28
#  - 77
#  - 23
# Effort: 54.25
# Total Fire: 217
# Input
# High = 150#Low = 55#Medium = 86#Low = 40#High = 110#Medium = 77
# 220
# Output
# Cells:
#  - 40
#  - 110
# Effort: 37.50
# Total Fire: 150


level_of_fire = input().split("#")
split_level_of_fire = []
water = int(input())
effort = 0
put_out_cells = []
for current in level_of_fire:
    type_of_fire, value_of_cell = current.split(" = ")
    if water <= 0:
        break
    value_of_cell = int(value_of_cell)
    if type_of_fire == "Low":
        if value_of_cell not in range(1, 51):
            continue
    elif type_of_fire == "Medium":
        if value_of_cell not in range(51, 81):
            continue
    elif type_of_fire == "High":
        if value_of_cell not in range(81, 126):
            continue
    if water >= value_of_cell:
        water -= value_of_cell
        put_out_cells.append(value_of_cell)
        effort += (value_of_cell * 0.25)
    else:
        continue

print("Cells:")
for cell in put_out_cells:
    print(f" - {cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {sum(put_out_cells)}")
