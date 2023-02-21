# Write a program that returns an encrypted version of the same text. Encrypt the text by replacing each character with the corresponding character three positions forward in the ASCII table. For example, A would be replaced with D, B would become E, and so on. Print the encrypted text.
# Examples
# Input	                    Output
# Programming is cool!	    Surjudpplqj#lv#frro$
# One year has 365 days.	Rqh#|hdu#kdv#698#gd|v1
idea = input()
idea = [ord(ch) for ch in idea]
code = [chr(ch + 3) for ch in idea]
print("".join(code))