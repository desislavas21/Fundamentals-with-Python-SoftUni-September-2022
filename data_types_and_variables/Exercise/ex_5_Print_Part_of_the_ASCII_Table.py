# Write a program that prints part of the ASCII table characters on the console,
# separated by a single space. On the first line of input,
# you will receive the char index you should start with.
# On the second line - the index of the last character you should print.
# Example
# Input	Output
# 60
# 65	    < = > ? @ A
# Input	Output
# 69
# 79	    E F G H I J K L M N O
# Input	Output
# 97
# 104	    a b c d e f g h
# Input	Output
# 40
# 55	    ( ) * + , - . / 0 1 2 3 4 5 6 7

start, finish = int(input()), int(input())

for i in range(start, finish+1):
    current_ch = chr(i)
    print(current_ch, end=" ")