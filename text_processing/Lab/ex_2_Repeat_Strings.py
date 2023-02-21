# Write a program that reads a sequence of strings, separated by a single space. Each string should be repeated N times, where N is the length of the string. Print the final strings concatenated into one string.
# Examples
# Input	         Output
# hi abc add	hihiabcabcabcaddaddadd
# work	        workworkworkwork
# ball	        ballballballball

def sequences(words: list):
    final = ""
    for word in words:
        final += (word * len(word))
    print(final)


words = input().split(" ")
sequences(words)