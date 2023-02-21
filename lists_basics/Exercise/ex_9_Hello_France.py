# You want to go to France by train, and the train ticket costs exactly 150$. You do not have enough money, so you decide to buy some items with your budget and then sell them at a higher price – with a 40% markup.
# You will receive a collection of items and a budget in the following format:
# {type->price|type->price|type->price……|type->price}
# {budget}
# The prices for each of the types cannot exceed a specific price, which is given below:
# Type	        Maximum Price
# Clothes	    50.00
# Shoes	        35.00
# Accessories	20.50
# If a price for a particular item is higher than the maximum price, don't buy it. Every time you buy an item, you have to reduce the budget with its price value. If you don't have enough money for it, you can't buy it. Buy as many items as you can.
# Next, you should increase the price of each item you have successfully bought by 40% and then sell it. Calculate if the budget after selling all the items is enough for buying the train ticket.
# Input
# Clothes->43.30|Shoes->25.25|Clothes->36.52|Clothes->20.90|Accessories->15.60
# 120
# Output
# 60.62 35.35 51.13
# Profit: 42.03
# Hello, France!
# Input
# Shoes->41.20|Clothes->20.30|Accessories->40|Shoes->15.60|Shoes->33.30|Clothes->48.60
# 90
# Output
# 28.42 21.84 46.62
# Profit: 27.68
# Not enough money.

train_ticket = 150
products = input().split("|")
budget = int(input())
initial_budget = budget
bought_items = []
for item in products:
    if budget <= 0:
        break
    type, price = item.split("->")
    price = float(price)
    if type == "Clothes":
        if price < 50 and budget >= price:
            bought_items.append(price)
            budget -= price
    elif type == "Shoes":
        if price < 35 and budget >= price:
            bought_items.append(price)
            budget -= price
    elif type == "Accessories":
        if price < 20.50 and budget >= price:
            bought_items.append(price)
            budget -= price

sold = []
profit = 0
for item in bought_items:
    sold.append(round(item * 1.4, 2))
for index in range(len(bought_items)):
    profit += (sold[index] - bought_items[index])
print(" ".join(str(x) for x in sold))
print(f"Profit: {profit}")
if (sum(sold) + budget) >= train_ticket:
    print("Hello, France!")
else:
    print("Not enough money.")
