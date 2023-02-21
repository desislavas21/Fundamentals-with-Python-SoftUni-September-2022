# You will receive a single number. You should write a function that returns the sum of all even and all odd digits in a given number. The result should be returned as a single string in the format:
# "Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"
# Print the result of the function on the console.
# Examples
# Input	                Output
# 1000435	            Odd sum = 9, Even sum = 4
# 3495892137259234	    Odd sum = 54, Even sum = 22


def even_odd(number):
    number = str(number)
    odd = []
    even = []
    for ch in number:
        if int(ch) % 2 == 0:
            even.append(int(ch))
        else:
            odd.append(int(ch))
    sum_of_odd_digits = sum(odd)
    sum_of_even_digits = sum(even)
    print(f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}" )


input_number = int(input())
even_odd(input_number)