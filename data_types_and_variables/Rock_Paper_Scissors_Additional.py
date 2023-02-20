# Rock-Paper-Scissors is a simple two-player game, where you and your opponent (the computer) simultaneously choose one of the following three options: "rock", "paper", or "scissors". The rules are as follows:
# · Rock beats scissors (the scissors get broken by the rock)
# · Scissors beats paper (the paper gets cut by the scissors)
# · Paper beats rock (the paper covers the rock)
# The winner is the player whose choice beats the choice of his opponent. If both players choose the same option (e.g., "paper"), the game outcome is "draw"

import random
rock, paper, scissors = "Rock", "Paper", "Scissors"
player_move = input("Choose [r]ock, [p]aper, [s]cissors: ")

if player_move == 'r':
    player_move = rock
elif player_move == 'p':
    player_move = paper
elif player_move == 's':
    player_move = scissors
else:
    raise SystemExit("Invalid input. Try again...")

computer_random_number = random.randint(1, 3)
computer_move = ''
if computer_random_number == 1:
    computer_move = rock
elif computer_random_number == 2:
    computer_move = paper
elif computer_random_number == 3:
    computer_move = scissors

if (player_move == rock and computer_move == scissors) or (player_move == paper and computer_move == rock)\
    or (player_move == scissors and computer_move == paper):
    print("You win!")
elif player_move == computer_move:
    print("Draw!")
else:
    print("You lose!")

