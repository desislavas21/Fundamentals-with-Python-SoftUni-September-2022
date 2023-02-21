# John invented a game with numbers and letters from the English alphabet. The game was simple.
# You receive a string consisting of a number between two letters. For the given string, you should perform different mathematical operations to achieve a result:
# •	First, if the letter in front of the number is:
# o	Uppercase: divide the number by the letter's position in the alphabet (starting from 1)
# o	Lowercase: multiply the number with the letter's position in the alphabet (starting from 1)
# •	Next, if the letter after the number is:
# o	Uppercase: subtract its position from the resulting number (starting from 1)
# o	Lowercase: add its position to the resulting number (starting from 1)
# The game was too easy for John. He decided to complicate it by doing the same calculations to multiple strings keeping track of only the total sum of all results. Once he started to solve this with more strings and bigger numbers, it became quite hard to do it only in his mind.
# He kindly asks you to write a program that performs the operations described above and sums the final results of each string.
# Input	                    Output
# A12b s17G	                330.00
# P34562Z q2576f   H456z	46015.12
# a1A	                    0.00
sentence = input().split()
number = 0
total = 0


def char_position(letter):
    return ord(letter.lower()) - 96


for word in sentence:
    letter_position_0 = char_position(word[0])
    letter_position_1 = char_position(word[-1])
    first = word[0]
    last = word[-1]
    number = int(word[1:-1])
    if first.isupper():
        number = number / letter_position_0
    elif first.islower():
        number = number * letter_position_0
    if last.isupper():
        number = number - letter_position_1
    elif last.islower():
        number = number + letter_position_1
    total += number

print(f"{total:.2f}")