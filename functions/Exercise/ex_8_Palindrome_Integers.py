# A palindrome is a number that reads the same backward as forward, such as 323 or 1001. Write a function that receives
# a list of positive integers, separated by comma and space ", ". The function should check if each integer
# is a palindrome - True or False. Print the result.
# Input
# 123, 323, 421, 121
# Output
# False
# True
# False
# True
# Input
# 32, 2, 232, 1010
# Output
# False
# True
# True
# False

def palindrome(numbers):
    answers = []
    for number in numbers:
        left = []
        right = []
        for i in range(0, len(number) // 2):
            left.append(number[i])
        for z in range(1, len(number) // 2 + 1):
            right.append(number[-z])
        if left == right:
            answers.append(True)
        else:
            answers.append(False)
    for answer in answers:
        print(answer)


input_numbers = input().split(", ")
palindrome(input_numbers)