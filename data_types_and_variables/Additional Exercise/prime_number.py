# Write a program to check if a number is prime. A prime number is a natural number greater than 1, not a product of two smaller natural numbers. For example, the only ways of writing 5 as a product, 1 × 5 or 5 × 1, involve 5 itself.
# The input comes as an integer number.
# The output should be True if the number is prime and False otherwise.
# Example
# Input	    Output
# 7	        True
# 8	        False
# 81	    False


number = int(input())

prime_number = True

if number > 1:
    for i in range(2, number):
        if number % i == 0:
            prime_number = False
            break

print(prime_number)
