# As a gladiator, Peter needs to repair his broken equipment when he loses a fight. His equipment consists of a helmet,
# a sword, a shield, and an armor.
# You will receive Peter's lost fights count.
# Every second lost game, his helmet is broken.
# Every third lost game, his sword is broken.
# When both his sword and helmet are broken in the same lost fight, his shield also breaks.
# Every second time his shield brakes, his armor also needs to be repaired.
# You will receive the price of each item in his equipment. Calculate his expenses for the year for renewing his equipment.
# Example
# Input     Output
# 7
# 2
# 3         Gladiator expenses: 16.00 aureus
# 4
# 5
# Input	    Output
# 23
# 12.50
# 21.50     Gladiator expenses: 608.00 aureus
# 40
# 200

lost_fights, helmet = int(input()), float(input()),
sword, shield, armor = float(input()), float(input()), float(input())
money = 0
repaired_shield = 0
for fight in range(1, lost_fights + 1):
    if fight % 2 == 0:
        money += helmet
    if fight % 3 == 0:
        money += sword
        if fight % 2 == 0:
            money += shield
            repaired_shield += 1
            if repaired_shield % 2 == 0 and repaired_shield != 0:
                money += armor

print(f"Gladiator expenses: {money:.2f} aureus")

