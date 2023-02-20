# On the first line, you will receive a key (integer). On the second line, you will receive n – the number of lines,
# which will follow. On the next n lines – you will receive a lower and an uppercase letter per line.
# You should add the key to each of the characters and append them to a message. In the end, print the decrypted message.
# Example
# Input	    Output
# 3
# 7
# P
# l         SoftUni
# c
# q
# R
# k
# f
# Input	    Output
# 1
# 7
# C
# d         Decrypt
# b
# q
# x
# o
# s

key = int(input())
n = int(input())
new_word = ''
for i in range(n):
    current_ch = input()
    numbers = ord(current_ch) + key
    new_word += chr(numbers)

print(new_word)


