# Write a program that reads the path to a file and subtracts the file name and its extension.
# Input
# C:\Internal\training-internal\Template.pptx
# Output
# File name: Template
# File extension: pptx
# Input
# C:\Projects\Data-Structures\LinkedList.cs
# Output
# File name: LinkedList
# File extension: cs
code = input().split("\\")
file, extension = (code[-1]).split(".")
print(f"File name: {file}")
print(f"File extension: {extension}")