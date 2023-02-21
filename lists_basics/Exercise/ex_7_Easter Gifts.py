# As a good friend, you decide to buy presents for your friends.
# Create a program that helps you plan the gifts for your friends and family. First, you are going to receive the gifts you plan on buying on a single line, separated by space, in the following format:
# "{gift1} {gift2} {gift3}… {giftn}"
# Then you will start receiving commands until you read the "No Money" message. There are three possible commands:
# •	"OutOfStock {gift}"
# o	Find the gifts with this name in your collection, if any, and change their values to "None".
# •	"Required {gift} {index}"
# o	If the index is valid, replace the gift on the given index with the given gift.
# •	"JustInCase {gift}"
# o	Replace the value of your last gift with this one.
# In the end, print the gifts on a single line, except the ones with value "None", separated by a single space in the following format:
# "{gift1} {gift2} {gift3} … {giftn}"
# Examples
# Input
# Eggs StuffedAnimal Cozonac Sweets EasterBunny Eggs Clothes
# OutOfStock Eggs
# Required Spoon 2
# JustInCase ChocolateEgg
# No Money
# Output
# StuffedAnimal Spoon Sweets EasterBunny ChocolateEgg
# Examples
# Input
# Sweets Cozonac Clothes Flowers Wine Clothes Eggs Clothes
# Required Paper 8
# OutOfStock Clothes
# Required Chocolate 2
# JustInCase Hat
# OutOfStock Cable
# No Money
# Output
# Sweets Cozonac Chocolate Flowers Wine Eggs Hat

planned_gifts = input().split(" ")

while True:
    command = input()
    if command == "No Money":
        break
    action, gift, *index = command.split(" ")
    if action == "OutOfStock":
        for i in range(len(planned_gifts)):
            if planned_gifts[i] == gift:
                planned_gifts[i] = "None"
    elif action == "Required":
        if int(index[0]) in range(len(planned_gifts)):
            planned_gifts[int(index[0])] = gift
    elif action == "JustInCase":
        planned_gifts[-1] = gift
print(' '.join(x for x in planned_gifts if x != "None"))
