# Write a program that finds how many times a word is used in a string.
# The output is a single number indicating the number of times the string contains the word.
# Note that letter case does not matter – it is case-insensitive.
# Examples
# Input	                                                                        Output
# The waterfall was so high, that the child couldn't see its peak.
# the	                                                                        2
# How do you plan on achieving that? How? How can you even think of that?
# how	                                                                        3
# There was one. Therefore I bought it. I wouldn't buy it otherwise.
# there	                                                                        1

import re
sentence = input()
some_word = input()
pattern = fr'\b{some_word}\b'
matches = re.findall(pattern, sentence, flags=re.IGNORECASE)
print(len(matches))
