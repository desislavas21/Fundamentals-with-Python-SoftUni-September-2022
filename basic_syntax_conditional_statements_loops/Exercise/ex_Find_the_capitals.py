#Write a program that takes a single string and prints a list of all the capital letters indices.
# Input       Output
# pYtHoN      [1, 3, 5]
# CApiTAls    [0, 1, 4, 5]
word = input()
number_of_cpitals = []
for ch in word:
    if ch.isupper():
        number_of_cpitals.append(word.index(ch))

print(number_of_cpitals)