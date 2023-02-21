# Write a program that receives a single string.
# On the first line, print all the digits found in the string, on the second – all the letters,
# and on the third – all the other characters. There will always be at least one digit, one letter, and one other character.
# Input
# Agd#53Dfg^&4F53
# Output
# 53453
# AgdDfgF
# #^&
sentence = input()
digits = []
letters = []
others = []
for ch in sentence:
    if ch.isdigit():
        digits.append(ch)
    elif ch.isupper() or ch.islower():
        letters.append(ch)
    else:
        others.append(ch)

print("".join(digits))
print("".join(letters))
print("".join(others))