# Write a program that reads a string from the console that contains:
# •	Explosions marked with '>'
# •	Immediately after the mark, there will be an integer x, which signifies the strength of the explosion
# •	Any other characters
# Your task is to delete x characters, starting after the exploded character ('>'). If you find another explosion mark ('>') while deleting characters, you should add the strength to your previous explosion. You should not delete the explosion character – '>'.
# When all characters are processed, print the final string.
# Input	                                Output
# abv>1>1>2>2asdasd	                    abv>>>>dasd
# pesho>2sis>1a>2akarate>4hexmaster	    pesho>is>a>karate>master
def string_explosion(data):
    data = data.split(">")
    result = ''
    left = 0
    for letter in data:
        if len(letter) > 1 and any(map(str.isdigit, letter)):
            left += (int(letter[0]) - 1)
            if left >= len(letter):
                result += ">"
            else:
                result += ">" + letter[1 + left:]
                left = 0
        elif len(letter) == 1 and letter.isdigit():
            if int(letter) > 1:
                left += (int(letter) - 1)
            result += ">"
        else:
            result += letter

    return result


data = input()
print(string_explosion(data))