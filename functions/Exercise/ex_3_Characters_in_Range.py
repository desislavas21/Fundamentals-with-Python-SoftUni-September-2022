# Write a function that receives two characters and returns a single string with all the characters in between them
# (according to the ASCII code), separated by a single space. Print the result on the console.
# Input	    Output
# a
# d	        b c
# Input	    Output
# #
# :	        $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9
# Input	    Output
# #
# C	        $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B

def characters_between(start, finish):
    start = ord(start)
    finish = ord(finish)
    for i in range(start+1, finish):
        print(chr(i), end=' ')


first = input()
second = input()
characters_between(first, second)