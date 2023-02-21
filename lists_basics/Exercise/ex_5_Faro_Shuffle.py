# A faro shuffle is a method for shuffling a deck of cards, in which the deck is split exactly in half. Then the cards in the two halves are perfectly interleaved, such that the original bottom card is still on the bottom and the original top card is still on top.
# For example, faro shuffling the list ['ace', 'two', 'three', 'four', 'five', 'six'] once, gives ['ace', 'four', 'two', 'five', 'three', 'six']
# Write a program that receives a single string (cards separated by space) and on the second line receives a count of faro shuffles that should be made. Print the state of the deck after the shuffle.
# Note: The length of the deck of cards will always be an even number.
# Example
# Input	                Output
# a b c d e f g h
# 5	                    ['a', 'c', 'e', 'g', 'b', 'd', 'f', 'h']
# one two three four
# 3	                    ['one', 'three', 'two', 'four']


cards = input().split()
shuffle = int(input())

lenght = len(cards)
mid = int(lenght / 2)

for i in range(0, shuffle):
    lst = []
    for p in range(0, mid):
        lst.append(cards[p])
        lst.append(cards[mid])
        mid += 1
    cards = lst
    mid = int(lenght / 2)
print(lst)
