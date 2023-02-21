# Most football fans love it for the goals and excitement. Well, this problem does not. You are up to handle the referee's little notebook and count the players who were sent off for fouls and misbehavior.
# The rules: Two teams, named "A" and "B" have 11 players each. The players on each team are numbered from 1 to 11. Any player may be sent off the field by being given a red card. If one of the teams has less than 7 players remaining, the referee stops the game immediately, and the team with less than 7 players loses.
# The card is a string with the team's letter ("A" or "B") followed by a single dash and the player's number. e.g., the card "B-7" means player #7 from team B received a card.
# The task: You will be given a sequence of cards (could be empty), separated by a single space. You should print the count of remaining players on each team at the end of the game in the format: "Team A - {players_count}; Team B - {players_count}". If the referee terminated the game, print an additional line: "Game was terminated".
# Note for the random tests: If a player who has already been sent off receives another card - ignore it.
# Input	                            Output
# A-1 A-5 A-10 B-2	                Team A - 8; Team B - 10
# A-1 A-5 A-10 B-2 A-10 A-7 A-3	    Team A - 6; Team B - 10
#                                   Game was terminated

notebook = input().split()
A_team = []
B_team = []

for item in notebook:
    if 'A' in item:
        if item not in A_team:
            A_team.append(item)
    if 'B' in item:
        if item not in B_team:
            B_team.append(item)
    if 11 - len(A_team) < 7 or 11 - len(B_team) < 7:
        break

print(f"Team A - {11 - len(A_team)}; Team B - {11 - len(B_team)}")
if 11 - len(A_team) < 7 or 11 - len(B_team) < 7:
    print("Game was terminated")