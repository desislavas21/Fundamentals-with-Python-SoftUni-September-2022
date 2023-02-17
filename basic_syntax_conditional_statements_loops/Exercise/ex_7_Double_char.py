# You will be given strings until you receive the command "End".
# For each string given, you should print a string in which each character (case-sensitive) is repeated twice.
# Note that if you receive the string "SoftUni", you should NOT print it!
# Examples
# Input
# Hello World
# Repeat
# End
# Output
# HHeelllloo WWoorrlldd
# RReeppeeaatt

# Input
# 1234!
# SoftUni
# softuni
# End
# Output
# 11223344!!
# ssooffttuunnii

command = input()
new_word = ''

while command != 'End':
    if command != 'SoftUni':
        for i in range(0, len(command)):
            new_word += (2 * command[i])
        print(new_word)
        new_word = ''
    command = input()