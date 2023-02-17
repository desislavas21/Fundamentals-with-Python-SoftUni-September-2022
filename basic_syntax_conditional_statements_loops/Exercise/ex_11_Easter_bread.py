# Since it is Easter, you have decided to make some loaves of Easter bread and exchange them for eggs.
# Create a program that calculates how many loaves you can make (according to the recipe) with the budget you have.
# Here is the recipe for one loaf:
# Eggs - 1 pack
# Flour - 1 kg
# Milk - 0.250 l
# First, you will receive your budget. Then, you will receive the price for 1 kg flour.
# The price for 1 pack of eggs is 75% of the price for 1 kg flour.
# The price for 1L milk is 25% more than the price for 1 kg flour.
# Keep in mind that you use only 250ml milk for a bread.
# Start cooking the loaves and keep making them until you have enough budget.
# Keep in mind that:
# · For every loaf of bread that you make, you will receive 3 colored eggs.
# · For every 3rd bread you make, you will lose some of your colored eggs after receiving the usual 3 colored eggs for your bread.
# The count of eggs you will lose is calculated when you subtract 2 from your current count of loaves - ({current_bread_count} - 2)
# In the end, print the loaves of bread you made, the eggs you have collected, and the money you have left, formatted to the 2nd decimal place, in the following format:
# "You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left}BGN left."
# Example
# Input       Output
# 20.50
# 1.25        You made 7 loaves of Easter bread! Now you have 16 eggs and 2.45BGN left.
#
# 15.75
# 1.4         You made 5 loaves of Easter bread! Now you have 14 eggs and 1.31BGN left.


budget, flour = float(input()), float(input())
eggs = 0.75 * flour
litter_milk = 1.25 * flour
ml_milk = litter_milk / 4
one_loaf = flour + eggs + ml_milk
made_bread = 0
bread = budget // one_loaf
received_eggs = 0
while made_bread != bread:
    made_bread += 1
    received_eggs += 3
    if made_bread % 3 == 0:
        received_eggs -= (made_bread - 2)
money_left = budget - bread * one_loaf

print(f"You made {made_bread} loaves of Easter bread! Now you have {received_eggs} eggs and {money_left:.2f}BGN left.")

