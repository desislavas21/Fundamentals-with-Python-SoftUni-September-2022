# Jenny studies programming with Python and
# wants to create a program that greets the user
# when he/she gives his/her name. The greeting should
# be in the format "Hello, {name}!".
# However, Jenny is in love with Johnny and would like
# to greet him differently: "Hello, my love!". Could you help her?
# Examples
# Input         Output
# Peter         Hello, Peter!
# Amy           Hello, Amy!
# Johnny        Hello, my love!

name = input()

if name != 'Johnny':
    print(f'Hello, {name}!')
else:
    print("Hello, my love!")