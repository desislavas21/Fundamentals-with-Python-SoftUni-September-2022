# Write a program that receives a single word, reverses it, and prints it.
# Example
# Input           Output
# Python          nohtyp
# banana          ananab

word = input()
# 1
word_reversed = ''
for i in range(len(word) - 1, -1, -1):
    word_reversed += word[i]
print(word_reversed)
# 2
print(word[::-1])
