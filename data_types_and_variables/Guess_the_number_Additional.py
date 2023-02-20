import random
computer_number = random.randint(1, 100)
guessed = False

while not guessed:
    player_number = int(input("You number: "))
    if player_number < 1 or player_number > 100:
        print("Try another!")
    if player_number == computer_number:
        print("That's the number!")
        guessed = True
    elif player_number < computer_number:
        print("Bigger")
    elif player_number > computer_number:
        print("Smaller")
