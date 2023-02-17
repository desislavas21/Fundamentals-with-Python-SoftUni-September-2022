# Help out the sorting hat to sort the new students in the houses of Hogwarts.
# You will be receiving names until the command "Welcome!".
# The length of each name determines in which house the student is going:
# · If the name is less than 5 chars, the student is going into Gryffindor
# o Print "{name} goes to Gryffindor."
# · If the name is exactly 5 chars, the student is going into Slytherin
# o Print "{name} goes to Slytherin."
# · If the name is exactly 6 chars, the student is going into Ravenclaw
# o Print "{name} goes to Ravenclaw."
# · If the name is more than 6 chars, the student is going into Hufflepuff
# o Print "{name} goes to Hufflepuff."
# While receiving names, if you receive "Voldemort", print "You must not speak of that name!"
# and end the program. No more sorting for today!
# If all students are sorted successfully, print "Welcome to Hogwarts."
# Example:
# Input
# Harry
# Ron
# Ginny
# Draco
# Welcome!
# Output:
# Harry goes to Slytherin.
# Ron goes to Gryffindor.
# Ginny goes to Slytherin.
# Draco goes to Slytherin.
# Welcome to Hogwarts.
#
# Input
# Luna
# Hermione
# Neville
# Voldemort
# Output
# Luna goes to Gryffindor.
# Hermione goes to Hufflepuff.
# Neville goes to Hufflepuff.
# You must not speak of that name!

command = input()

while command != 'Welcome!':
    name = len(command)
    if command == 'Voldemort':
        print("You must not speak of that name!")
        break
    else:
        if name < 5:
            print(f"{command} goes to Gryffindor.")
        elif name == 5:
            print(f"{command} goes to Slytherin.")
        elif name == 6:
            print(f"{command} goes to Ravenclaw.")
        else:
            print(f"{command} goes to Hufflepuff.")

    command = input()

if command != 'Voldemort':
    print("Welcome to Hogwarts.")