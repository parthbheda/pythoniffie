a = input("Enter first num")
b = input("Enter second num")
c = input("Enter third num")
mini = a
if b < mini:
    mini = b
if c < mini:
    mini = c

print("{} is smallest".format(mini))
