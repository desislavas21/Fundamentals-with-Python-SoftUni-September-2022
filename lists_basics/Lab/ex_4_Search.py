# On the first line, you will receive a number n.
# On the second line, you will receive a word.
# On the following n lines, you will be given some strings.
# You should add them to a list and print them.
# After that, you should filter out only the strings that include the given word and print that list too.
# Input
# 3
# SoftUni
# I study at SoftUni
# I walk to work
# I learn Python at SoftUni
# Output
# ["I study at SoftUni", "I walk to work", "I learn Python at SoftUni"]
# ["I study at SoftUni", "I learn Python at SoftUni"]
# Input
# 4
# tomatoes
# I love tomatoes
# I can eat tomatoes forever
# I don't like apples
# Yesterday I ate two tomatoes
# Output
# ["I love tomatoes", "I can eat tomatoes forever", "I don't like apples", "Yesterday I ate two tomatoes"]
# ["I love tomatoes", "I can eat tomatoes forever", "Yesterday I ate two tomatoes"]

n = int(input())
word = input()
statements = []
for i in range(n):
    c_statement = input()
    statements.append(c_statement)
print(statements)

for i in range(len(statements) - 1, -1, -1):
    element = statements[i]
    if word not in element:
        statements.remove(element)
print(statements)