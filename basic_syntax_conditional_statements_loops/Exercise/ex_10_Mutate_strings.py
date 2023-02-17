# You will be given two strings.
# Transform the first string into the second one, letter by letter, starting from the first one.
# After each interaction, print the resulting string only if it is unique.
# Note: the strings will have the same length.
# Examples
# Input
# bubble gum
# turtle hum

# Output
# tubble gum
# turble gum
# turtle gum
# turtle hum
#
# Input
# Kitty
# Doggy

# Output
# Ditty
# Dotty
# Dogty
# Doggy

first, second = input(), input()
last_printed = first

for ch_index in range(len(first)):
    left = second[:ch_index+1]
    right = first[ch_index+1:]
    new = left + right
    if new == last_printed:
        continue
    print(new)
    last_printed = new
