# Write a function that calculates the total price of an order and returns it. The function should receive one of the following products: "coffee", "coke", "water", or "snacks", and a quantity of the product. The prices for a single piece of each product are:
# •	coffee - 1.50
# •	water - 1.00
# •	coke - 1.40
# •	snacks - 2.00
# Print the result formatted to the second decimal place.
# Example
# Input     Output
# water
# 5	        5.00
# coffee
# 2	        3.00

snack_input = input()
number_input = int(input())


def total(snack, number):
    overall = None
    if snack == 'coffee':
        overall = 1.5 * number
    elif snack == 'water':
        overall = 1 * number
    elif snack == 'coke':
        overall = 1.4 * number
    elif snack == 'snacks':
        overall = 2 * number
    return f"{overall:.2f}"


print(total(snack_input, number_input))