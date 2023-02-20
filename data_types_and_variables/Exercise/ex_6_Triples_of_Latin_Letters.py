#Write a program to read an integer N and print all triples of the first N small Latin letters, ordered alphabetically:
# Example
# Input   Output
# 3       aaa
#         aab
#         aac
#         aba
#         abb
#         abc
#         aca
#         acb
#         acc
#         baa
#         bab
#         bac
#         bba
#         bbb
#         bbc
#         bca
#         bcb
#         bcc
#         caa
#         cab
#         cac
#         cba
#         cbb
#         cbc
#         cca
#         ccb
#         ccc

number = int(input())

for i in range(0, number):
    for j in range(0, number):
        for k in range(0, number):
            print(f"{chr(97 + i)}{chr(97 + j)}{chr(97 + k)}")
