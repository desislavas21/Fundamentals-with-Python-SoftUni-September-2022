# Write a function that checks if a given password is valid. Password validations are:
# •	It should be 6 - 10 (inclusive) characters long
# •	It should consist only of letters and digits
# •	It should have at least 2 digits
# If a password is valid, print "Password is valid".
# Otherwise, for every unfulfilled rule, print a message:
# •	"Password must be between 6 and 10 characters"
# •	"Password must consist only of letters and digits"
# •	"Password must have at least 2 digits"
# Input	        Output
# logIn	        Password must be between 6 and 10 characters
#               Password must have at least 2 digits
# Input	        Output
# MyPass123	    Password is valid
# Input	        Output
# Pa$s$s	    Password must consist only of letters and digits
#               Password must have at least 2 digits
import string


def password_validator(password):
    password = list(password)
    password_length = len(password)
    valid = True
    counter = 0
    if password_length <= 5 or password_length > 10:
        print("Password must be between 6 and 10 characters")
        valid = False
    for item in password:
        if item in string.digits:
            counter += 1
        if item not in string.ascii_letters and item not in string.digits:
            print("Password must consist only of letters and digits")
            valid = False
            break
    if counter < 2:
        print("Password must have at least 2 digits")
        valid = False
    if valid:
        print("Password is valid")


input_password = input()
password_validator(input_password)