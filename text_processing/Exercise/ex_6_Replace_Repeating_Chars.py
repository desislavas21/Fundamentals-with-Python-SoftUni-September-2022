# Write a program that reads a string from the console and replaces any sequence of the same
# letters with a single corresponding letter.
# Examples
# Input	                    Output
# aaaaabbbbbcdddeeeedssaa	abcdedsa
# qqqwerqwecccwd	        qwerqwecwd
text = input()
text = [ch for ch in text]
should_be_removed = []
for index in range(0, len(text) - 1):
    if text[index] == text[index + 1]:
        should_be_removed.append(index + 1)
counter = 0
for index in should_be_removed:
    text.pop(index - counter)
    counter += 1
print("".join(text))