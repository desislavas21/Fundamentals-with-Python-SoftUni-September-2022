# You will be given number n.
# After that, you'll receive different strings n times.
# Your task is to check if the given strings are pure,
# meaning that they do NOT consist of any of the characters: comma ",", period ".", or underscore "_":
# · If a string is pure, print "{string} is pure."
# · Otherwise, print "{string} is not pure!"
# Examples

# Input
# 2
# pure string
# not_pure_string
# Output
# pure string is pure.
# not_pure_string is not pure!

# Input
# 3
# SoftUni
# 12345
# string.pureness
# Output
# SoftUni is pure.
# 12345 is pure.
# string.pureness is not pure!

n = int(input())

for i in range(n):
    current_str = input()
    if ',' in current_str:
        print(f"{current_str} is not pure!")
    elif '.' in current_str:
        print(f"{current_str} is not pure!")
    elif '_' in current_str:
        print(f"{current_str} is not pure!")
    else:
        print(f"{current_str} is pure.")