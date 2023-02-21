# On the first line, you will receive a string. On the second line, you will receive a second string.
# Write a program that removes all the occurrences of the first string in the second until there is no match.
# At the end, print the remaining string.
# Input	        Output
# ice
# kicegiciceeb	kgb
should_be_removed = input()
sentence = input()

while should_be_removed in sentence:
    sentence = sentence.replace(should_be_removed, "")
print(sentence)