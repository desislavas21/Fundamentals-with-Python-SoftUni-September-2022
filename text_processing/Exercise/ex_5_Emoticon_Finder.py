# Find all emoticons in the text. An emoticon always starts with ":" and is followed by a symbol.
# The input will be provided as a single string.
# Example
# Input
# There are so many emoticons nowadays :P. I have many ideas :O what input to place here :)
# Output
# :P
# :O
# :)
text = input()
emoticons = []
for index in range(0, len(text)):
    if text[index] == ":":
        emoticons.append(text[index:index+2])
for emoticon in emoticons:
    print(emoticon)

