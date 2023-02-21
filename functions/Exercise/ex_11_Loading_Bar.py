# You will receive a single integer number between 0 and 100 (inclusive) divisible by 10 without remainder
# (0, 10, 20, 30...). Your task is to create a function that returns a loading bar depending on the number
# you have received in the input. Print the result on the console. For more clarification, see the examples below.
# Input	    Output
# 30	    30% [%%%.......]
#           Still loading...
# Input 	Output
# 50	    50% [%%%%%.....]
#           Still loading...
# Input	    Output
# 100	    100% Complete!
#           [%%%%%%%%%%]

def loading(number: int):
    baterry = ['.' for x in range(10)]
    for index in range(int(number/10)):
        baterry[index] = "%"
    if number == 100:
        print(f"{number}% Complete!\n[{''.join(baterry)}]")
    else:
        print(f"{number}% [{''.join(baterry)}]\nStill loading...")


number_input = int(input())
loading(number_input)