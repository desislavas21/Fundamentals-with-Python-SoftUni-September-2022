# Read two integer numbers and, after that, exchange their values. Print the variable values before and after the exchange, as shown below:
# Examples
# Input
# 5
# 10
# Output
# Before:
# a = 5
# b = 10
# After:
# a = 10
# b = 5
# Input
# 10
# 20
# Before:
# a = 10
# b = 20
# After:
# a = 20
# b = 10

a = int(input())
b = int(input())
print(f"Before:\n"
      f"a = {a}\n"
      f"b = {b}")
temp = a
a = b
b = temp
print(f"After:\n"
      f"a = {a}\n"
      f"b = {b} ")
