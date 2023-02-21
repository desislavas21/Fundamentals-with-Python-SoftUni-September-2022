# A perfect number is a positive integer that is equal to the sum of its proper positive divisors. That is the sum of its positive divisors, excluding the number itself (also known as its aliquot sum).
# Write a function that receives an integer number and returns one of the following messages:
# •	"We have a perfect number!" - if the number is perfect.
# •	"It's not so perfect." - if the number is NOT perfect.
# Print the result on the console.
# Input	    Output
# 6	        We have a perfect number!
# 28	    We have a perfect number!
# 1236498	It's not so perfect.

def checker(number: int):
    divisors = []
    for i in range(1, number):
        if number % i == 0:
            divisors.append(i)
    total = 0
    for number_1 in divisors:
        total += number_1

    if total == number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


number_input = int(input())
print(checker(number_input))