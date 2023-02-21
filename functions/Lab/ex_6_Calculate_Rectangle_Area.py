# Create a function that calculates and returns the area of a rectangle by given width and height.
# Print the result on the console.
# Examples
# Input	    Output
# 3
# 4	        12
# 6
# 2	        12

weight_input = int(input())
height_input = int(input())


def area(a, ha):
    return int(a * ha)


print(area(weight_input, height_input))