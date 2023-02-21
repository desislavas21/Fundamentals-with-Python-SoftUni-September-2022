# Write a program that receives a sequence of numbers (integers) separated by a single space. It should print a list of only the even numbers. Use filter().
# Example
# Input	            Output
# 1 2 3 4	        [2, 4]
# 1 2 3 -1 -2 -3	[2, -2]


def even_number(numb):
    if numb % 2 == 0:
        return numb


all_numbers = input().split(' ')
int_numbers = []
for number in all_numbers:
    int_numbers.append(int(number))

even_numbers = list(filter(even_number, int_numbers))

print(even_numbers)
